from django.urls import path
from skills import views
urlpatterns = [
    path('',views.skills_list,name='skills_list'),
    path('skills_create/',views.skills_create,name='skills_create'),
    path('skills_create_save/',views.skills_create_save,name='skills_create_save'),
    path('skills/skills_create_update/<int:pk>/', views.skills_create_update, name='skills_create_update'),
    path('skills_update/',views.skills_update,name='skills_update'),

]