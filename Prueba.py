import pygame,sys #Importamos la libreria pygame, y sys
from pygame.locals import * #Importamos todos los modulos de la libreria pygame

pygame.init() #Inicializamos todos los modulos si o si
ventana = pygame.display.set_mode((800,600)) #Creamos un objeto que tendra la ventana principal, recibe como parametros el tamaño en x e y
pygame.display.set_caption("Prueba Logica") #Pone un titulo a la ventana

posX,posY = 300,300
pos_dosX,pos_dosY = 500,100

tanqueUno = pygame.image.load("Images/Tanque2.png") #Mediante el metodo load() podemos almacenar una imagen en un objeto
tanqueUnoRect = tanqueUno.get_rect()


tanqueDos = pygame.image.load("Images/Tanque2Refle.png")
tanqueDosRect = tanqueDos.get_rect()


velocidadTanqueUno = 1 #La imagen se movera a una velocidad de 1 pixeles
velocidadTanqueDos = 15

negro = (0,0,0) #Generamos el color blanco para la superficie de la ventana
derecha=True 
comienzo=False
score=0

fuente = pygame.font.SysFont("Arial",40) #Definimos una fuente del sistema
textoGameOver="GAME OVER"
textoTiempo=fuente.render("Time: ",0,(255,0,0))
textoFinJuego=fuente.render(textoGameOver,0,(255,0,0))
textoNada=fuente.render("",0,(0,0,0))

is_running=True

while is_running:
    ventana.fill(negro) #Cambia el color de la superficie

    tiempo=int("{:.0f}".format(pygame.time.get_ticks()/1000))#Obtenemos el tiempo desde que inicio el programa en milis segundos, al dividirlo por mil, obtendremos los segundos
    textoTiempo = fuente.render("Time: "+str(tiempo),0,(255,0,0)) #Si llego a segundos, lo almacenamos en el objeto contador
            
    textoScore=fuente.render("Score: "+str(score)+" (10)",0,(255,0,0))

    tanqueUnoRect.left = posX
    tanqueUnoRect.top = posY
    tanqueDosRect.left = pos_dosX
    tanqueDosRect.top = pos_dosY    

    if(tanqueUnoRect).colliderect(tanqueDosRect): #Detecta si hay colision o no, entre rectangulo_uno y rectangulo_dos
        velocidadTanqueUno = 0
        score+=1
        pos_dosY-=100
        posX-=600
        #print("Colisiono")
    else: 
        velocidadTanqueUno = 1
        #print("No hay colision")

    for event in pygame.event.get(): #Recorremos la lista de eventos
        if event.type == QUIT: #Si se presiono la X para cerrar la ventana
            pygame.quit() #Cerramos los modulos de pygame
            sys.exit() #Cerramos la ventana
        elif event.type == pygame.KEYDOWN: #Evalua si alguna tecla fue presionada con KEYDOWN
            if event.key == K_LEFT: #Comienza a evaluar que tecla se presiono
                pos_dosX -= velocidadTanqueDos
            elif event.key == K_RIGHT:
                pos_dosX += velocidadTanqueDos
            elif event.key == K_UP:
                pos_dosY -= velocidadTanqueDos
            elif event.key == K_DOWN:
                pos_dosY += velocidadTanqueDos
            elif event.key == K_SPACE:
                comienzo=True
                
        # elif event.type == pygame.KEYUP: #Evalua que tecla fue liberada con KEYUP
        #     if event.key == K_LEFT: #Comienza a evaluar que tecla se libero e imprimi un mensaje por consola
        #         print("Tecla Izquierda Liberada")
        #     elif event.key == K_RIGHT:
        #         print("Tecla Derecha Liberada")
        #     elif event.key == K_UP:
        #         print("Tecla Arriba Liberada")
        #     elif event.key == K_DOWN:
        #         print("Tecla Abajo Liberada")

    if derecha == True: #Si derecha es true, y posX menor a 650, aumenta los pixeles segun velocidad, cuando posX es 650, da false y pasa al siguiente bloque
        if posX<600:
            posX += velocidadTanqueUno
        else:
            derecha=False
    else:
        if posX>1: #Mientras posX sea mayor a 1, comenzara a restar pixeles segun velocidad, cuando sea 1, derecha sera true, y cambiara al bloque de arriba
            posX -= velocidadTanqueUno
        else:
            derecha = True
    
    ventana.blit(tanqueUno,(posX,posY)) #El metodo blit nos permite posicionar el objeto con la imagen en la superficie en determinadas coordenadas
    ventana.blit(textoTiempo,(30,10)) #Mostramos por pantalla el objeto contador
    ventana.blit(textoScore,(550,10))

    if score == 10:
        tiempoFin = tiempo
        ventana.blit(textoFinJuego,(260,500))
    else:
        if comienzo:
            ventana.blit(tanqueDos,(pos_dosX,pos_dosY)) #El metodo blit nos permite posicionar el objeto con la imagen en la superficie en determinadas coordenadas
        else:
            textoInicio = fuente.render("Pres Space to Start",0,(255,0,0))
            ventana.blit(textoInicio,(200,550))
    
    pygame.display.update() #La ventana se va a estar actualizando