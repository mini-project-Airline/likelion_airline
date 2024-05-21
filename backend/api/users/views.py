from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer, LoginSerializer
from .models import User

# 회원가입
class SignUpView(APIView):
    # POST 요청
    def post(self, request):
        serializer = UserSerializer(data=request.data)  # 데이터 직렬화
        # 데이터 유효성 검사
        if serializer.is_valid():
            serializer.save()  # 유저 데이터 DB 저장
            # 유저 생성 성공 시 응답
            return Response({"message": "회원가입 성공"}, status=status.HTTP_201_CREATED)
        # 유저 생성 실패 시 응답
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 로그인
class LoginView(APIView):
    # POST 요청
    def post(self, request):
        serializer = LoginSerializer(data=request.data)  # 데이터 직렬화
        # 데이터 유효성 검사
        if serializer.is_valid():
            # 유저 인증(email과 password를 사용해 인증)
            user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
            # 유저 인증 확인
            if user:
                refresh = RefreshToken.for_user(user)  # 새로운 토큰 생성
                # 생성된 리프레시 토큰, 엑세스 토큰을 포함한 딕셔너리 생성
                token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                # 로그인 성공 시 응답
                response_data = {
                    "message": "로그인 성공",
                    "token": token,
                    "user": user.email
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                # 로그인 실패 시 응답
                return Response({"message": "로그인에 실패했습니다."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 사용자 삭제
class UserDeleteView(APIView):
    def delete(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)  # user_id에 해당하는 DB 가져오기
            user.delete()  # 가져온 유저 삭제
            # 유저 삭제 성공 시 응답
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            # 유저 삭제 실패 시 응답
            return Response({"message": "A user with that ID does not exist."}, status=status.HTTP_404_NOT_FOUND)
        