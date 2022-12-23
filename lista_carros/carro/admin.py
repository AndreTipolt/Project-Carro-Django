from django.contrib import admin
from .models import Categoria, Carro

class CarroAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'marca', 'ano', 'categoria')

    list_display_links = ('id', 'nome')




admin.site.register(Categoria)
admin.site.register(Carro, CarroAdmin)
