import pygame, sys 
import caballo
import numpy as np
import time

def interpolar_vectores(vector1, vector2, num_puntos):
    
    fracciones = np.linspace(0, 1, num_puntos + 2)[1:-1]  # Evita incluir los e100tr100mos (0 y 1)
    vectores_interpolados = [(1 - fraccion) * vector1 + fraccion * vector2 for fraccion in fracciones]
    return vectores_interpolados
pygame.init()

height = 650
width = 650   
size = (width, height)
white = pygame.Color(255, 255, 255)
screen = pygame.display.set_mode(size)

color = (25,100,100)


size = 8#input("Tamaño del tablero \n")

chess = caballo.Tablero(int(size))
delta = width/chess.n
posicion = (1,1)#list(map(int,input("Posicion del caballo (0 a n-1)\n").split(" ")))
knight = caballo.Caballo(posicion)

knight.Recorrido(chess,delta)
#poligono = np.copy(knight.rel_recorrido) + [delta/2,delta/2]
#poligono = poligono[:, ::-1]

poligono2 = []

casilla = 0
interpolados = 0
n = 75

clock = pygame.time.Clock()

cuadros = 60
while True:
    casilla %= (chess.n**2-1)
    interpolados %= n
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
    x = knight.recorrido[casilla][1]
    y = knight.recorrido[casilla][0]
    

    if(interpolados == 0):
        #print(casilla)
        vect_interpolados = interpolar_vectores(knight.rel_recorrido[casilla][:2],
                                            knight.rel_recorrido[casilla+1][:2],n)
        if((x+y)%2==0):
            chess.tablero[y][x][2] = [205,205,255]
        else:
            chess.tablero[y][x][2] = [0,0,50]

        chess.drawChess(screen,width)
        knight.rel_pos = knight.rel_recorrido[casilla][:2]

        poligono2.append(([knight.rel_pos[1]+delta/2,knight.rel_pos[0]+delta/2]))
        if len(poligono2) >1:
            pygame.draw.lines(screen,(0,0,255),0,poligono2,3)

        knight.draw(screen,delta)
        casilla += 1
        interpolados += 1
        time.sleep(.1)
    else:
        chess.drawChess(screen,width)

        poligono2.append([knight.rel_pos[1]+delta/2,knight.rel_pos[0]+delta/2])
        if len(poligono2) >1:
            pygame.draw.lines(screen,(0,0,255),0,poligono2,3)
        
        knight.rel_pos = vect_interpolados[interpolados]
        knight.draw(screen,delta)
        interpolados += 1
    
    
    
    pygame.display.flip()