from django import forms
from django.forms import ModelForm,widgets
from .models import Colaborador

class FormColab(ModelForm):

    class Meta:
        model = Colaborador
        fields = ['RutColab', 'Fotografia', 'Nombre', 'Fono', 'Direcc', 'Email', 'Pais', 'Contra']

        labels={
            'RutColab': 'rut_colaborador',
            'Fotografia': 'foto',
            'Nombre': 'nombre',
            'Fono': 'telefono',
            'Direcc': 'direccion',
            'Email': 'correo',
            'Pais': 'pais',
            'Contra': 'contraseña',

        }
        widgets={
            'RutColab':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'rut',
                    'name': 'rut',
                    'placeholder': 'ingresar_rut'
                }
            ),
            'Nombre':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'nombre',
                    'name': 'nombre',
                    'placeholder': 'nombre_colaborador'
                }
            ),
            'Fono':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'telefono',
                    'name': 'telefono',
                    'placeholder': 'Telefono'
                }
            ),
            'Direcc':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'direccion',
                    'name': 'direccion',
                    'placeholder': 'calle'
                }
            ),
            'Email':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'correo',
                    'name': 'correo',
                    'placeholder': 'correo_electronico'
                }
            ),
            'Pais':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'pais',
                    'name': 'pais',
                    'placeholder': 'ingrese_pais'
                }
            ),
            'Contra':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'password',
                    'name': 'password',
                    'placeholder': 'ingrese_contraseña'
                }
            ),
        }