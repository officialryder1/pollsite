from django.urls import path
from .views import Index, post_vote, login_user, logout_user, register_user

urlpatterns = [
   path('', Index, name='home'),
   path('like/<int:pk>', post_vote, name='vote'),
   path('logout', logout_user, name='logout'),
   path('login_user', login_user, name='login'),
   path('register', register_user, name='register')
]