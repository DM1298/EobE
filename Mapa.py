def genera_cofre(n_cofre,path_cofre):
    path_cofre=path_cofre+n_cofre+'.txt'
    items=[]
    fd_cofre=open(path)
    n_items=fd_cofre.readline()
    n_items.replace('\n','0')
    n_items=int(n_items)
    for i in range(0,n_items):
        item=fd_cofre.readline()
        item=item[:-1]
        items.append(item)
    return items

#Genera/añade los atributos de la casilla segun la 'letra' pasada por parametro
#n_cofre lleva el conteo de los cofres del mapa
def genera_casilla(letra,n_cofre,path_cofre):
    if letra=='#':      #MURO
        casilla= {
            'c' : letra,
            'pisable': False
        }
    elif letra==' ':    #AIRE
        casilla= {
            'c': letra,
            'pisable': True
        }
    elif letra=='E':    #ENEMIGO
        casilla= {
            'c': letra,
            'pisable': False
        }
    elif letra=='C':    #COFRE
        casilla= {
            'c': letra,
            'pisable': False,
            'n_cofre': n_cofre,
            'contenido': genera_cofre(n_cofre,path_cofre)
        }

    return casilla

#Genera la matriz del mapa a partir de archivo txt
def genera_mapa(path):
    fd=open(path,'r')
    largo=fd.readline()
    largo.replace('\n','0')
    largo=int(largo)
    ancho=fd.readline()
    ancho.replace('\n','0')
    ancho=int(ancho)
    matriz=[]
    n_cofre=0
    for i in range(largo):
        matriz.append([0]*ancho)
    for i in range(0,largo):
        for j in range(0,ancho+1):
            casilla=fd.read(1)
            if casilla!='\n':
                s_casilla=genera_casilla(casilla,n_cofre,path+'/cofres')
                if casilla == 'C':
                    n_cofre += 1
                matriz[i][j]=s_casilla
    fd.close()
    return matriz

def ancho_mapa(mapa):
    return len(mapa[0])

def largo_mapa(mapa):
    return len(mapa)

def imprime_mapa(mapa):
    ancho=ancho_mapa(mapa)
    largo=largo_mapa(mapa)
    for i in range(0,largo):
        for j in range(0,ancho):
            print(mapa[i][j]['c'],end='')
        print()

def comprueba_casilla(mapa,x,y):
    return mapa[x][y].get('pisable')
