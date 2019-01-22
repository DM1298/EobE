import Mapa
import Personaje
import os
import Menuses
import getch

def jugar(mapa,personaje):
    test=True
    while test:
        Mapa.imprime_mapa(mapa)
        move=getch.getch()
        x=personaje.get('pos_x')
        y=personaje.get('pos_y')
        x_bak=x
        y_bak=y
        if move == 'A':
            x -= 1
        elif move == 'B':
            x += 1
        elif move == 'C':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == str(chr(27)):
            i = Menuses.menuses(1)
            if i == 2:
                test = False
        if Mapa.comprueba_casilla(mapa,x,y):
            Personaje.modifica_posicion(personaje,x,y)
            mapa, error=Personaje.inserta_personaje(personaje,mapa) #en vez de retornar error, yo haria que se ocupara de eso esta funcion
            if not error:
                aire=Mapa.genera_casilla(' ',0,0)
                mapa[x_bak][y_bak]=aire
