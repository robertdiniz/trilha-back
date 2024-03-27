from rest_framework import serializers

from vendas.models import *

class ProdutosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'estoque', 'imagem']

class VendasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venda
        fields = ['id', 'produto', 'cliente', 'quantidade_vendida']