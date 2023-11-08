from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby),
    path('room/', views.room),

    path('get_token/', views.get_token),
    path('create_member/', views.create_member),
]