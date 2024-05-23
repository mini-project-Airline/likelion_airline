from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # 유저 생성
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        # 직렬화 필드
        fields = ['email', 'firstName', 'lastName', 'password']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    # 유효성 확인
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # 유저 인증(email과 password를 사용해 인증)
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user: # 유저 인증 안됐을 경우
                msg = '이메일 또는 비밀번호가 잘못되었습니다.'
                # 인증 오류
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = '이메일과 비밀번호를 입력해주세요.'
            # 입력할 필수 필드 누락할 경우 예외 발생
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user  # 유저 객체 추가
        return attrs