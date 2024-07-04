from django.urls import path
from .views import login_, register, logout_

app_name = 'users'

urlpatterns = [
    path('login/', login_, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_, name='logout'),
]