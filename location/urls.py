from django.urls import path
from .views import index, update_location

urlpatterns = [
    path('', index, name='index'),
    path('update-location/', update_location, name='update_location'),
]

