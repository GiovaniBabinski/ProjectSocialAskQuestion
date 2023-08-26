from django.urls import path
from .views import perguntas_list,pergunta_detalhes,registrar,create_pergunta,update_pergunta,delete_pergunta,update_resposta,change_profile,list_info,delete_resposta

urlpatterns = [
    path('feed/',perguntas_list, name='perguntas'),
    path('pergunta/<slug:slug>/', pergunta_detalhes, name='pergunta_detalhes'),
    path('registrar/',registrar, name='register'),
    path('add-pergunta/', create_pergunta, name = 'add_pergunta'),
    path('update/<slug:slug>/',update_pergunta, name='update_pergunta'),
    path('delete/<slug:slug>/', delete_pergunta, name='delete_pergunta'),
    path('resposta/atualizar/<int:id>/', update_resposta, name='update_resposta'),
    path('resposta/delete/<int:id>/', delete_resposta, name='delete_resposta'),
    path('profile/', change_profile, name='profile'),
    path('list/', list_info, name='list_info'),

]
