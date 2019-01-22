import getch

def menu_inventario(inventario, mapa):
    import Mapa
    ancho = Mapa.ancho_mapa(mapa)
    largo = len(inventario)*2
    HUD=[]
    for i in range(largo):
        HUD.append([' ']*ancho)
    for i in range(largo):
        for j in range(ancho):
            if i % 2 == 1 or j == 0 or j == ancho-1:
                HUD[i][j] = '#'
    for i in range(len(inventario)):
        for j in range(len(inventario[i])):
            HUD[i*2][j + 4] = inventario[i][j]
    i = 0
    seleccionado = False
    while not seleccionado:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        for j in range(len(inventario)):
            if i == j:
                HUD[j*2][2] = '>'
            else:
                HUD[j*2][2] = ' '
        import Mapa
        Mapa.imprime_mapa(mapa)
        for j in range(largo):
            for k in range(ancho):
                print(HUD[j][k], end="")
            print()
        print('Selecciona un item de tu inventario con las flechas y el intro')
        x = getch.getch()
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
        x = getch.getch()
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
        return ["Volver", "Guardar", "Salir","***PAUSA***"]
