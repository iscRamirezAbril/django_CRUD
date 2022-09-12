from django.urls import path, include
from . import views

urlpatterns = [
    # Esta es la URL principal de la aplicación employees_CRUD, donde se mostrará el formulario de 
    # registro de los empleados. Aquí, se manda a llamar del archivo "views.py" la función de vista de 
    # nombre "employee_form" (localhost:8000/employees/))
    path('', views.employee_form, name='employee_insert'), # GET and POST request for insert operation
    
    # Esta es la URL que se utiliza para modificar los datos de un empleado registrado. Aquí, se está tomando de
    # referencia el ID del empleado que se desea modificar (localhost:8000/employees/1/update). Cabe mencionar que
    # tambien se le está dando un nombre a la URL para poder utilizarla en el archivo "employee_list.html" (name="update_employee")
    path('<int:id>/', views.employee_form, name='employee_update'),
    
    # Esta es la URL que se utiliza para listar los empleados, donde se manda a llamar del archivo "views.py"
    # a la función de vista de nombre "employee_list" (localhost:8000/employees/list/)
    path('list/', views.employee_list, name='employee_list'),
]