import pygame,sys #Importamos la libreria pygame, y sys
from pygame.locals import * #Importamos todos los modulos de la libreria pygame

pygame.init() #Inicializamos todos los modulos si o si
ventana = pygame.display.set_mode((800,600)) #Creamos un objeto que tendra la ventana principal, recibe como parametros el tamaño en x e y
pygame.display.set_caption("Hola Mundo") #Pone un titulo a la ventana

tanque = pygame.image.load("Images/Tanque.png") #Mediante el metodo load() podemos almacenar una imagen en un objeto
posX,posY = 100,150

velocidad = 2 #La imagen se movera a una velocidad de 2 pixeles
blanco = (255,255,255) #Generamos el color blanco para la superficie de la ventana
derecha=True 

rectangulo_uno = pygame.Rect(0,0,100,50) #Creamos dos objetos, que almacenaran un rectangulo cada uno
rectangulo_dos = pygame.Rect(300,250,100,50)


while True:
    ventana.fill(blanco) #Cambia el color de la superficie
   
    pygame.draw.rect(ventana,(120,120,43),rectangulo_uno) #Dibujamos el rectangulo en la pantalla
    rectangulo_uno.left, rectangulo_uno.top = pygame.mouse.get_pos() #Mediante las coordenadas del mouse, modificamos la posicion del rectangulo

    pygame.draw.rect(ventana,(180,70,70),rectangulo_dos)

    if( rectangulo_uno).colliderect(rectangulo_dos): #Detecta si hay colision o no, entre rectangulo_uno y rectangulo_dos
        velocidad = 0
        print("Colisiono")
    else: 
        velocidad = 2
        print("No hay colision")

    for evento in pygame.event.get(): #Recorremos la lista de eventos
        if evento.type == QUIT: #Si se presiono la X para cerrar la ventana
            pygame.quit() #Cerramos los modulos de pygame
            sys.exit() #Cerramos la ventana

    if derecha == True: #Si derecha es true, y posX menor a 650, aumenta los pixeles segun velocidad, cuando posX es 650, da false y pasa al siguiente bloque
        if posX<700:
            posX += velocidad
            rectangulo_dos.left = posX
        else:
            derecha=False
    else:
        if posX>1: #Mientras posX sea mayor a 1, comenzara a restar pixeles segun velocidad, cuando sea 1, derecha sera true, y cambiara al bloque de arriba
            posX -= velocidad
            rectangulo_dos.left = posX
        else:
            derecha = True
    pygame.display.update() #La ventana se va a estar actualizando