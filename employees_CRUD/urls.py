from django.urls import path, include
from . import views

urlpatterns = [
    # Esta es la URL principal de la aplicación employees_CRUD, donde se mostrará el formulario de 
    # registro de los empleados. Aquí, se manda a llamar del archivo "views.py" la función de vista de 
    # nombre "employee_form" (localhost:8000/employees/))
    path('', views.employee_form),
    # Esta es la URL que se utiliza para listar los empleados, donde se manda a llamar del archivo "views.py"
    # a la función de vista de nombre "employee_list" (localhost:8000/employees/list/)
    path('list/', views.employee_list)
]