selecoes = []
dic = {}
campeao = None

for i in range(16):
  selecao = input()
  selecoes.append(selecao)
  dic[selecao] = {"partidas": 0,
                  "vitorias": 0,
                  "derrotas": 0,
                  "penaltis": 0,
                  "normal": 0,
                  "marcados": 0,
                  "sofridos": 0}

partidas = []
for i in range(16):
  p = input()
  lista_partida = p.replace('(','').replace(')','').split()
  partidas.append(lista_partida)

for selecao in selecoes:
  for partida in partidas:
    if selecao in partida:
      if partida[1] != partida[3]: # nao teve penalti
        if selecao == partida[0]: # time do lado esquerdo
          dic[selecao]['partidas'] += 1
          dic[selecao]['normal'] += 1
          dic[selecao]['marcados'] += int(partida[1])
          dic[selecao]['sofridos'] += int(partida[3])
          if partida[1] > partida[3]:
            dic[selecao]['vitorias'] += 1
          else:
            dic[selecao]['derrotas'] += 1
        else: # time do lado direito
          dic[selecao]['partidas'] += 1
          dic[selecao]['normal'] += 1
          dic[selecao]['marcados'] += int(partida[3])
          dic[selecao]['sofridos'] += int(partida[1])
          if partida[3] > partida[1]:
            dic[selecao]['vitorias'] += 1
          else:
            dic[selecao]['derrotas'] += 1
      else: # com penalti 
        if selecao == partida[0]: # time lado esquerdo
          dic[selecao]['partidas'] += 1
          dic[selecao]['penaltis'] += 1
          dic[selecao]['marcados'] += int(partida[1])
          dic[selecao]['sofridos'] += int(partida[3])
          if partida[4] > partida[6]:
            dic[selecao]['vitorias'] += 1
          else:
            dic[selecao]['derrotas'] += 1
        else: # time lado direito
          dic[selecao]['partidas'] += 1
          dic[selecao]['penaltis'] += 1
          dic[selecao]['marcados'] += int(partida[3])
          dic[selecao]['sofridos'] += int(partida[1])
          if partida[6] > partida[4]:
            dic[selecao]['vitorias'] += 1
          else:
            dic[selecao]['derrotas'] += 1

  if dic[selecao]['vitorias'] == 4:
    campeao = selecao

for selecao in selecoes:
  print("-" * 50)
  print("Pais:", selecao)
  print("Partidas:", dic[selecao]["partidas"])
  print("Partidas decididas em tempo normal de jogo:", dic[selecao]["normal"])
  print("Partidas decicidas nos penaltis:", dic[selecao]["penaltis"])
  print("Vitorias:", dic[selecao]["vitorias"])
  print("Derrotas:", dic[selecao]["derrotas"])
  print("Gols marcados:", dic[selecao]["marcados"])
  print("Gols sofridos:", dic[selecao]["sofridos"])
  
print("-" * 50)
print("Pais campeao:", campeao)
print("-" * 50)