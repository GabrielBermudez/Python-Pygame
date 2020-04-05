import pygame,sys #Importamos la libreria pygame, y sys
from pygame.locals import * #Importamos todos los modulos de la libreria pygame

pygame.init() #Inicializamos todos los modulos si o si
ventana = pygame.display.set_mode((800,600)) #Creamos un objeto que tendra la ventana principal, recibe como parametros el tamaño en x e y
pygame.display.set_caption("Hola Mundo") #Pone un titulo a la ventana

fuente = pygame.font.SysFont("Arial",30) #Definimos una fuente del sistema
aux=1
contador=fuente.render("Tiempo: ",0,(255,0,0))

while True:

    ventana.fill((0,0,0)) #Al poner un fondo de color, logramos que los textos no se superpongan
    tiempo = pygame.time.get_ticks()/1000 #Obtenemos el tiempo desde que inicio el programa en milis segundos, al dividirlo por mil, obtendremos los segundos

    if aux == tiempo: #Con este bloque, mostramos en consola cuando tiempo vaya sumando segundo por segundo
        aux+=1
        print(tiempo)
        contador = fuente.render("Tiempo: "+str(tiempo),0,(255,0,0)) #Si llego a segundos, lo almacenamos en el objeto contador
       
    for evento in pygame.event.get(): #Recorremos la lista de eventos
        if evento.type == QUIT: #Si se presiono la X para cerrar la ventana
            pygame.quit() #Cerramos los modulos de pygame
            sys.exit() #Cerramos la ventana

    ventana.blit(contador,(30,30)) #Mostramos por pantalla el objeto contador
    pygame.display.update() #La ventana se va a estar actualizando