import pygame
import sys  # Importamos la libreria pygame, y sys
from pygame.locals import *  # Importamos todos los modulos de la libreria pygame

pygame.init()  # Inicializamos todos los modulos si o si
# Creamos un objeto que tendra la ventana principal, recibe como parametros el tamaño en x e y
ventana = pygame.display.set_mode((1024, 600))
pygame.display.set_caption("Hola Mundo")  # Pone un titulo a la ventana

# Mediante el metodo load() podemos almacenar una imagen en un objeto
tanque = pygame.image.load("Images/Tanque.png")
posX, posY = 100, 150

velocidad = 4  # La imagen se movera a una velocidad de 2 pixeles
# Generamos el color blanco para la superficie de la ventana
blanco = (255, 255, 255)
derecha = True

while True:
    ventana.fill(blanco)  # Cambia el color de la superficie
    # El metodo blit nos permite posicionar el objeto con la imagen en la superficie en determinadas coordenadas
    ventana.blit(tanque, (posX, posY))

    for event in pygame.event.get():  # Recorremos la lista de eventos
        if event.type == QUIT:  # Si se presiono la X para cerrar la ventana
            pygame.quit()  # Cerramos los modulos de pygame
            sys.exit()  # Cerramos la ventana
        elif event.type == pygame.KEYDOWN: #Evalua si alguna tecla fue presionada con KEYDOWN
            if event.key == K_LEFT: #Comienza a evaluar que tecla se presiono
                posX -= velocidad
            elif event.key == K_RIGHT:
                posX += velocidad
            elif event.key == K_UP:
                posY -= velocidad
            elif event.key == K_DOWN:
                posY += velocidad
        elif event.type == pygame.KEYUP: #Evalua que tecla fue liberada con KEYUP
            if event.key == K_LEFT: #Comienza a evaluar que tecla se libero e imprimi un mensaje por consola
                print("Tecla Izquierda Liberada")
            elif event.key == K_RIGHT:
                print("Tecla Derecha Liberada")
            elif event.key == K_UP:
                print("Tecla Arriba Liberada")
            elif event.key == K_DOWN:
                print("Tecla Abajo Liberada")

    pygame.display.update() #La ventana se va a estar actualizando
