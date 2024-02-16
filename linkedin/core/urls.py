# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('members/', views.members_list, name='members_list'),
    path('profile/<int:user_id>/', views.profile,
         name='profile'),

]
