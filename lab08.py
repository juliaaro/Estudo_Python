l = int(input())
lista = []
pontuacao = ['.',',','?','!']

for i in range(0,l):
  linhas = input().lower()
  lista.append(linhas)

n = int(input())
lista_palavras =[]

for i in range(0,n):
  palavra = input()
  lista_palavras.append(palavra)


texto = ' '.join(lista)
for p in pontuacao:
  texto = texto.replace(p, '')
lista_texto = texto.split()


for busca in lista_palavras:
  similares = 0
  ocorrencia = 0
  for palavra in lista_texto:
    if busca.lower() in palavra and palavra != busca.lower():
      similares += 1
    if busca.lower() == palavra:
      ocorrencia += 1
  
  print("Palavra buscada:", busca)
  print("Ocorrencia:", ocorrencia)
  print("Palavras similares:", similares)
