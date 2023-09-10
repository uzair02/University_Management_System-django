from django.urls import path
from . import views

urlpatterns = [
    #To add 
    path('create/', views.create, name='create_enr'),

    #To read 
    path('read/', views.read, name='read_enr'),

    #To edit 
    path('edit/<int:pk>', views.edit, name='edit_enr'),

    #To delete 
    path('delete/<int:pk>', views.delete, name='delete_enr'),
]