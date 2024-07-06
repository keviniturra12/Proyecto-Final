from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente,SolicitudServicio

class ClienteRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    address = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'address', 'date_of_birth', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            cliente = Cliente(user=user, phone=self.cleaned_data['phone'], address=self.cleaned_data['address'], date_of_birth=self.cleaned_data['date_of_birth'])
            cliente.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está en uso.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("El número de teléfono debe contener solo dígitos.")
        return phone

class SolicitudServicioForm(forms.ModelForm):
    class Meta:
        model = SolicitudServicio
        fields = ['tipo_servicio', 'titulo', 'descripcion', 'archivo_adjunto']

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if SolicitudServicio.objects.filter(titulo=titulo).exists():
            raise forms.ValidationError("Una solicitud con este título ya existe.")
        return titulo

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if len(descripcion) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return descripcion   

class ActualizarSolicitudFormtTecnico(forms.ModelForm):

    class Meta:
        model = SolicitudServicio
        fields = ['estado', 'abogado']


class ActualizarSolicitudForm(forms.ModelForm):
    class Meta:
        model = SolicitudServicio
        fields = ['estado']
