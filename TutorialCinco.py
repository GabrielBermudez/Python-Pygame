import pygame,sys #Importamos la libreria pygame, y sys
from pygame.locals import * #Importamos todos los modulos de la libreria pygame

pygame.init() #Inicializamos todos los modulos si o si
ventana = pygame.display.set_mode((800,600)) #Creamos un objeto que tendra la ventana principal, recibe como parametros el tamaño en x e y
pygame.display.set_caption("Hola Mundo") #Pone un titulo a la ventana

pygame.draw.circle(ventana,(8,70,128),(88,98),20) #Dibuja un circulo, recibe como parametro, la superficie, el color, el punto central del circulo y el radio
pygame.draw.rect(ventana,(130,70,70),(0,0,100,50)) #Dibuja un rectangulo, recibe como parametro, la superficie, el color, el punto de origin super izquierdo, el ancho y el alto
pygame.draw.polygon(ventana,(90,180,70),((140,0),(291,106),(237,277),(56,277),(0,106))) #Dibula un poligono, recibe como parametro, la superficie, el color, y entre tuplas, una serie de coordenadas, pygame luego se encarga de unirlos

while True:
    for evento in pygame.event.get(): #Recorremos la lista de eventos
        if evento.type == QUIT: #Si se presiono la X para cerrar la ventana
            pygame.quit() #Cerramos los modulos de pygame
            sys.exit() #Cerramos la ventana

    pygame.display.update() #La ventana se va a estar actualizando