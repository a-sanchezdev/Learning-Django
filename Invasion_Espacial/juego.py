import pygame
import os
from pygame import mixer
import random
import math
#Inicializar Pygame
pygame.init()


#Crear la pantalla
pantalla = pygame.display.set_mode((800,600))

#Titulo e Icono
pygame.display.set_caption("Invasion Espacial")
ruta_imagen = os.path.join(os.path.dirname(__file__), "ufo.png")
icono = pygame.image.load(ruta_imagen)
pygame.display.set_icon(icono)
ruta_fondo = os.path.join(os.path.dirname(__file__), "Fondo.jpg")
fondo = pygame.image.load(ruta_fondo)

#Agregar musica
ruta_musica_fondo = os.path.join(os.path.dirname(__file__), "MusicaFondo.mp3")
mixer.music.load(ruta_musica_fondo)
mixer.music.set_volume(0.3)
mixer.music.play(-1)



#Jugador variables
img_ju= os.path.join(os.path.dirname(__file__), "spaceship.png")
img_jugador = pygame.image.load(img_ju)
jugador_x = 368
jugador_y = 500 
jugador_x_cambio = 0
jugador_y_cambio = 0

#variables del enemigo
img_ju2= []
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_ju2= os.path.join(os.path.dirname(__file__), "monster.png")
    img_enemigo.append(pygame.image.load(img_ju2))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.6)
    enemigo_y_cambio.append(50)

#variables del bala
balas = []
img_ju3= os.path.join(os.path.dirname(__file__), "bullet.png")
img_bala = pygame.image.load(img_ju3)
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

#puntaje
puntaje = 0
letra= os.path.join(os.path.dirname(__file__), "PressStart2P-Regular.ttf")
fuente = pygame.font.Font(letra,25)
texto_x = 10
texto_y = 10

#texto final del juego
letra_final= os.path.join(os.path.dirname(__file__), "PressStart2P-Regular.ttf")
fuente_final = pygame.font.Font(letra_final,40)

#funcion mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntuaje: {puntaje}",True,(255,255,255))
    pantalla.blit(texto,(x,y))

#funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

#funcion enemigo
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene],(x,y))

#funcion disparar bala 
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x+16,y+10))


#funcion texto final de juego
def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True,(255,255,255))
    pantalla.blit(mi_fuente_final,(230,250))

#Funcion detectar colisiones
def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_2-x_1,2) + math.pow(y_2-y_1,2))
    if distancia < 27:
        return True
    else:
        return False

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
                ruta_musica_bala = os.path.join(os.path.dirname(__file__), "disparo.mp3")
                sonido_bala = mixer.Sound(ruta_musica_bala)
                sonido_bala.set_volume(0.3)
                sonido_bala.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                    }
                balas.append(nueva_bala)

                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y)
                
                # Movimiento bala
                for bala in balas:
                    bala["y"] += bala["velocidad"]
                    pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
                    if bala["y"] < 0:
                        balas.remove(bala)

        #evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #Modificar ubicacion jugador
    jugador_x += jugador_x_cambio

    #modificar ubicacion enemigo
    for  e in range(cantidad_enemigos):

        #Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
         
        enemigo_x[e] += enemigo_x_cambio[e]

        #mantener dentro de los bordes a enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.6
            enemigo_y[e] += enemigo_y_cambio[e]
        if enemigo_x[e] >= 736:
            enemigo_x_cambio[e]=-0.6
            enemigo_y[e] += enemigo_y_cambio[e]


        #Colision
        colision = hay_colision(enemigo_x[e],enemigo_y[e],bala_x,bala_y)
        if colision:
            ruta_musica_colision = os.path.join(os.path.dirname(__file__), "Golpe.mp3")
            sonido_colision = mixer.Sound(ruta_musica_colision)
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje+=1
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50,200)

        enemigo(enemigo_x[e],enemigo_y[e],e)

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

    

    jugador(jugador_x,jugador_y)

    mostrar_puntaje(texto_x,texto_y)

    #Actualizar
    pygame.display.update()

