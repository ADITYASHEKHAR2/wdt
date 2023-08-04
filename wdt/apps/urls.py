from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('about',views.about,name='about'),
    path('calculator',views.calculator,name="calculator"),
    path('tic-tac-toe',views.ttt,name="ttt"),
    path("to-do-list",views.tdl,name="tdl"),
    path("rock-paper-scissor",views.rps,name="rps"),
]
