from django.contrib import admin

from .models import *

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    pass


