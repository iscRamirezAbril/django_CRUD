from django.shortcuts import render

# Create your views here.

# Función de vista que se encargará de mostrar la lista de empleados
def employee_list(request):
    return render(request, "employees_CRUD/employee_list.html")

# Función de vista que se encargará de mostrar el formulario para crear y actualizar un empleado
def employee_form(request):
    return render(request, "employees_CRUD/employee_form.html")

# Función de vista que se encargará de eliminar un empleado
def employee_delete(request):
    return 

