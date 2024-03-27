from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('criar-produto/', CreateProdutoView.as_view(), name="criar-produto"),
    path('registrar-venda/', CreateVendaView.as_view(), name="registrar-venda"),
    path('venda/<int:pk>/editar', UpdateVendaView.as_view(), name="editar-venda"),
    path('venda/<int:pk>/delete', DeleteVendaView.as_view(), name="deletar-venda"),
]