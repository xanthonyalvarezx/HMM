from django.urls import path
from pages.views import landing, resources

urlpatterns = [
    path('landing', landing, name="landingpage" ),
    path('resources', resources, name="resourcespage")
]
