import pygame,sys #Importamos la libreria pygame, y sys
from pygame.locals import * #Importamos todos los modulos de la libreria pygame

pygame.init() #Inicializamos todos los modulos si o si
ventana = pygame.display.set_mode((800,600)) #Creamos un objeto que tendra la ventana principal, recibe como parametros el tamaño en x e y
pygame.display.set_caption("Hola Mundo") #Pone un titulo a la ventana


color = pygame.Color(130,180,150) #Creamos un objeto que almacenara un color RGB mediante la funcion Color()
pygame.draw.line(ventana,color,(60,80),(160,108),8) #Dibuja una linea, recibe como parametro, la superficie, el color, el punto de origen, el punto de fin, y el grosor

print(color.r)
print(color.g)
print(color.b)


while True:
    for evento in pygame.event.get(): #Recorremos la lista de eventos
        if evento.type == QUIT: #Si se presiono la X para cerrar la ventana
            pygame.quit() #Cerramos los modulos de pygame
            sys.exit() #Cerramos la ventana

    pygame.display.update() #La ventana se va a estar actualizando