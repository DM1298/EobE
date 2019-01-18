def genera_mapa(path):
    fd=open(path,'r')
    largo=fd.readline()
    largo.replace('\n','0')
    largo=int(largo)
    ancho=fd.readline()
    ancho.replace('\n','0')
    ancho=int(ancho)
    matriz=[]
    for i in range(largo):
        matriz.append(['0']*ancho)

    for i in range(0,largo):
        for j in range(0,ancho+1):
            casilla=fd.read(1)
            if casilla!='\n':
                matriz[i][j]=casilla
    for i in range(0,largo):
        for j in range(0,ancho):
            print(matriz[i][j],end='')
        print()
    fd.close()
genera_mapa("./mapa1.txt")
