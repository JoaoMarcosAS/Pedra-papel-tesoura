import funcoes
from random import randint

jogadas = ['', 'Pedra', 'Papel' , 'Tesoura']
pontos = perdeu = partidas = empate= 0

# escolha do jogador
while True:
    while True:
        funcoes.formatacao('Pedra[1]  Papel[2]  Tesoura[3]')
        
        try:
            jogador = int(input('Escolha: '))
            if jogador == 1 or jogador == 2 or jogador == 3:
                break
            else:
                print('ERRO! digite uma opção valida!')
        except:
            print('ERRO! digite uma opção valida!')

    maquina = randint(1, 3)

    maquinaesco = jogadas[maquina]
    jogadoresco = jogadas[jogador]

    print(f'O jogado escolheu {jogadoresco} e a maquinha escolheu {maquinaesco}.')
    print('O jogador', end=' ')

    # sistema de pontuação
    if jogador == maquina: 
        print('Empate!')
        empate += 1
    elif jogador == 2 and maquina == 1:
        print('Ganhou, Ponto!')
        pontos +=1
    elif jogador == 1 and maquina == 3:
        print('Ganhou, Ponto!')
        pontos += 1
    elif jogador == 3 and maquina == 2:
        print('Ganhou, Ponto!')
        pontos += 1
    else:
        print('Perdeu!')
        perdeu += 1
    partidas += 1
    
    while True:
        try:
                continuar = input('Quer continuar? [S/N] ')
                if continuar[0].strip().upper() not in 'SN':
                    print('ERRO! digite uma opção valida!')
                else:
                    break
        except:
            print('ERRO! digite a opção valida!')

    if continuar[0].strip().upper() == 'N':
        break

funcoes.formatacao('Placar de pontuação')
print(f'O jogador conseguiu {pontos} pontos')
print(f'O jogador perdeu {perdeu} vezes')
print(f'O jogador empatou {empate} vezes')
print(f'O jogador jogou {partidas} vezes')
