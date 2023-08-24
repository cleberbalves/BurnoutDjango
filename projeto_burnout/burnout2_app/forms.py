# burnout_app/forms.py
from django import forms

class EntradaValoresForm(forms.Form):
    nome = forms.CharField(max_length=100)
    idade = forms.IntegerField()
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Feminino')])
    email = forms.EmailField()
