from django.urls import path
from . import views

urlpatterns = [
    path('', views.loader, name="loader"),
    path('home/', views.home, name="home"),
    path('login/', views.elderaccount, name="elderAccountLogin")
    # path('register/', views.register, name='register'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('', views.home, name='home')
]
