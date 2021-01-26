n = int(input())
notas = []
pesos = []
for i in range(0,n):
  notas.append(float(input()))

for i in range(0,n):
  pesos.append(int(input()))

a = []
for i in range(len(notas)):
  produto = (notas[i]*pesos[i]) 
  a.append(produto)

media = sum(a) / sum(pesos)

nota_final = 0

if (media >= 5.0) or (media < 2.5):
  nota_final = media
  print('Media laboratorios:', format(media, ".1f").replace(".", ","))
  if media >= 5.0:
    print('Situacao: Aprovado por nota')
  if media < 2.5:
    print('Situacao: Reprovado por nota')
  print('Nota final:', format(nota_final, ".1f").replace(".", ","))

if (media < 5.0) and (media > 2.5):
  m = int(input())
  notas_exame = []
  produtos_exame = []
  pesos_exame = []
  for i in range(0,m):
    x = int(input())
    pesos_exame.append(pesos[x-1])
  for i in range(0,m):
    notas_exame.append(float(input()))
  for i in range(len(notas_exame)):
    produtos_exame.append(pesos_exame[i] * notas_exame[i])

  media_exame = sum(produtos_exame) / sum(pesos_exame)
  nota_final = min(5,(media + media_exame)/2)

  print('Media laboratorios:', format(media, ".1f").replace(".", ","))
  if nota_final >= 5.0:
    print('Situacao: Aprovado no exame')
  if nota_final < 5.0:
    print('Situacao: Reprovado no exame')
  print('Nota final:', format(nota_final, ".1f").replace(".", ","))