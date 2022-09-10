from django.urls import path

from .views import RegisterUserAPI , loginAPI , LogoutAPI
  

app_name = "user_registration"
urlpatterns = [
    path("register/", view=RegisterUserAPI.as_view(), name="register"),
    path("login/", view=loginAPI.as_view(), name="login"),
    path("logout/", view=LogoutAPI.as_view(), name="logout"),

]