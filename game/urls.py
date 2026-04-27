from django.urls import path
from game import views
urlpatterns = [
   path('',views.game_list,name='game_list'),
   path('create/',views.game_create,name='game_create'),
   path('create_save/',views.game_create_save,name='game_create_save'),
   path('game_update/<int:pk>/',views.game_update,name='game_update'),
   path('game_update_save/<int:pk>/',views.game_update_save,name='game_update_save'),
]
