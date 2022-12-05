busca = "Venda de produtos"
lista = [(1, 'Prestação de serviço'), (2, 'Compra de produto'), (3, 'Alimentação'), (4, 'Venda de produtos')]
saida = ''

if type(busca) == int:
    for itens in lista:
        if itens[0] == busca:
            saida = itens[1]
else:
    for itens in lista:
        if itens[1] == busca:
            saida = itens[0]

print(saida)