from django import forms # Se importan los formularios de Django
from . models import Employee # Se importa el modelo Employee del archivo models.py

# Como parámetro de la clase "employeeForm", del módulo "forms", se utilizará la clase "ModelForm".
class employeeForm(forms.ModelForm):
    # class Meta: Se utiliza para definir los atributos de la clase "employeeForm".
    class Meta:
        model = Employee # Se define el modelo que utilizará la clase "employeeForm".
        fields = '__all__' # Se definen los campos que utilizará la clase "employeeForm", en este caso, todos los campos del modelo "Employee".