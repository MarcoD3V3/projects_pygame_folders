import pygame

pygame.init()

# Dimensiones de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Personaje Movible")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Tamaño y posición inicial del personaje
character_size = 20
character_x, character_y = width // 2, height // 2
player__img = pygame.image.load("player.png")

# Velocidad del personaje
character_speed = 0.1

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()

    # Movimiento del personaje
    if keys[pygame.K_LEFT] and character_x > 0:
        character_x -= character_speed
    if keys[pygame.K_RIGHT] and character_x < width - character_size:
        character_x += character_speed
    if keys[pygame.K_UP] and character_y > 0:
        character_y -= character_speed
    if keys[pygame.K_DOWN] and character_y < height - character_size:
        character_y += character_speed

    # Limpiar la pantalla
    screen.fill(black)

    # Dibujar el personaje (un cuadrado)
    pygame.draw.rect(screen, white, (character_x, character_y, character_size, character_size))

    # Actualizar la pantalla
    pygame.display.update()

pygame.quit()
