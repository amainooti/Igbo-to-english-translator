from django.urls import path
from .views import home  # Import your view function

urlpatterns = [
    path('', home, name='home'),  # Assumes you have a view named 'home'
    # Add more paths as needed
]
