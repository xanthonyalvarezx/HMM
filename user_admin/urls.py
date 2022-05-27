from django.urls import path
from user_admin.views import  login_view

urlpatterns = [
  # path('createadmin/', add_admin, name="createadmin"),
  path('', login_view, name="login")
]