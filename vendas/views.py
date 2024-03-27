from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import *
from .models import *

class IndexView(ListView):
    model = Venda
    template_name = 'index.html'
    success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vendas"] = Venda.objects.all()
        return context


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'form.html'
    fields = ['nome', 'preco', 'imagem']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Criando Produto'
        context["botao"] = 'Criar Produto'
        context["corbtn"] = 'success'
        return context
    
class CreateVendaView(CreateView):
    model = Venda
    template_name = 'form.html'
    fields = ['produto', 'cliente', 'quantidade_vendida']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Registrando Venda'
        context["botao"] = 'Registrar Venda'
        context["corbtn"] = 'success'
        return context

class UpdateVendaView(UpdateView):
    model = Venda
    fields = ['produto', 'cliente', 'quantidade_vendida']
    template_name = 'form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Editando Venda'
        context["botao"] = 'Editar Venda'
        context["corbtn"] = 'primary'
        return context


class DeleteVendaView(DeleteView):
    model = Venda
    success_url = reverse_lazy('index')