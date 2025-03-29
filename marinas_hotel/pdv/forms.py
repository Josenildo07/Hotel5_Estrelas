from django import forms
from .models import Cliente, Quarto, Reserva, Despesa, Receita, Servico
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone']

class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = ['numero', 'tipo', 'preco']

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ['cliente', 'quarto', 'data_ent', 'data_sai']
        widgets = {
        'data_ent': forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA', 'type': 'date'}),
        'data_sai': forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA', 'type': 'date'}),}
        

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['desc_desp', 'valor_desp', 'data_desp']
        widgets = {
        'data_desp': forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA', 'type': 'date'}),}

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['desc_rec', 'valor_rec', 'data_rec']
        widgets = {
        'data_rec': forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA', 'type': 'date'}),}

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'preco']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem.")
    