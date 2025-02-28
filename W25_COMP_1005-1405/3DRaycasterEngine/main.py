'''
DEMO PROJECT FOR A RAYCASTER ENGINE
This project uses Digital Differential Analyser (DDA) algorithmn to generate a pseudo-3D
world by projecting rays from the player and casting them towards the world.

This is by no means the most efficient/eligant implementation of DDA. It seeks merely to
be a demonstration of the capabilities of the engine.

Heavily influenced by the code of Sage3D on youtube.
https://www.youtube.com/watch?v=gYRrGTC7GtA&t=11s

Nicholas Waworuntu 
Feb 2025
'''

import pygame
import math

from consts import *
from player import *
from utils import *

def main():
    player = Player()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RAYCASTER ENGINE")

    clock = pygame.time.Clock()

    skyX = 0
    skyY = 0

    running = True
    while running:
        # Draws background and ground.
        screen.fill((100, 100, 100)) 

        # Draw Sky
        pygame.draw.rect(screen, (102, 196, 255), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT / 2)) 

        player.update()

        player.drawWorld(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()

        clock.tick(60)
    
    pygame.quit()

main()