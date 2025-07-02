from django.urls import path, include
from . import views



urlpatterns = [
    
    path('register/', views.home, name='register'),
    path('verify/', views.verify, name='verify'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard')
]
