from django.urls import path
from . import views

# Define url patterns

urlpatterns = [
  path('', views.index)
]