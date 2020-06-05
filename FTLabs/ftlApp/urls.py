from django.urls import path

from .import views

app_name = 'ftlApp'

urlpatterns = [
    path('',views.home, name='home'),
    path('sign_up/', views.createUser, name='createUser'),
    path('login/', views.login),

]