from django.urls import path
from .views import login_view, register_view, logout_

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_, name='logout'),
]