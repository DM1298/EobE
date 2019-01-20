import Mapa
import random

def crear_personaje():
    personaje={
        'c': 'O',
        'ps': 1000,
        'mana': 500,
        'inventario': [],
        'pos_x': 0,
        'pos_y': 0
    }
    return personaje

def inserta_personaje(personaje,mapa):
    x=personaje['pos_x']
    y=personaje['pos_y']
    if mapa[x][y].get('pisable')==True:
            mapa[x][y] = personaje
            error=False
    else: error=True
    return mapa,error

def modifica_posicion(personaje,x,y):
    personaje['pos_x']=x
    personaje['pos_y']=y
    return personaje
