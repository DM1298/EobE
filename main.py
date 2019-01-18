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
<<<<<<< HEAD
    input()
    personaje=Personaje.crear_personaje()
    mapa=Personaje.inserta_personaje(personaje,mapa)
    Mapa.imprime_mapa()
=======
    inventario_de_pega = ["Llibertat","Presos","Politics"]
    Menuses.menu_inventario(inventario_de_pega, mapa)
>>>>>>> 4f7332e5ec999eed1bbcf654d3dc0f74742bc475
else:
    print('Salir')
