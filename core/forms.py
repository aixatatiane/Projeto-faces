from django import forms
from .models import Face

class FacesModelForm(forms.ModelForm):
    class Meta:
        model = Face
        fields = [
            'nome', 'descricao', 'ocupacao',
            'data_nascimento', 'data_falecimento', 'imagem',
            'postado_por',
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'ocupacao': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_falecimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'postado_por': forms.Select(attrs={'class': 'form-control'}),
        }
