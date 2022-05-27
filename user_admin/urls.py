from django.urls import path
from user_admin.views import  login_view, register_view

urlpatterns = [
  # path('createadmin/', add_admin, name="createadmin"),
  path('', login_view, name="login"),
  path('register/', register_view, name="register")
]