from django import forms
from .models import Faces

class FacesModelForm(forms.ModelForm):
    class Meta:
        model = Faces
        fields = [
            'nome', 'descricao', 'ocupacao',
            'data_nascimento', 'data_falecimento', 'imagem',
            'postado_por',
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricai': forms.Textarea(attrs={'class': 'form-control'}),
            'ocupacao': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'data_falecimento': forms.DateInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }