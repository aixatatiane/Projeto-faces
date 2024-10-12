from django.contrib import admin
from .models import Face

@admin.register(Face)
class FacesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ocupacao', 'data_nascimento', 'data_falecimento', 'postado_por')
    search_fields = ('nome', 'ocupacao', 'descricao')
    list_filter = ('ocupacao', 'data_nascimento', 'data_falecimento')
    date_hierarchy = 'data_nascimento'
