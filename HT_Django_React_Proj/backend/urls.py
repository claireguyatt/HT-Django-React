from django.urls import path, include
from . import views

urlpatterns = [

    path('users/', views.create_user),
    path('users/<int:pk>/', views.user_detail)

]