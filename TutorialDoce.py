import pygame,sys #Importamos la libreria pygame, y sys
from pygame.locals import * #Importamos todos los modulos de la libreria pygame

pygame.init() #Inicializamos todos los modulos si o si
ventana = pygame.display.set_mode((800,600)) #Creamos un objeto que tendra la ventana principal, recibe como parametros el tamaño en x e y
pygame.display.set_caption("Hola Mundo") #Pone un titulo a la ventana

miFuente = pygame.font.Font(None,30) #Generamos una fuente predeterminada al poner none, podriamos remplazarlo por una ruta de una fuente en el sistema
miFuenteSistema = pygame.font.SysFont("Arial",30) #Generamos una fuente que ya trae el sistema

miTexto = miFuente.render("GAME OVER",0,(255,0,0))  #El metodo render() renderiza el texto pasado como parametro y color, almacenando el un objeto
miTextoSistema = miFuenteSistema.render("GAME OVER",0,(255,0,0))

while True:
    for evento in pygame.event.get(): #Recorremos la lista de eventos
        if evento.type == QUIT: #Si se presiono la X para cerrar la ventana
            pygame.quit() #Cerramos los modulos de pygame
            sys.exit() #Cerramos la ventana

    ventana.blit(miTexto,(200,200)) #El metodo blit va a mostrar al objeto en la pantalla
    ventana.blit(miTextoSistema,(200,250))
    pygame.display.update() #La ventana se va a estar actualizando