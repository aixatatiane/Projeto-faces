from django.urls import path
from .views import benvindo, faces, index, participantes, reflexao

app_name = 'core'

urlpatterns = [
    path('', index, name='home'),
    path('faces/', faces, name='faces'),
    path('ben-vindo/', benvindo, name='benvindo'),
    path('participantes/', participantes, name='participantes'),
    path('reflexao-filosofica/', reflexao, name='reflexao'),
    path('reflexao-filosofica/', reflexao, name='reflexao'),
]