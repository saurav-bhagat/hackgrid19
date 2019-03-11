from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.base_demo, name='base-api'),
]