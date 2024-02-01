import pygame
import os
import random
#Inicializar Pygame
pygame.init()


#Crear la pantalla
pantalla = pygame.display.set_mode((800,600))

#Titulo e Icono
pygame.display.set_caption("Invasion Espacial")
ruta_imagen = os.path.join(os.path.dirname(__file__), "ufo.png")
icono = pygame.image.load(ruta_imagen)
ruta_fondo = os.path.join(os.path.dirname(__file__), "Fondo.jpg")
fondo = pygame.image.load(ruta_fondo)

pygame.display.set_icon(icono)

#Jugador variables
img_ju= os.path.join(os.path.dirname(__file__), "spaceship.png")
img_jugador = pygame.image.load(img_ju)
jugador_x = 368
jugador_y = 500 
jugador_x_cambio = 0
jugador_y_cambio = 0

#variables del enemigo
img_ju2= os.path.join(os.path.dirname(__file__), "monster.png")
img_enemigo = pygame.image.load(img_ju2)
enemigo_x = random.randint(0,736)
enemigo_y = random.randint(50,200)
enemigo_x_cambio = 0.4
enemigo_y_cambio = 50

#variables del bala
img_ju3= os.path.join(os.path.dirname(__file__), "bullet.png")
img_bala = pygame.image.load(img_ju3)
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

#funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

#funcion enemigo
def enemigo(x,y):
    pantalla.blit(img_enemigo,(x,y))

#funcion disparar bala 
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x+16,y+10))


#Loop del juego
se_ejecuta = True
while se_ejecuta:
    pantalla.blit(fondo,(0,0))
    #iterar eventos
    for evento in pygame.event.get():
        #cerrar evento
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.4
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.4
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y)

        #evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #Modificar ubicacion jugador
    jugador_x += jugador_x_cambio

    #modificar ubicacion enemigo
    enemigo_x += enemigo_x_cambio

    #movimiento de bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible == True:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio


    #mantener dentro de bordes jugador
    if jugador_x <= 0:
        jugador_x = 0
    if jugador_x >= 736:
        jugador_x = 736

    #mantener dentro de los bordes a enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.4
        enemigo_y += enemigo_y_cambio
    if enemigo_x >= 736:
        enemigo_x_cambio=-0.4
        enemigo_y += enemigo_y_cambio


    jugador(jugador_x,jugador_y)
    enemigo(enemigo_x,enemigo_y)

    #Actualizar
    pygame.display.update()

