
import funcoes
import os
from random import randint
from time import sleep
from pynput.keyboard import Key, Listener

os.system('clear') or None
jogadas = ['', 'Pedra', 'Papel' , 'Tesoura']
pontos = perdeu = partidas = empate= 0
pontos_lista = list()

funcoes.formatacao('Pedra  Papel Tesoura')
nome = input('Por favor digite o seu nome: ')

while True:
    while True:
        funcoes.formatacao('Pedra[1]  Papel[2]  Tesoura[3]')

        try:
            jogador = int(input('Escolha: '))
            if jogador == 1 or jogador == 2 or jogador == 3:
                break
        except:
            os.system('clear') or None
            print('ERRO! digite uma opção valida!')
             
    maquina = randint(1, 3)

    maquinaesco = jogadas[maquina]
    jogadoresco = jogadas[jogador]
    
    print('Pedra...', flush=True,end='  ')
    sleep(0.5)
    print('Papel...', flush=True, end='  ')
    sleep(0.5)
    print('Tesoura...', flush=True)
    sleep(0.5)

    print(f'O jogador escolheu {jogadoresco} e a maquinha escolheu {maquinaesco}.')
    print('O jogador', end=' ')

    # sistema de pontuação
    if jogador == maquina: 
        print('Empatol!')
        empate += 1
    elif jogador == 2 and maquina == 1:
        print('Ganhou, Pon == 1 or jogador == 2 or jogador == 3to!')
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
    
    print('Pressione ENTER para continuar!')
    with Listener(on_press = funcoes.pressione_enter) as listener:
        listener.join()

    while True:
        try:
            os.system('clear') or None
            continuar = input('Quer continuar? [S/N] ')
            if continuar[0].strip().upper() not in 'SN' or continuar in '1234567890':
                print('ERRO! digite uma opção valida!')
            else:
                break
        except:
            os.system('clear') or None
            print('ERRO! digite a opção valida!')

    if continuar[0].strip().upper() == 'N':
        break
    
    os.system('clear') or None

os.system('clear') or None

funcoes.formatacao('Placar de pontuação')
print(f'O jogador conseguiu {pontos} pontos')
print(f'O jogador perdeu {perdeu} vezes')
print(f'O jogador empatou {empate} vezes')
print(f'O jogador jogou {partidas} vezes')
