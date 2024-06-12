# biblioteca de automação > pyautogui
import pyautogui as auto # as > altera o nome da biblioteca de pyautohui para auto

import time
import mouseinfo # biblioteca que fornece as coordenadas xy do mouse
# mouseinfo.mouseInfo() # aplicativo que aparece as coordenadas

# define espera para cada comano auto
auto.PAUSE = 0.7


auto.press('win') # press > significa apertar uma tecla
auto.write("edge") # write > escreve
auto.press("enter")

auto.hotkey('alt', 'space') # hotkey > ombinar teclas de atalho
auto.press('x')

auto.write('github.com')
auto.press("enter")

# abre o classromm
auto.hotkey('ctrl', 't')
auto.write('classroom.google.com')
auto.press('enter')

time.sleep(1) # da biblioteca time
auto.move(10, duration=3)
auto.click(975, 469, duration=0.5)