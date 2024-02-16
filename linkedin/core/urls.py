# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('members/', views.members_list, name='members_list'),
    path('profile/', views.profile_user, name='profile'),
    path('view_profile/<int:user_id>/', views.view_profile,
         name='view_profile'),

]
