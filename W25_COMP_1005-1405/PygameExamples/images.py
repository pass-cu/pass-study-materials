# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

clock = pygame.time.Clock()

dog = pygame.image.load("dog.jpg")

running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    screen.blit(dog, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()