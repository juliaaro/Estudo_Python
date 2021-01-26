import copy
def existe_caminho(tabuleiro, a, b, c, d):
  aux = tabuleiro[a][b]
  tabuleiro[a][b] = 0
  if a == c and b == d:
    return True
  if aux == 0:
    return False
  if (a + aux) < len(tabuleiro):
    if existe_caminho(tabuleiro, a + aux, b, c, d) == True:
      return True
  if (b + aux) < len(tabuleiro[0]):
    if existe_caminho(tabuleiro, a, b + aux, c, d) == True:
      return True
  if (a - aux) >= 0:
    if existe_caminho(tabuleiro, a - aux, b, c, d) == True:
      return True
  if (b - aux) >= 0:
    if existe_caminho(tabuleiro, a, b - aux, c, d) == True:
      return True
  return False


n, m = [int(i) for i in input().split()]
tabuleiro = []
for i in range(n):
  tabuleiro.append([int(i) for i in input().split()])
a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]

tabuleiro2 = copy.deepcopy(tabuleiro)

if existe_caminho(tabuleiro, a, b, c, d) == True:
  caminho_1 = 'existe caminho'
else:
  caminho_1 = 'nao existe caminho'
if existe_caminho(tabuleiro2, c, d, a, b) == True:
  caminho_2 = 'existe caminho'
else:
  caminho_2 = 'nao existe caminho'

print("({},{}) -> ({},{}):".format(a,b,c,d), caminho_1)
print("({},{}) -> ({},{}):".format(c,d,a,b), caminho_2)