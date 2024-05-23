from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer, LoginSerializer
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# 회원가입
class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # 사용자 생성 및 저장
            return Response({"message": "회원가입 성공"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 로그인
class LoginView(APIView):
    # POST 요청
    def post(self, request):
        # 전달받은 이메일과 비밀번호를 사용하여 LoginSerializer를 초기화
        serializer = LoginSerializer(data=request.data)

        # 유효성 검사 및 유저 인증 수행
        if request.method == 'POST':
            if serializer.is_valid():
                user = serializer.validated_data['user']  # 유저 객체 가져오기
                user_id = str(user.id)  # 유저 아이디 가져오기

                # 유저 인증 성공 시, 토큰 생성
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                # 로그인 성공 메시지와 토큰, 유저 이메일 반환
                response_data = {
                    "message": "로그인 성공",
                    "token": access_token,
                    "user": user_id,
                }

                # 유효성 검사 성공 시, 클라이언트에게 반환
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                # 유효성 검사 실패 시, 에러 메시지 반환
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # GET 요청에 대한 처리
    def get(self, request):
        # GET 요청을 거부하고 "Method Not Allowed" 응답을 반환
        if request.method == 'GET':
            return Response({"message": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



# 사용자 삭제
class UserDeleteView(APIView):
    def delete(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"message": "A user with that id does not exist."}, status=status.HTTP_404_NOT_FOUND)


        