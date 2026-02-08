import pygame
import numpy as np


class Tablero:
    def __init__(self, n) -> None:
        self.n = n
        self.tablero = 0
        self.generar()
        pass

    def generar(self):
        blancas = [255,255,255]
        negras = [0,0,0]

        self.tablero = ([[[0,0,blancas] if (i+j)%2==0 else [0,0,negras] for i in range(self.n)] for j in range(self.n)])

        for row in range(self.n):
            for col in range(self.n):
                pos1 = [row-2,col-1]
                pos2 = [row-2,col+1]
                pos3 = [row-1,col+2]
                pos4 = [row+1,col+2]
                pos5 = [row+2,col+1]
                pos6 = [row+2,col-1]
                pos7 = [row+1,col-2]
                pos8 = [row-1,col-2]

                if(pos1[0]>= 0 and pos1[1]>=0):
                    self.tablero[pos1[0]][pos1[1]][0] += 1

                if(pos2[0]>= 0 and pos2[1]<self.n):
                    self.tablero[pos2[0]][pos2[1]][0] += 1

                if(pos3[0]>= 0 and pos3[1]<self.n):
                    self.tablero[pos3[0]][pos3[1]][0] += 1

                if(pos4[0]<self.n and pos4[1]<self.n):
                    self.tablero[pos4[0]][pos4[1]][0] += 1

                if(pos5[0]<self.n and pos5[1]<self.n):
                    self.tablero[pos5[0]][pos5[1]][0] += 1

                if(pos6[0]<self.n and pos6[1]>=0):
                    self.tablero[pos6[0]][pos6[1]][0] += 1

                if(pos7[0]<self.n and pos7[1]>=0):
                    self.tablero[pos7[0]][pos7[1]][0] += 1

                if(pos8[0]>= 0 and pos8[1]>=0):
                    self.tablero[pos8[0]][pos8[1]][0] += 1

    def drawChess(self,screen,width):
        delta = width/self.n
        x = 0
        y = 0
        for i,val in enumerate(self.tablero):
            for j, val2 in enumerate(val):
                y = i*delta
                x = j*delta
                color = val2[2]
                pygame.draw.rect(screen,color,(x,y,x+delta,y+delta))
                '''if (i+j)%2 == 0:
                    pygame.draw.rect(screen,(255,255,255),(x,y,x+delta,y+delta))
                else:
                    pygame.draw.rect(screen,(0,0,0),(x,y,x+delta,y+delta))'''


class Caballo:
    def __init__(self,position) -> None:
        self.position = np.array(position, dtype=int)
        self.rel_pos = np.array(position, dtype=float)
        self.recorrido = []
        self.rel_recorrido = 0
        self.numero_casilla = []
        self.vel_const = .015
        self.knight = pygame.image.load("caballo/LightKnight.webp")
        

    def Recorrido(self,tablero,delta):
        self.recorrido.append([self.position[1],self.position[0]])
        tablero.tablero[self.position[1]][self.position[0]][1] = 1
        

        n = tablero.n
        self.numero_casilla = np.array([[-1 for i in range(n)] for j in range(n)])
        self.numero_casilla[self.position[1]][self.position[0]] = 0
        count = 1
        
        while(count < (n*n)):
            #sentido horario 1
            pos = [
                [self.position[1]-2,self.position[0]-1,0],
                [self.position[1]-2,self.position[0]+1,1],
                [self.position[1]-1,self.position[0]+2,0],
                [self.position[1]+1,self.position[0]+2,1],
                [self.position[1]+2,self.position[0]+1,0],
                [self.position[1]+2,self.position[0]-1,1],
                [self.position[1]+1,self.position[0]-2,0],
                [self.position[1]-1,self.position[0]-2,1]
                
            ]

            posible_jugada = []
            posible_jugada2 = []
            posible_jugada3 = []
            # Paso 2
            
            for i in pos:

                if(i[0] < n and i[0] >= 0 and i[1] < n and i[1] >= 0 
                and tablero.tablero[i[0]][i[1]][1] == 0):
                    tablero.tablero[i[0]][i[1]][0] -= 1
                    if(len(posible_jugada)==0):
                        posible_jugada.append(i)
                    else:
                        last = [posible_jugada[-1][0],posible_jugada[-1][1]]
                        if(tablero.tablero[i[0]][i[1]][0] < 
                           tablero.tablero[last[0]][last[1]][0] ):
                            posible_jugada.pop()
                            posible_jugada.append(i)
                        elif(tablero.tablero[i[0]][i[1]][0] == 
                           tablero.tablero[last[0]][last[1]][0] ):
                            posible_jugada.append(i)
            if(len(posible_jugada) == 1):
                tablero.tablero[posible_jugada[0][0]][posible_jugada[0][1]][1] = 1
                self.position[0] = posible_jugada[0][1]
                self.position[1] = posible_jugada[0][0]   
                            
            # Paso 3
            
            elif(len(posible_jugada) > 1):
                for casilla in posible_jugada:
                    if(len(posible_jugada2) == 0):
                        posible_jugada2.append(casilla)
                    else:
                        if(distancia_minima(casilla,n) < distancia_minima(posible_jugada2[-1],n)):
                            posible_jugada2.pop()
                            posible_jugada2.append(casilla)
                        elif(distancia_minima(casilla,n) == distancia_minima(posible_jugada2[-1],n)):
                            posible_jugada2.append(casilla)
            if(len(posible_jugada2) == 1):
                tablero.tablero[posible_jugada2[0][0]][posible_jugada2[0][1]][1] = 1
                self.position[0] = posible_jugada2[0][1]
                self.position[1] = posible_jugada2[0][0]
            # Paso 4
            elif(len(posible_jugada2) > 1):
                for casilla in posible_jugada2:
                    if(len(posible_jugada2) == 0):
                        posible_jugada2.append(casilla)
                    else:
                        if(minima_pared(casilla,n) < minima_pared(posible_jugada2[-1],n)):
                            posible_jugada2.pop()
                            posible_jugada2.append(casilla)
                        elif(minima_pared(casilla,n) == minima_pared(posible_jugada2[-1],n)):
                            posible_jugada3.append(casilla)
            if(len(posible_jugada3) == 1):
                tablero.tablero[posible_jugada2[0][0]][posible_jugada2[0][1]][1] = 1
                self.position[0] = posible_jugada2[0][1]
                self.position[1] = posible_jugada2[0][0]
            # Paso 5
            elif(len(posible_jugada3) == 2):
                if(posible_jugada3[0][1] == 1):
                    tablero.tablero[posible_jugada3[0][0]][posible_jugada3[0][1]][1] = 1
                    self.position[0] = posible_jugada3[0][1]
                    self.position[1] = posible_jugada3[0][0]
                else:
                    tablero.tablero[posible_jugada3[1][0]][posible_jugada3[1][1]][1] = 1
                    self.position[0] = posible_jugada3[1][1]
                    self.position[1] = posible_jugada3[1][0]
            
            self.numero_casilla[self.position[1]][self.position[0]] = count
            self.recorrido.append([self.position[1],self.position[0]])
            
            count += 1
        self.rel_recorrido = np.array(self.recorrido, dtype=float) * delta

    def draw(self,screen,delta):
        self.knight = pygame.transform.scale(self.knight,(delta,delta))
        screen.blit(self.knight,(self.rel_pos[1],self.rel_pos[0]))
    
    def move(self):
        self.rel_pos += (self.vel*self.vel_const)

def distancia_manhattan(punto1, punto2):
    return abs(punto1[0] - punto2[0]) + abs(punto1[1] - punto2[1])

def distancia_minima(punto, n):
    esquinas = [(0, 0), (0, n), (n, 0), (n, n)]
    resultado = n

    for esquina in esquinas:
        a = distancia_manhattan(esquina,punto)
        if(a < resultado):
            resultado = a
    return resultado

def minima_pared(punto,n):
    distancia_hasta_pared_horizontal = min(punto[0], n - punto[0])
    distancia_hasta_pared_vertical = min(punto[1], n - punto[1])
    
    return min(distancia_hasta_pared_horizontal, distancia_hasta_pared_vertical)

def printMat(arr):
    for i in arr:
        print(i)
 
'''tab1 = Tablero(8)
caballo = Caballo([4,4])

caballo.Recorrido(tab1,1)
printMat(caballo.numero_casilla)'''