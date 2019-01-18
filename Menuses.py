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

def menu_inventario(inventario, mapa):
    import Mapa
    ancho = Mapa.ancho_mapa(mapa)
    largo = Mapa.largo_mapa(mapa)
    largo -= (largo % 4 - 1)
    HUD=[]
    for i in range(largo):
        HUD.append([' ']*ancho)
    for i in range(largo):
        for j in range(ancho):
            if i % 4 == 0 or j == 0 or j == ancho-1:
                HUD[i][j] = '#'
    for i in range(len(inventario)):
        for j in range(len(inventario[i])):
            HUD[i*4 + 2][j + 4] = inventario[i][j]
    i = 0
    seleccionado = False
    while not seleccionado:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        for j in range(len(inventario)):
            if i == j:
                HUD[i*2 + 2][2] = '>'
            else:
                HUD[i*2 + 2][2] = ' '
        for j in range(largo):
            for k in range(ancho):
                print(HUD[j][k], end="")
            print()
        print('Selecciona un item de tu inventario con las flechas y el intro')
        x = getch()
        if x == 'A' and i > 0:
            i = i - 1
        elif x == 'A':
            i = len(inventario) - 1
        elif x == 'B' and i < len(inventario) - 1:
            i = i + 1
        elif x == 'B':
            i = 0
        elif x == '\n':
            seleccionado = True
    return i

def menuses(numero):
    lista = selecciona_lista(numero)
    rango = len(lista)
    i = 0
    seleccionado = False
    while not seleccionado:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        print(lista[rango-1])
        for j in range(0, rango-1):
            if i == j:
                print('> ', end="")
            else:
                print('  ', end="")
            print(lista[j])
        print('\nUsa las flechas para elejir, y el intro para seleccionar', end='')
        x = getch()
        if x == 'A' and i > 0:
            i = i - 1
        elif x == 'A':
            i = rango - 2
        elif x == 'B' and i < rango - 2:
            i = i + 1
        elif x == 'B':
            i = 0
        elif x == '\n':
            seleccionado = True
    return i

def selecciona_lista(numero):
    if numero == 0: #Menu Principal
        return ["Juego Nuevo", "Cargar Juego", "Salir", "***Eat or be Eaten***"]
    if numero == 1: #Menu de 'Esc'
        return ["Volver", "Guardar", "Salir"]
