"""
Semana 2 — O carrinho de compras (Orientação a Objetos: composição)

Complete os trechos marcados com TODO.
Não altere os nomes da classe e dos métodos: a correção é automática.
"""

from produtos import ALIQUOTA_PADRAO, Produto


class Carrinho:
    """Guarda produtos e suas quantidades."""

    def __init__(self):
        self._itens = {}

    def adicionar(self, produto: Produto, quantidade: int = 1) -> None:
        """
        - TypeError se produto não for instância de Produto
        - ValueError se quantidade não for inteiro >= 1
        - Se já existir produto com o mesmo nome, soma a quantidade
        """
        if not isinstance(produto, Produto):
            raise TypeError("produto deve ser um Produto.")

        if type(quantidade) is not int:
            raise ValueError("quantidade deve ser um número inteiro.")

        if quantidade < 1:
            raise ValueError("quantidade deve ser 1 ou mais.")

        nome = produto.nome

        if nome in self._itens:
            self._itens[nome][1] = self._itens[nome][1] + quantidade
        else:
            self._itens[nome] = [produto, quantidade]

    def remover(self, nome: str) -> None:
        """Remove o produto inteiro. KeyError se não existir."""
        if nome not in self._itens:
            raise KeyError(nome)

        del self._itens[nome]

    def subtotal(self) -> float:
        """Soma de preco * quantidade (sem impostos)."""
        soma = 0

        for item in self._itens.values():
            produto = item[0]
            quantidade = item[1]
            soma = soma + produto.preco * quantidade

        return round(soma, 2)

    def total_impostos(self) -> float:
        """Soma de produto.imposto() * quantidade."""
        soma = 0

        for item in self._itens.values():
            produto = item[0]
            quantidade = item[1]
            soma = soma + produto.imposto() * quantidade

        return round(soma, 2)

    def total(self) -> float:
        """subtotal() + total_impostos()"""
        return round(self.subtotal() + self.total_impostos(), 2)

    def economia(self) -> float:
        """
        Quanto o consumidor pagaria A MAIS se todos os produtos
        tivessem a alíquota padrão:
            soma de round(preco * ALIQUOTA_PADRAO, 2) * quantidade
            menos total_impostos()
        """
        imposto_cheio = 0

        for item in self._itens.values():
            produto = item[0]
            quantidade = item[1]
            imposto_de_uma_unidade = round(produto.preco * ALIQUOTA_PADRAO, 2)
            imposto_cheio = imposto_cheio + imposto_de_uma_unidade * quantidade

        return round(imposto_cheio - self.total_impostos(), 2)

    def __len__(self) -> int:
        """Total de UNIDADES no carrinho."""
        unidades = 0

        for item in self._itens.values():
            quantidade = item[1]
            unidades = unidades + quantidade

        return unidades

    def __contains__(self, nome: str) -> bool:
        """Permite: 'Arroz 5kg' in carrinho"""
        return nome in self._itens


if __name__ == "__main__":
    from produtos import ProdutoCestaBasica, ProdutoPadrao

    c = Carrinho()
    c.adicionar(ProdutoCestaBasica("Feijão 1kg", 8.00), 2)
    c.adicionar(ProdutoPadrao("Chocolate", 10.00))
    print("Total:", c.total())
    print("Economia:", c.economia())
