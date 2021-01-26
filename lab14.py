def busca_palavra(matriz, linha, coluna, palavra):
  if len(palavra) == 0:
    return True
  for i in range(-1,2,1):
    for j in range(-1,2,1):
      if (linha + i < len(matriz)) and (coluna + j < len(matriz[0])) and linha + i >= 0 and coluna + j >= 0:
        if matriz[linha+i][coluna+j] == palavra[0]:
          if busca_palavra(matriz, linha + i, coluna + j, palavra[1:]) == True:
            return True
  return False

matriz = []
palavras = []

while True:
  aux = input()
  if aux.isdigit() == False:
    matriz.append(aux.split())
  else:
    n = int(aux)
    break

for i in range(n):
  palavras.append(input())

print(40 * "-")
print("Lista de Palavras")
print(40 * "-")

palavras.sort()
for palavra in palavras:
  posicoes = []
  for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
      if matriz[linha][coluna] == palavra[0]:
        if busca_palavra(matriz, linha, coluna, palavra[1:]) == True:
          posicoes.append((linha + 1,coluna + 1))
  
  print("Palavra:", palavra)
  print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in posicoes])).strip())
  print(40 * "-")