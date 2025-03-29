from django.contrib import admin
from .models import Cliente, Quarto, Reserva, Despesa, Receita, Servico


# Registre os modelos para que apareçam no painel de administrador
admin.site.register(Cliente)
admin.site.register(Quarto)
admin.site.register(Reserva)
admin.site.register(Despesa)
admin.site.register(Receita)
admin.site.register(Servico)