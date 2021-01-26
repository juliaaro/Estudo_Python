def verifica_jogo(tabuleiro, alt_tab, larg_tab, alt_peca, larg_peca, peca):
    for i in range(alt_tab):
        for j in range(larg_tab):
            elem = 0
            for k in range(alt_peca):
                for l in range(larg_peca):
                    if (i+k) < alt_tab and (j+l) < larg_tab:
                        if tabuleiro[i+k][j+l] == '*' and peca[k][l] == '#':
                            break
                        if tabuleiro[i+k][j+l] == '.':
                            elem += 1
                        if tabuleiro[i+k][j+l] == '*' and peca[k][l] == '.':
                            elem += 1
            if elem == (alt_peca * larg_peca):
                for k in range(alt_peca):
                    for l in range(larg_peca):
                        if tabuleiro[i+k][j+l] == '.':
                            tabuleiro[i+k][j+l] = '#'
                status_do_jogo = 'O jogo deve continuar'
                return tabuleiro, status_do_jogo
    status_do_jogo = 'Fim de jogo'
    return tabuleiro, status_do_jogo

n_tab = input().split()
alt_tab = int(n_tab[0])
larg_tab = int(n_tab[1])

tabuleiro = []

for i in range(alt_tab):
    linha = list(input())
    tabuleiro.append(linha)

n_peca = input().split()
alt_peca = int(n_peca[0])
larg_peca = int(n_peca[1])

peca = []

for aux in range(alt_peca):
    aux = list(input())
    peca.append(aux)

tabuleiro, status_do_jogo = verifica_jogo(tabuleiro, alt_tab, larg_tab, alt_peca, larg_peca, peca)

for linha in tabuleiro:
    print(''.join(linha))

print(status_do_jogo)