from django.forms import ModelForm
from .models import Produto, Venda

class ProdutoForm(ModelForm):
    
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'imagem']

class VendaForm(ModelForm):

    class Meta:
        model = Venda
        fields = ['produto', 'cliente', 'quantidade_vendida']
    
