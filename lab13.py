def bubleSort(matriz, aux):
  j = aux
  for a in range(len(matriz)):
    for i in range(len(matriz)):
      if (i+1) < len(matriz):
        if matriz[i][j] > matriz[i+1][j]:
          matriz[i], matriz[i+1] = matriz[i+1], matriz[i]
  return matriz


n = int(input())
dados = []

cabecalho = input().split(',')

for i in range(n):
  aux = input().split(',')
  linha = []
  for j in range(len(aux)):
    if j == 0:
      linha.append(aux[j])
    else:
      linha.append(int(aux[j]))
  dados.append(linha)

prioridade = input().split()
for i in range(len(prioridade)):
  aux = len(prioridade)-i-1
  a = cabecalho.index(prioridade[aux])
  dados = bubleSort(dados, a)

dados.insert(0, cabecalho)

for linha in dados:
  print('{:15s}'.format(linha[0]), ''.join('{:>10}'.format(item) for item in linha[1:]))