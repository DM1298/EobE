import Mapa
import random

def crear_personaje():
    personaje={
        'c': 'O',
        'ps': 1000,
        'mana': 500,
        'inventario': []
    }
    return personaje

def inserta_personaje(personaje,mapa):
    x=Mapa.ancho_mapa(mapa)
    y=Mapa.largo_mapa(mapa)
    x-=1
    y-=1
    aire=False
    pos_x = -1
    pos_y = -1
    while aire:
        pos_x=randint(1,x)
        pos_y=randint(1,y)
        if mapa[pos_x][pos_y].get('pisable')==True:
            aire=True
    mapa[pos_x][pos_y]=personaje
    #TODO::PQ NO FUNCIONA ESTO????
    return mapa
