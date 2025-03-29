from django.urls import path
from django.contrib import admin
from .views import (clientes_view, criar_cliente, criar_despesa, despesas_view, criar_quarto,
                    quartos_view, criar_receita, receitas_view, criar_reserva, reservas_view, 
                    criar_servico, servicos_view, dashboard,  logout_view, login_view, register_view,
                    relatorios_view, )
                    
urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    
    path('clientes/', clientes_view, name='clientes'),
    path('clientes/criar/', criar_cliente, name='criar_cliente'),
    
    path('despesas/', despesas_view, name='despesas'),
    path('despesas/criar/', criar_despesa, name='criar_despesa'),

    path('quartos/', quartos_view, name='quartos'),
    path('quartos/criar/', criar_quarto, name='criar_quarto'),

    path('receitas/', receitas_view, name='receitas'),
    path('receitas/criar/', criar_receita, name='criar_receita'),

    path('reservas/', reservas_view, name='reservas'),
    path('reservas/criar/', criar_reserva, name='criar_reserva'),  

    path('servicos/', servicos_view, name='servicos'),
    path('servicos/criar/', criar_servico, name='criar_servico'),

    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('relatorios/', relatorios_view, name='relatorios'),
   
    
]