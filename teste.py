pontosA = list()
pontosB = list()
contadorB = 0

while True:
    
    pontuação = input('precione [A/B] (n para parar): ')

    if pontuação == 'a':
        pontosA.append('a')
    elif pontuação == 'b':
        contadorB += 1
        pontosB.append(contadorB)
    elif pontuação == 'n':
        break
    
with open('pontos.txt', 'a') as arquivo:
    pripontos = arquivo.write(str(pontosA))
with open('pontos.txt', 'a') as arquivo:
    segpontos = arquivo.write(f'\n{str(pontosB)}')
    
