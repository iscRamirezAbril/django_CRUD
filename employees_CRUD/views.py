from django.shortcuts import render

from employees_CRUD.forms import employeeForm # Se importa la clase "employeeForm" del archivo forms.py
from .forms import employeeForm # Se importa la clase "employeeForm" del archivo forms.py
from django.shortcuts import render, redirect # Se importan las funciones "render" y "redirect" de Django
from .models import Employee # Se importa la clase "Employee" del archivo models.py

# Create your views here.

# Función de vista que se encargará de mostrar la lista de empleados
def employee_list(request):
    context = {'employee_list': Employee.objects.all()} # Se crea un diccionario con la lista de empleados
    return render(request, "employees_CRUD/employee_list.html", context)

# Función de vista que se encargará de mostrar el formulario para crear y actualizar un empleado
def employee_form(request, id = 0): 
    # Si el método de la petición es GET, se ejecutará el siguiente código
    if request.method == "GET": 
        # Si el ID es igual a 0, se ejecutará el siguiente código
        if id == 0:
            form = employeeForm() # Se crea una instancia de la clase "employeeForm"
        else:
            employee = Employee.objects.get(pk=id) # Se obtiene el empleado que se desea modificar mediante el ID (llaave primaria)
            form = employeeForm(instance=employee) # Se crea una instancia de la clase "employeeForm" con los datos del empleado
        # Se renderiza el archivo "employee_form.html" y se le pasa como parámetro el formulario "form"
        return render(request, "employees_CRUD/employee_form.html", {'form': form})

    # Si el método de la petición es POST, se ejecutará el siguiente código
    else:
        if id == 0:
            form = employeeForm(request.POST) # Se crea una instancia de la clase "employeeForm" y se le pasa como parámetro la petición POST
        else:
            employee = Employee.objects.get(pk=id) # Se obtiene el empleado que se desea modificar mediante el ID (llaave primaria)
            form = employeeForm(request.POST, instance=employee) # Se crea una instancia de la clase "employeeForm" y se le pasa como parámetro la petición POST y el empleado
        if form.is_valid(): # Si el formulario es válido, se ejecutará el siguiente código
            form.save() # Se guarda el formulario y la información del empleado registrada en la base de datos
        # Se procede a redireccionar al usuario a la página de la lista de empleados (localhost:8000/employees/list/)
        return redirect('/employees/list/')
            
# Función de vista que se encargará de eliminar un empleado
def employee_delete(request, id): # Se recibe como parámetro el ID del empleado que se desea eliminar
    employee = Employee.objects.get(pk=id) # Se obtiene el empleado que se desea modificar mediante el ID (llaave primaria)
    employee.delete() # Se elimina el empleado
    return redirect('/employees/list/') # Se procede a redireccionar al usuario a la página de la lista de empleados (localhost:8000/employees/list/)