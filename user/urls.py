from django.urls import path, include


from .views import RegistrationAPIView, LoginAPIView
#  ChangePasswordView
from . import views

app_name = 'user'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),

]

# path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail')
# path('change-password/<int:pk>',
#      views.ChangePasswordView.as_view(), name='change_password'),
