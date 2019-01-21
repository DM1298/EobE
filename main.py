import Menuses
import Mapa
import Personaje
import os
import Juega

i = Menuses.menuses(0)
if i == 0:
    path='./partida/mapa1.txt'
    mapa=Mapa.genera_mapa(path)
    Mapa.imprime_mapa(mapa)
    person=Personaje.crear_personaje()
    pj_insertado=True
    while(pj_insertado):
        mapa,pj_insertado=Personaje.inserta_personaje(person,mapa)
        if pj_insertado:
            new_x=input('Inidica posicion del personaje x:')
            new_y=input('Inidica posicion del personaje y:')
            new_x=int(new_x)
            new_y=int(new_y)
            Personaje.modifica_posicion(person,new_x,new_y)
    Juega.jugar(mapa,person)
    os.system('clear')
    print('GG WP')

elif i == 1:
    os.system('clear')
    partida='./partida/mapa1.txt'
    mapa=Mapa.genera_mapa(partida)
    Mapa.imprime_mapa(mapa)
    personaje=Personaje.crear_personaje()
    mapa=Personaje.inserta_personaje(personaje,mapa)
else:
    print('Salir')
