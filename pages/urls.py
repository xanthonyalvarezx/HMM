from django.urls import path
from pages.views import landing

urlpatterns = [
    path('landing', landing, name="landingpage"  )
]
