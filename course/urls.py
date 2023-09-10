from django.urls import path
from . import views

urlpatterns = [
    #To add 
    path('create/', views.create, name='create_course'),

    #To read 
    path('read/', views.read, name='read_course'),

    #To edit 
    path('edit/<int:pk>', views.edit, name='edit_course'),

    #To delete 
    path('delete/<int:pk>', views.delete, name='delete_course'),
]