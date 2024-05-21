from django.urls import path
from . import views

urlpatterns =[
    path('signup/', views.SignUpView.as_view(), name='user_signup'),  # 회원가입
    path('login/', views.LoginView.as_view(), name='user_login'),   # 로그인
    path('delete/<int:user_id>/', views.UserDeleteView.as_view(), name='user_delete'),  # 사용자 삭제
 ]