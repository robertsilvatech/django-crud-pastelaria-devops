from django import forms
from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Produto XYZ'}), required=False)
    preco = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '999.99'}), required=False)
    qtd_estoque = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 10}), required=False)
    class Meta:
        model = Produto
        fields = '__all__'