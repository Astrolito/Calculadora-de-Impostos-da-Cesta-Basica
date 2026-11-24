"""
Semana 3 — Reescrevendo com estilo funcional

Aqui não existe carrinho guardando coisas. Cada item é uma tupla
que não muda, e cada função recebe a lista de itens e devolve uma resposta.
"""

from collections import namedtuple

ALIQUOTA_PADRAO = 0.25
ALIQUOTAS = {"cesta_basica": 0.0, "reduzido": 0.10, "padrao": 0.25}

Item = namedtuple("Item", ["nome", "preco", "categoria", "quantidade"], defaults=[1])


def aliquota(categoria):
    """Devolve a alíquota da categoria. ValueError se a categoria não existir."""
    if categoria not in ALIQUOTAS:
        raise ValueError("Categoria desconhecida: " + str(categoria))

    return ALIQUOTAS[categoria]


def imposto_item(item):
    """Imposto do item: round(round(preco * alíquota, 2) * quantidade, 2)."""
    imposto_de_uma_unidade = round(item.preco * aliquota(item.categoria), 2)
    return round(imposto_de_uma_unidade * item.quantidade, 2)


def total_impostos(itens):
    """Soma dos impostos de todos os itens."""
    impostos = map(imposto_item, itens)
    return round(sum(impostos), 2)


def valor_sem_imposto(item):
    """Preço * quantidade de um item."""
    return item.preco * item.quantidade


def total_compra(itens):
    """Soma de preço * quantidade, mais os impostos."""
    valores = map(valor_sem_imposto, itens)
    return round(sum(valores) + total_impostos(itens), 2)


def filtrar_por_categoria(itens, categoria):
    """Lista nova, só com os itens da categoria."""
    return list(filter(lambda item: item.categoria == categoria, itens))


def ordenar_por_preco(itens, decrescente=False):
    """Lista nova, ordenada pelo preço de uma unidade."""
    return sorted(itens, key=lambda item: item.preco, reverse=decrescente)


def imposto_cheio_item(item):
    """Imposto que o item pagaria com a alíquota padrão."""
    return round(item.preco * ALIQUOTA_PADRAO, 2) * item.quantidade


def economia_total(itens):
    """
    Quanto o consumidor pagaria a mais se tudo tivesse a alíquota padrão:
    soma do imposto cheio de cada item, menos total_impostos(itens).
    """
    impostos_cheios = map(imposto_cheio_item, itens)
    return round(sum(impostos_cheios) - total_impostos(itens), 2)


if __name__ == "__main__":
    compra = [
        Item("Feijão 1kg", 8.00, "cesta_basica", 2),
        Item("Chocolate", 10.00, "padrao"),
    ]
    print("Total:", total_compra(compra))
    print("Economia:", economia_total(compra))
