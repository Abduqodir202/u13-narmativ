from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.tables_list, name='tables_list'),
    path('detail/<int:pk>/', views.tables_detail, name='tables_detail'),
    path('create_form/', views.tables_create_form, name='tables_create_form'),
    path('create/', views.tables_create, name='tables_create'),
    path('update_form/<int:pk>/', views.tables_update_forme, name='tables_update_form'),
    path('update/<int:pk>/', views.tables_update, name='tables_update'),
    path('delete/<int:pk>/', views.tables_delete, name='tables_delete'),
]
