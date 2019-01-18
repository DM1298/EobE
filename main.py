import Menuses
import Mapa

i = Menuses.menuses(0)
if i == 0:
    print('NewGame()')
elif i == 1:
    partida='./partida/mapa1.txt'
    mapa=Mapa.genera_mapa(partida)
    Mapa.imprime_mapa(mapa)
    inventario_de_pega = ["Llibertat","Presos","Politics"]
    Menuses.menu_inventario(inventario_de_pega, mapa)
else:
    print('Salir')
