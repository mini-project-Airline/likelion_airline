from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.utils import IntegrityError
import secrets

# 유저 생성 및 관리 : 일반유저/관리자유저
class UserManager(BaseUserManager):
    # 일반유저 생성
    def create_user(self, email, firstName, lastName, password=None):
        if not email:
            raise ValueError('must have user email')
        if not firstName:
            raise ValueError('must have user firstName')
        if not lastName:
            raise ValueError('must have user lastName')
        user = self.model(
            email=self.normalize_email(email),
            firstName=firstName,
            lastName=lastName
        )
        user.set_password(password)  # 비밀번호를 해시하여 저장
        user.save(using=self._db)
        
        # 사용자 생성 후 토큰 생성 및 연결
        try:
            token = Token.objects.create(user=user)
            token.token = secrets.token_hex(20)  # 랜덤한 토큰 생성
            token.save()
        except IntegrityError:
            pass  # 토큰 생성 실패 시 처리
        
        return user

    # 관리자유저 생성
    def create_superuser(self, email, firstName, lastName, password=None):
        user = self.create_user(
            email,
            password=password,
            firstName=firstName,
            lastName=lastName
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        # 관리자유저 생성 후 토큰 생성 및 연결
        try:
            token = Token.objects.create(user=user)
            token.token = secrets.token_hex(20)  # 랜덤한 토큰 생성
            token.save()
        except IntegrityError:
            pass  # 토큰 생성 실패 시 처리
        
        return user
    

# 유저
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100, null=False, blank=False)
    lastName = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)
    is_active = models.BooleanField(default=True)  # 유저 활성화
    is_staff = models.BooleanField(default=False)  # False: 일반유저
    
    objects = UserManager()  # 유저 생성 및 관리

    USERNAME_FIELD = 'email'  # 유저이름 = 이메일
    REQUIRED_FIELDS = ['firstName', 'lastName']  # 유저 생성 시 입력해야할 필수 필드

    def __str__(self):
        return self.user

    # 유저 특정 권한 확인
    def has_perm(self, perm, obj=None):
        return True

    # 유저 특정 앱에 대한 권한 확인
    def has_module_perms(self, app_label):
        return True


# 토큰
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 유저와 연결
    token = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.token
