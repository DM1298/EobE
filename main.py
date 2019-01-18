import Menuses
import Mapa

i = Menuses.menuses(0)
if i == 0:
    print('NewGame()')
elif i == 1:
    partida='./partida/mapa1.txt'
    mapa=Mapa.genera_mapa(partida)
    Mapa.imprime_mapa(mapa)
else:
    print('Salir')
