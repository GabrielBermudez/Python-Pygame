import pygame,sys #Importamos la libreria pygame, y sys
from pygame.locals import * #Importamos todos los modulos de la libreria pygame

pygame.init() #Inicializamos todos los modulos si o si
ventana = pygame.display.set_mode((800,600)) #Creamos un objeto que tendra la ventana principal, recibe como parametros el tamaño en x e y
pygame.display.set_caption("Hola Mundo") #Pone un titulo a la ventana

color2 = pygame.Color(117,92,72)

tanque = pygame.image.load("Images/Tanque.png") #Mediante el metodo load() podemos almacenar una imagen en un objeto
posX,posY = 200,150
ventana.fill(color2)
ventana.blit(tanque,(posX,posY)) #El metodo blit nos permite posicionar el objeto con la imagen en la superficie en determinadas coordenadas

while True:
   
    for evento in pygame.event.get(): #Recorremos la lista de eventos
        if evento.type == QUIT: #Si se presiono la X para cerrar la ventana
            pygame.quit() #Cerramos los modulos de pygame
            sys.exit() #Cerramos la ventana

    pygame.display.update() #La ventana se va a estar actualizando