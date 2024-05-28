# api/auths/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from api.users.models import User

class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        old_password = request.data.get('oldPassword')
        new_password = request.data.get('newPassword')

        if not old_password or not new_password:
            return Response({"message": "Old password and new password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # 인증된 사용자의 현재 비밀번호를 확인합니다.
        authenticated_user = authenticate(email=user.email, password=old_password)
        if authenticated_user is None:
            return Response({"message": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)

        # 새로운 비밀번호를 설정합니다.
        authenticated_user.set_password(new_password)
        authenticated_user.save()

        return Response({"message": "비밀번호가 변경되었습니다."}, status=status.HTTP_200_OK)
