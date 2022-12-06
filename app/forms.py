from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator


class ContactoForm(forms.ModelForm):

   	class Meta: 
          model = Contacto
          #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
          #De esta forma pod+riamos sólo importar algunos del modelo
          fields = '__all__' 
          #Con esto importamos todos	

class ProductoForm(forms.ModelForm):

       nombre = forms.CharField(min_length=3, max_length=50)
       imagen = forms.ImageField(required=True, validators=[MaxSizeFileValidator(max_file_size=2)])
       precio = forms.IntegerField(min_value=1, max_value=1500000)

       class Meta:
              model = Producto
              fields = '__all__'

              widgets = {
                     "fecha_fabricacion": forms.SelectDateWidget()
              }
              #No es lo más elegante, lo ideal es cargar un pluggin de js

class CustomUserCreationForm(UserCreationForm):
       #De esta forma tenemos control si en el futuro queremos hacer valdaciones

       class Meta:
              model = User
              fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

#Esto podemos hacerlo porque los datos ya están en la tabla, si queremos agregar otros habría que hacerlo de otra forma.