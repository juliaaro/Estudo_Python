lista = list()
n = int(input())
for i in range(0,n):
    pç = float(input())
    lista.append(pç)
k = int(input())
q = float(input())

lucro = -1
for i in range(len(lista)): #compra
    a = i+k+1
    if a > n:
        a = n
    for j in range(i,a): #venda
        qntd = q // lista[i]
        lucro_1 = ((qntd * lista[j]) - (qntd * lista[i]))
        if lucro_1 > lucro:
            valor_compra = lista[i]
            valor_venda = lista[j]
            qtde_acoes = qntd
            dia_compra = i+1
            dia_venda = j+1
            lucro = lucro_1

print('Dia da compra:', dia_compra)
print('Valor de compra: R$', format(valor_compra, '.2f').replace('.', ','))
print('Dia da venda:', dia_venda)
print('Valor de venda: R$', format(valor_venda, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', int(qtde_acoes))
print('Lucro: R$', format(lucro, '.2f').replace('.', ','))
