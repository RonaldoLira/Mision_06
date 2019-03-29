# encoding: UTF-8
# Autor: Ronaldo Estefano Lira Buendia
# Crear espirografos
import math
import pygame  # Librería de pygame



# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = 255, 255, 255
AMARILLO = 255, 243, 0
VERDE_BANDERA = (27, 94, 32)  # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)  # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)  # nada de rojo, ni verde, solo azul
ROSA = 244, 0, 255

# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        radio = 50
        for angulo in range(0, 360 + 1, 20):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(radio * math.cos(a))
            y = int(radio * math.sin(a))
            pygame.draw.circle(ventana, ROJO, ((x + ALTO // 2), (ANCHO // 2 + y)), radio, 1)


        reloj.tick(40)
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)


        radio = 150
        for angulo in range(0, 360 + 1, 20):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(radio * math.cos(a))
            y = int(radio * math.sin(a))
            pygame.draw.circle(ventana, AZUL, ((x + ALTO // 2), (ANCHO // 2 + y)), radio, 1)

        reloj.tick(40)
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)


        radio = 100
        for angulo in range(0, 360 + 1, 20):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(radio * math.cos(a))
            y = int(radio * math.sin(a))
            pygame.draw.circle(ventana, AMARILLO, ((x + ALTO // 2), (ANCHO // 2 + y)), radio, 1)

        reloj.tick(40)
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)

        radio = 200
        for angulo in range(90, 360 + 1, 50):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(radio * math.cos(a))
            y = int(radio * math.sin(a))
            pygame.draw.circle(ventana, VERDE_BANDERA, ((x + ALTO // 2), (ANCHO // 2 + y)), radio, 1)

        reloj.tick(40)
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)

        radio = 300
        for angulo in range(100, 360 + 1, 60):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(radio * math.cos(a))
            y = int(radio * math.sin(a))
            pygame.draw.circle(ventana, ROSA, ((x + ALTO // 2), (ANCHO // 2 + y)), radio, 1)

        reloj.tick(40)
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()  # Por ahora, solo dibuja


# Llamas a la función principal
main()