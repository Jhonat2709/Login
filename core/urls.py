from django.urls import path
from . import views
from .utils import loginValidation
from .views import dashboard

#Create your urls here
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('login/', views.signin, name="login"),
    path('login-process/', loginValidation.loginProcess, name="login-process"),
    path('logout/', views.signout, name="logout"),
    path('dashboard/', views.dashboard, name='dashboard'),
]

