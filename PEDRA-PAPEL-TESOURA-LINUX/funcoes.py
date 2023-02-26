from pynput.keyboard import Key
import os


# função utilazada para a formatação de título.
def formatacao(formatar):
     print('-=' * 15)
     print(f'{formatar}'.center(30))
     print('-=' * 15)
 

# função utilizado para identificar se o botão ENTER foi pressionado.
def pressione_enter(key):
     if key == Key.enter:
          os.system('clear') or None
          return False
          