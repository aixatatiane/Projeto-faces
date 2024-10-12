from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control usuario w-100',
                    'placeholder': 'Digite sua nome de usuario',
                    'id': 'usuario',
                    'style': """
                        width: 100% !important; height: 4.375rem; font-family: var(--font-family-main);
                        border-radius: var(--border-radius); border: 1px solid var(--text-color-black);
                        font-size: var(--font-size-medium); font-weight: 400; background: var(--background-color); 
                        color: var(--text-color-black); font-family: var(--font-family-main);
                        font-size: var(--font-size-medium); font-weight: 400;'idth: 29.1875rem; height: 4.375rem;
                        font-family: var(--font-family-main); border-radius: var(--border-radius);
                        border: 1px solid var(--text-color-black); font-size: var(--font-size-medium);
                        font-weight: 400; background: var(--background-color);   color: var(--text-color-black);
                        font-family: var(--font-family-main); font-size: var(--font-size-medium); font-weight: 400;
                    """
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control w-100 email',
                    'placeholder': 'Digite seu email',
                },
            ),
        }

    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control w-100 senha',
                'placeholder': 'Digite sua senha',
            })
    )
    password2 = forms.CharField(
        label='Confirm Password', 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control w-100 senha',
                'placeholder': 'Confirme sua senha',
            })
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username', 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control w-100 mb-3 usuario',
                'placeholder': 'Informe seu nome de usuario',
                'id': 'usuario',
                'style': """
                    width: 29.1875rem; height: 4.375rem; font-family: var(--font-family-main);
                    border-radius: var(--border-radius); border: 1px solid var(--text-color-black);
                    font-size: var(--font-size-medium); font-weight: 400; background: var(--background-color); 
                    color: var(--text-color-black); font-family: var(--font-family-main);
                    font-size: var(--font-size-medium); font-weight: 400;'idth: 29.1875rem; height: 4.375rem;
                    font-family: var(--font-family-main); border-radius: var(--border-radius);
                    border: 1px solid var(--text-color-black); font-size: var(--font-size-medium);
                    font-weight: 400; background: var(--background-color);   color: var(--text-color-black);
                    font-family: var(--font-family-main); font-size: var(--font-size-medium); font-weight: 400;
                """
            })
    )
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control w-100 mb-3 senha',
                'placeholder': 'Informe sua senha',
            }
        )
    )
