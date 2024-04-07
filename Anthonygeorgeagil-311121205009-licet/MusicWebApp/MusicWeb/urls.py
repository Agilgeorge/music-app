from django.urls import path
from . import views

urlpatterns = [
    path('Songs/', views.songs, name = 'songs'),
    path('Songs/<int:id>', views.songpost, name = 'songpost'),
    path('login',views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('logout', views.logout_user, name ="logout"),
    path('search', views.search, name = 'search')
]
