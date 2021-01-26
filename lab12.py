def imprime_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(x) for x in imagem[i]))

def mediana(lista):
    lista_ordenada = sorted(lista)
    elemento_central = len(lista_ordenada) // 2
    if len(lista) % 2 == 1:
        return lista_ordenada[elemento_central]
    else:
        return (lista_ordenada[elemento_central-1] + lista_ordenada[elemento_central]) // 2

def filtro_negativo(imagem):
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            imagem[i][j] = (255 - int(imagem[i][j]))
    return imagem

def filtro_mediana(imagem):
    copia = [[i for i in j] for j in imagem]
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            lista = [imagem[i][j]]
            if i != 0 and j != 0:
                lista.append(imagem[i-1][j-1])
            if i != 0:
                lista.append(imagem[i-1][j])
            if i != 0 and j != (len(imagem[0])-1):
                lista.append(imagem[i-1][j+1])
            if j != 0:
                lista.append(imagem[i][j-1])
            if j != (len(imagem[0])-1):
                lista.append(imagem[i][j+1])
            if i != (len(imagem)-1) and j != 0:
                lista.append(imagem[i+1][j-1])
            if i != (len(imagem)-1):
                lista.append(imagem[i+1][j])
            if i != (len(imagem)-1) and j != (len(imagem[0])-1):
                lista.append(imagem[i+1][j+1])
            copia[i][j] = mediana(lista)
    return copia

def convolucao(imagem, M, D):
    copia = []
    for i in range(1, len(imagem)-1):
        copia.append([])
        for j in range(1, len(imagem[0])-1):
            l1 = 0
            l2 = 0
            l3 = 0
            if i != 0 and j != 0 and j != (len(imagem[0])-1):
                l1 = (M[0][0] * imagem[i-1][j-1]) + (M[0][1] * imagem[i-1][j]) + (M[0][2] * imagem[i-1][j+1])
            if j != 0 and j != (len(imagem[0])-1):
                l2 = (M[1][0] * imagem[i][j-1]) + (M[1][1] * imagem[i][j]) + (M[1][2] * imagem[i][j+1])
            if i != 0 and i != (len(imagem)-1) and j != 0 and j != (len(imagem[0])-1):
                l3 = (M[2][0] * imagem[i+1][j-1]) + (M[2][1] * imagem[i+1][j]) + (M[2][2] * imagem[i+1][j+1])
            if ((l1 + l2 + l3) // D) < 0:
                matriz = 0
            elif ((l1 + l2 + l3) // D) > 255:
                matriz = 255
            else:
                matriz = (l1 + l2 + l3) // D
            copia[i-1].append(matriz)
            
    return copia


filtro = input()
p2 = input()
m, n = [int(x) for x in input().split()]
z = input() 
imagem = []

for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem.append(linha)

if filtro == 'negativo':
    imagem = filtro_negativo(imagem)
elif filtro == 'mediana':
    imagem = filtro_mediana(imagem)
elif filtro == 'sharpen':
    imagem = convolucao(imagem, [[0, -1, 0], [-1, 5, -1], [0, -1, 0]], 1)
elif filtro == 'blur':
    imagem = convolucao(imagem, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], 9)
elif filtro == 'edge-detect':
    imagem = convolucao(imagem, [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], 1)

imprime_imagem(imagem)