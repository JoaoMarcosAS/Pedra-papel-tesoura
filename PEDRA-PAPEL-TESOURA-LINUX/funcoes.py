from pynput.keyboard import Key, Listener

import os

def formatacao(formatar):
     print('-=' * 15)
     print(f'{formatar}'.center(30))
     print('-=' * 15)
 

def pressione_enter(key):
     if key == Key.enter:
          os.system('clear') or None
          return False
          