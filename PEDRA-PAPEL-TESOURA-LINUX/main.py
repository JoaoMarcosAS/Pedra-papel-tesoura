import funcoes
import os
from random import randint
from time import sleep
from pynput.keyboard import Listener

#função para limpar o terminal
os.system('clear') or None

jogadas = ['', 'Pedra', 'Papel' , 'Tesoura']
pontos = perdeu = partidas = empate = 0

# jogo pedra papel tesoura
while True:
    
    #sistema de escolha de pedra, papel ou tesoura do jogador
    while True:
        funcoes.formatacao('Pedra[1]  Papel[2]  Tesoura[3]')

        try:
            jogador = int(input('Escolha: '))
            if jogador == 1 or jogador == 2 or jogador == 3:
                break
        except:
            os.system('clear') or None
            print('ERRO! digite uma opção válida!')


    
    print('Pedra...', flush=True,end='  ')
    sleep(0.5)
    print('Papel...', flush=True, end='  ')
    sleep(0.5)
    print('Tesoura...', flush=True)
    sleep(0.5)

    print(f'O jogador escolheu {jogadoresco} e a maquinha escolheu {computadoresco}.')
    print('O jogador', end=' ')
       
    # sistema de escolha de pedra,papel ou tesoura do computador   
    computador = randint(1, 3)

    computadoresco = jogadas[computador]
    jogadoresco = jogadas[jogador]

    # sistema de pontuação
    if jogador == computador: 
        print('Empatol!')
        empate += 1
    elif jogador == 2 and computador == 1:
        print('Ganhou, Pon == 1 or jogador == 2 or jogador == 3to!')
        pontos +=1
    elif jogador == 1 and computador == 3:
        print('Ganhou, Ponto!')
        pontos += 1
    elif jogador == 3 and computador == 2:
        print('Ganhou, Ponto!')
        pontos += 1
    else:
        print('Perdeu!')
        perdeu += 1
    partidas += 1
    
    # sistema de pressionar ENTER para continuar
    print('Pressione ENTER para continuar!')
    with Listener(on_press = funcoes.pressione_enter) as listener:
        listener.join()

    # sistema de escolha de não continuar ou continuar o jogo pedra papel tesoura 
    while True:
        try:
            os.system('clear') or None
            continuar = input('Quer continuar? [S/N] ')
            if continuar[0].strip().upper() not in 'SN' or continuar in '1234567890':
                print('ERRO! digite uma opção válida!')
            else:
                break
        except:
            os.system('clear') or None
            print('ERRO! digite uma opção válida!')
    
    if continuar[0].strip().upper() == 'N':
        break
    
    #sistema para limapar tela
    os.system('clear') or None

#sistema para limapar tela
os.system('clear') or None

# Placar de pontuação
funcoes.formatacao('Placar de pontuação')

print(f'O jogador conseguiu {pontos} pontos')
print(f'O jogador perdeu {perdeu} vezes')
print(f'O jogador empatou {empate} vezes')
print(f'O jogador jogou {partidas} vezes')
     