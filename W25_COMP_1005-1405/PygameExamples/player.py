# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

clock = pygame.time.Clock()

running = True

x = 32
y = 32
velX = 0
velY = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # HANDLE PLAYER MOVEMENT
    keys = pygame.key.get_pressed()

    velX = 0
    velY = 0

    if (keys[pygame.K_w]):
        velY = -1
    if (keys[pygame.K_s]):
        velY = 1
    if (keys[pygame.K_a]):
        velX = -1
    if (keys[pygame.K_d]):
        velX = 1

    x += velX
    y += velY

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 32, 32))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()