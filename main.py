import funcoes
jogadas = ['', 'Pedra', 'Papel' , 'Tesoura']
funcoes.formatacao('Pedra  Papel  Tesoura')
print('Pedra Papel Tesoura')

# escolha do jogador
while True:
    jogador = int(input('Escolha: '))
    if jogador == 1 or jogador == 2 or jogador == 3:
        break
    else:
        print('ERRO! digite uma opção valida')

    