from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Sum
from rest_framework.viewsets import ModelViewSet

from .forms import *
from .models import *
from vendas.api.serializers import ProdutosSerializer, VendasSerializer

class IndexView(LoginRequiredMixin, ListView):
    model = Venda
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vendas"] = Venda.objects.all()
        faturamento = Venda.objects.aggregate(Sum('produto__preco'))
        if faturamento['produto__preco__sum'] is None:
            context["faturamento"] = False
        else:
            context["faturamento"] = round(faturamento['produto__preco__sum'],2)
        return context


class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produtos.html'
    success_url = reverse_lazy('index')
    login_url = 'login'
    redirect_field_name = 'redirect_to'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["produtos"] = Produto.objects.all()
        return context


class CreateProdutoView(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = 'form.html'
    fields = ['nome', 'preco', 'estoque', 'imagem']
    success_url = reverse_lazy('index')
    login_url = 'login'
    redirect_field_name = 'redirect_to'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["titulo"] = 'Criando Produto'
        context["botao"] = 'Criar Produto'
        context["corbtn"] = 'success'
        return context
    

class CreateVendaView(LoginRequiredMixin, CreateView):
    model = Venda
    template_name = 'form.html'
    fields = ['produto', 'cliente', 'quantidade_vendida']
    success_url = reverse_lazy('index')
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):

        response = super().form_valid(form)

        produto_vendido = form.cleaned_data['produto']
        quantidade_vendida = form.cleaned_data['quantidade_vendida']

        produto_vendido.estoque -= quantidade_vendida
        produto_vendido.save()

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Registrando Venda'
        context["botao"] = 'Registrar Venda'
        context["corbtn"] = 'success'
        return context


class UpdateVendaView(LoginRequiredMixin, UpdateView):
    model = Venda
    fields = ['produto', 'cliente', 'quantidade_vendida']
    template_name = 'form.html'
    success_url = reverse_lazy('index')
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Editando Venda'
        context["botao"] = 'Editar Venda'
        context["corbtn"] = 'primary'
        return context

class UpdateProdutoView(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ['nome', 'preco', 'estoque', 'imagem']
    template_name = 'form.html'
    success_url = reverse_lazy('index')
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Editando Produto'
        context["botao"] = 'Editar Produto'
        context["corbtn"] = 'primary'
        return context


class DeleteVendaView(LoginRequiredMixin, DeleteView):
    model = Venda
    success_url = reverse_lazy('index')
    template_name = 'delete.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'

class DeleteProdutoView(LoginRequiredMixin, DeleteView):
    model = Produto
    success_url = reverse_lazy('index')
    template_name = 'delete.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'


# API 
class ProdutoModelViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutosSerializer

class VendaModelViewSet(ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendasSerializer