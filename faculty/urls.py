from django.urls import path
from . import views

urlpatterns = [
    #To add 
    path('create/', views.create, name='create_faculty'),

    #To read 
    path('read/', views.read, name='read_faculty'),

    #To edit 
    path('edit/<int:pk>', views.edit, name='edit_faculty'),

    #To delete 
    path('delete/<int:pk>', views.delete, name='delete_faculty'),
]