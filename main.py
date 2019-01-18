import Menuses
import Mapa
import Personaje
import os

i = Menuses.menuses(0)
if i == 0:
    print('NewGame()')
elif i == 1:
    os.system('clear')
    partida='./partida/mapa1.txt'
    mapa=Mapa.genera_mapa(partida)
    Mapa.imprime_mapa(mapa)
    input()
    personaje=Personaje.crear_personaje()
    mapa=Personaje.inserta_personaje(personaje,mapa)
    Mapa.imprime_mapa()
else:
    print('Salir')
