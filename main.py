def getch():
  import sys, tty, termios
  old_settings = termios.tcgetattr(0)
  new_settings = old_settings[:]
  new_settings[3] &= ~termios.ICANON
  try:
    termios.tcsetattr(0, termios.TCSANOW, new_settings)
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(0, termios.TCSANOW, old_settings)
  return ch

def menuses(numero):
    lista = selecciona_lista(numero)
    rango = len(lista)
    i = 0
    seleccionado = False
    while not seleccionado:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        for j in range(0, rango):
            if i == j:
                print('> ', end="")
            else:
                print('  ', end="")
            print(lista[j])
        print('\nUsa las flechas para elejir, y el intro para seleccionar')
        x = getch()
        print(x)
        if x == 'A' and i > 0:
            i = i - 1
        elif x == 'A':
            i = rango - 1
        elif x == 'B' and i < rango - 1:
            i = i + 1
        elif x == 'B':
            i = 0
        elif x == '\n':
            seleccionado = True
    return i

def selecciona_lista(numero):
    lista = []
    switcher = {
        0: #Menu principal
            ["Juego Nuevo", "Cargar Juego","Salir"]
    }
    lista = switcher.get(numero)
    return lista

i = 0
menuses(i)
print('Finalizado, Saliendo, Esperando, Mirando, Observando...')
