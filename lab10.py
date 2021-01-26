matriz = []
lista_palavras = []

def horizontal(mat, palavra):
    ocorrencias = 0
    palavra = list(palavra)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            letras_encontradas = 0
            for k in range(len(palavra)):
                if (j+k) < (len(mat[i])):
                    if mat[i][j+k].lower() == palavra[k] or mat[i][j+k] == '*':
                        letras_encontradas += 1
            if len(palavra) == letras_encontradas:
                ocorrencias += 1
                for indice in range(len(palavra)):
                    mat[i][indice+j] = mat[i][indice+j].upper()
    return ocorrencias

def vertical(mat, palavra):
    ocorrencias = 0
    palavra = list(palavra)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            letras_encontradas = 0
            for k in range(len(palavra)):
                if (i+k) < (len(mat)):
                    if mat[i+k][j].lower() == palavra[k] or mat[i+k][j] == '*':
                        letras_encontradas += 1
                    else:
                        break
                else:
                    break
            if len(palavra) == letras_encontradas:
                ocorrencias += 1
                for indice in range(len(palavra)):
                    mat[indice+i][j] = mat[indice+i][j].upper()
    return ocorrencias

def diagonal_sup(mat, palavra):
    ocorrencias = 0
    palavra = list(palavra)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            letras_encontradas = 0
            for k in range(len(palavra)):
                if (i+k) < (len(mat)) and (j+k) < (len(mat[i])):
                    if mat[i+k][j+k].lower() == palavra[k] or mat[i+k][j+k] == '*':
                        letras_encontradas += 1
                    else: 
                        break
                else:
                    break
            if len(palavra) == letras_encontradas:
                ocorrencias += 1
                for indice in range(len(palavra)):
                    mat[indice+i][indice+j] = mat[indice+i][indice+j].upper()
    return ocorrencias

def diagonal_inf(mat, palavra):
    ocorrencias = 0
    palavra = list(palavra)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            letras_encontradas = 0
            for k in range(len(palavra)):
                if (i-k) < (len(mat)) and (j+k) < (len(mat[i])):
                    if mat[i-k][j+k].lower() == palavra[k] or mat[i-k][j+k] == '*':
                        letras_encontradas += 1
                    else:
                        break
                else:
                    break
            if len(palavra) == letras_encontradas:
                ocorrencias += 1
                for indice in range(len(palavra)):
                    mat[i-indice][j+indice] = mat[i-indice][j+indice].upper()
    return ocorrencias

while True:
    linha = input()
    if linha.isdigit() == False:
        matriz.append(linha.split())
    else:
        n = int(linha)
        break

for i in range(n):
    palavra = input()
    lista_palavras.append(palavra)

print("-" * 40)
print("Lista de Palavras")
print("-" * 40)

for palavra in lista_palavras:
    horiz = horizontal(matriz, palavra)
    vert = vertical(matriz, palavra)
    diag1 = diagonal_sup(matriz, palavra)
    diag2 = diagonal_inf(matriz, palavra)
    print("Palavra:", palavra)
    print("Ocorrencias:", horiz + vert + diag1 + diag2)
    print("-" * 40)

for linha in matriz:
  print(" ".join(linha))