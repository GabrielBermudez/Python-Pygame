import pygame,sys #Importamos la libreria pygame, y sys
from pygame.locals import * #Importamos todos los modulos de la libreria pygame

color1 = (0,140,60) #Creamos un objeto que almacenara un color RGB
color2 = pygame.Color(255,120,9) #Creamos un objeto que almacenara un color RGB mediante la funcion Color()

pygame.init() #Inicializamos todos los modulos si o si
ventana = pygame.display.set_mode((800,600)) #Creamos un objeto que tendra la ventana principal, recibe como parametros el tamaño en x e y
pygame.display.set_caption("Hola Mundo") #Pone un titulo a la ventana

while True:
    ventana.fill(color2) #Cambia el color de la superficie por el que se encuentra en el objeto
    for evento in pygame.event.get(): #Recorremos la lista de eventos
        if evento.type == QUIT: #Si se presiono la X para cerrar la ventana
            pygame.quit() #Cerramos los modulos de pygame
            sys.exit() #Cerramos la ventana

    pygame.display.update() #La ventana se va a estar actualizando