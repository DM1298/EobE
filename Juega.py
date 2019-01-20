import Mapa
import Personaje
import os
import Menuses

def jugar(mapa,personaje):
    test=True
    while test:
        os.system('clear')
        print('Jugando...')
        Mapa.imprime_mapa(mapa)
        move=Menuses.getch()
        x=personaje.get('pos_x')
        y=personaje.get('pos_y')
        x_bak=x
        y_bak=y
        if move == 'A':
            x+=1
        elif move == 'B':
            x-=1
        elif move == 'C':
            y+=1
        elif move == 'D':
            y-=1
        if Mapa.comprueba_casilla(mapa,x,y):
            Personaje.modifica_posicion(personaje,x,y)
            mapa=Personaje.inserta_personaje(personaje,mapa)
            aire=Mapa.genera_casilla(' ',0,0)
            mapa[x_bak][y_bak]=0
            mapa[x_bak][y_bak]=aire
