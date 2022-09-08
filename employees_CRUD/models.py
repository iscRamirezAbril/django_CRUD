# |-----| Emportación de librerías |-----|
from pyexpat import model # De pyexpat importa model 
from django.db import models # De django.db importa models

# Create your models here.

# |-----| CLASE #1: Position |-----|
# Clase que almacenará los puestos de trabajo de los empleados
class Position(models.Model): # Del módulo models, importamos la clase Model
    posTitle = models.CharField(max_length=50) # Campo que almacenará el nombre del puesto de trabajo

# |-----| CLASE #2: Employee |-----|
# Clase que almacenará los datos de los empleados
class Employee(models.Model): # Del módulo models, importamos la clase Model
    empFirtsName = models.CharField(max_length=50, null=False) # Campo que almacenará el nombre del empleado
    empLastName = models.CharField(max_length=50, null=False) # Campo que almacenará el apellido del empleado
    empCode = models.CharField(max_length=3, null=False) # Campo que almacenará el código del empleado
    empPhoneNum = models.CharField(max_length=10, null=False) # Campo que almacenará el número de teléfono del empleado
    empEmail = models.EmailField(max_length=50, null=False) # Campo que almacenará el correo electrónico del empleado
    empRegisterDate = models.DateField(auto_now=False, auto_now_add=True) # Campo que almacenará la fecha de registro del empleado
    # |----------| Relación de la clase Employee con la clase Position (LLAVE FORÁNEA) |----------| #
    empPosition = models.ForeignKey(Position, on_delete=models.CASCADE, null=False) # Campo que almacenará el puesto de trabajo del empleado
