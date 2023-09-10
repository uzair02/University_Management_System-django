from django.urls import path
from . import views

urlpatterns = [
    #To add 
    path('create/', views.create_dept, name='create_dept'),

    #To read 
    path('read/', views.read_dept, name='read_dept'),

    #To edit 
    path('edit/<int:pk>', views.edit_dept, name='edit_dept'),

    #To delete 
    path('delete/<int:pk>', views.delete_dept, name='delete_dept'),
]