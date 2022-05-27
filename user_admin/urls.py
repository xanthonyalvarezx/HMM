from django.urls import path
from user_admin.views import  login_view, register_view,logout_view

urlpatterns = [
  # path('createadmin/', add_admin, name="createadmin"),
  path('', login_view, name="login"),
  path('logout/', logout_view, name="logout"),
  path('register/', register_view, name="register")
]