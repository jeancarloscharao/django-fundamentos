from django import forms
from .models import Cliente, Endereco


class ClienteForm(forms.ModelForm):
    class Meta():
        model = Cliente
        fields = ['nome', 'data_nascimento', 'email', 'profissao', 'sexo']


class EnderecoForm(forms.ModelForm):
    class Meta():
        model = Endereco
        fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'pais']
