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
velX = 1
velY = 1

def bounce():
    global velX, velY

    if (x == SCREEN_WIDTH or x == 0):
        velX = -velX
    if (y == SCREEN_HEIGHT or y == 0):
        velY = -velY

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    dog = pygame.image.load("dog.jpg")

    # RENDER YOUR GAME HERE
    bounce()

    x += velX
    y += velY
    screen.blit(dog, (x - dog.get_width() / 2, y - dog.get_height() / 2))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()