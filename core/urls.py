from django.urls import path
from .views import faces, index, participantes, reflexao, faces_detalhe, atualizar_face, deletar_face, cadastrar_face

app_name = 'core'

urlpatterns = [
    path('', index, name='home'),
    path('faces/', faces, name='faces'),
    path('faces/<int:id>/', faces_detalhe, name='faces-detalhe'),
    path('faces/<int:id>/atualizar/', atualizar_face, name='atualizar-face'),
    path('faces/<int:id>/deletar/', deletar_face, name='faces-deletar'),
    path('faces/cadastrar/', cadastrar_face, name='cadastrar-face'),
    path('participantes/', participantes, name='participantes'),
    path('reflexao-filosofica/', reflexao, name='reflexao'),
]