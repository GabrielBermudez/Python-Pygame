import pygame,sys #Importamos la libreria pygame, y sys
from pygame.locals import * #Importamos todos los modulos de la libreria pygame

pygame.init() #Inicializamos todos los modulos si o si
ventana = pygame.display.set_mode((1024,600)) #Creamos un objeto que tendra la ventana principal, recibe como parametros el tamaño en x e y
pygame.display.set_caption("Hola Mundo") #Pone un titulo a la ventana

tanque = pygame.image.load("Images/Tanque.png") #Mediante el metodo load() podemos almacenar una imagen en un objeto
posX,posY = 100,150

velocidad = 2 #La imagen se movera a una velocidad de 2 pixeles
blanco = (255,255,255) #Generamos el color blanco para la superficie de la ventana
derecha=True 

while True:
    ventana.fill(blanco) #Cambia el color de la superficie
    ventana.blit(tanque,(posX,posY)) #El metodo blit nos permite posicionar el objeto con la imagen en la superficie en determinadas coordenadas
    
    for evento in pygame.event.get(): #Recorremos la lista de eventos
        if evento.type == QUIT: #Si se presiono la X para cerrar la ventana
            pygame.quit() #Cerramos los modulos de pygame
            sys.exit() #Cerramos la ventana

    if derecha == True: #Si derecha es true, y posX menor a 650, aumenta los pixeles segun velocidad, cuando posX es 650, da false y pasa al siguiente bloque
        if posX<650:
            posX += velocidad
        else:
            derecha=False
    else:
        if posX>1: #Mientras posX sea mayor a 1, comenzara a restar pixeles segun velocidad, cuando sea 1, derecha sera true, y cambiara al bloque de arriba
            posX -= velocidad
        else:
            derecha = True
    pygame.display.update() #La ventana se va a estar actualizando