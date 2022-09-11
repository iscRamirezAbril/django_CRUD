from django.shortcuts import render

from employees_CRUD.forms import employeeForm # Se importa la clase "employeeForm" del archivo forms.py
from .forms import employeeForm # Se importa la clase "employeeForm" del archivo forms.py

# Create your views here.

# Función de vista que se encargará de mostrar la lista de empleados
def employee_list(request):
    return render(request, "employees_CRUD/employee_list.html")

# Función de vista que se encargará de mostrar el formulario para crear y actualizar un empleado
def employee_form(request):
    form = employeeForm() # Se crea una instancia de la clase "employeeForm"
    # Se renderiza el archivo "employee_form.html" y se le pasa como parámetro el formulario "form"
    return render(request, "employees_CRUD/employee_form.html", {'form': form})

# Función de vista que se encargará de eliminar un empleado
def employee_delete(request):
    return 

