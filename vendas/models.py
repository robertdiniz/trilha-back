from django.db import models

class Produto(models.Model):
    nome = models.CharField("Nome do Produto", max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    estoque = models.IntegerField(default=0)
    imagem = models.ImageField("Imagem", upload_to="images/")

    def __str__(self) -> str:
        return f'{self.nome} - {self.preco}'
    
class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.CharField("Cliente", max_length=100)
    quantidade_vendida = models.IntegerField()
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.cliente} - {self.produto.nome} - {self.data_venda.strftime("%d/%m/%Y")}'
