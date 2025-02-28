import pygame
import math
import random

from consts import *
from utils import *

class Player:
    x = 4.5
    y = 5.1

    speed = 0.05

    angle = 0
    fov = 30

    DEBUG_MODE = False

    def __init__(self):
        pass

    def castRay(self, screen, angle):
        # Correct angle if greater than 2PI or less than 0
        if (angle > 2 * PI):
            angle -= 2 * PI
        if (angle < 0):
            angle += 2 * PI

        # Return variables.
        distanceFinal = 0
        shadeAlpha = 1

        # The distance of the horizontal component and vertical component are set to an
        # absurdly big number that will be shrunk later once the final distances are
        # calculated.
        distanceH = 1000000
        distanceV = 1000000

        # Ray Variables
        horiztonalRayX = self.x
        horiztonalRayY = self.y
        verticalRayX = self.x
        verticalRayY = self.y

        rayX = self.x
        rayY = self.y

        xOffset = 0
        yOffset = 0

        a = angle      # Player Angle

        # HORIZONTAL LINE CHECKING

        aTan = 0
        if (a != 0): aTan = -1 / math.tan(a)

        dofMax = 8
        dof = 0

        # Looking Up.
        if (a > PI):
            rayY = math.floor(self.y) - 0.0001
            rayX = (self.y - rayY) * aTan + self.x
            yOffset = -1
            xOffset = -yOffset * aTan

        # Looking Down.
        if (a < PI):
            rayY = math.floor(self.y) + 1
            rayX = (self.y - rayY) * aTan + self.x
            yOffset = 1
            xOffset = -yOffset * aTan

        # Looking left or right.
        if (a == 0 or a == PI):
            rayX = self.x
            rayY = self.y
            dof = dofMax

        while (dof < dofMax):
            p = getOnMap(rayX, rayY)

            if (p >= 0 and p < MAP_WIDTH * MAP_HEIGHT and MAP[p] > 0):
                horiztonalRayX = rayX
                horiztonalRayY = rayY
                distanceH = pointDistance(self.x, self.y, horiztonalRayX, horiztonalRayY)
                dof = dofMax
            else:
                rayX += xOffset
                rayY += yOffset
                dof += 1

        # VERTICAL LINE CHECKING

        nTan = -math.tan(a)
        dof = 0

        # Looking Left.
        if (a > PI / 2 and a < PI / 2 * 3):
            rayX = math.floor(self.x) - 0.0001
            rayY = (self.x - rayX) * nTan + self.y
            
            xOffset = -1
            yOffset = -xOffset * nTan

        # Looking Right.
        if (a < PI / 2 or a > PI / 2 * 3):
            rayX = math.floor(self.x) + 1 
            rayY = (self.x - rayX) * nTan + self.y
            xOffset = 1
            yOffset = -xOffset * nTan

        # Looking Up or Down.
        if (a == 0 or a == PI):
            rayX = self.x
            rayY = self.y
            dof = dofMax

        while (dof < dofMax):
            p = getOnMap(rayX, rayY)

            if (p >= 0 and p < MAP_WIDTH * MAP_HEIGHT and MAP[p] > 0):
                verticalRayX = rayX
                verticalRayY = rayY
                distanceV = pointDistance(self.x, self.y, verticalRayX, verticalRayY)
                dof = dofMax
            else:
                rayX += xOffset
                rayY += yOffset
                dof += 1

        if (distanceV < distanceH):
            rayX = verticalRayX
            rayY = verticalRayY
            shadeAlpha = 0.8
        if (distanceH < distanceV):
            rayX = horiztonalRayX
            rayY = horiztonalRayY
            shadeAlpha = 1.0

        distanceFinal = pointDistance(self.x, self.y, rayX, rayY)

        # FIX FISH EYE
        cosineAngle = self.angle - a
        if (cosineAngle > 2 * PI):
            cosineAngle -= 2 * PI
        if (cosineAngle < 0):
            cosineAngle += 2 * PI

        distanceFinal = distanceFinal * math.cos(cosineAngle)

        if (self.DEBUG_MODE):
            pygame.draw.line(screen, (255, 200, 0),
                            (self.x * TILE_SIZE, self.y * TILE_SIZE),
                            (rayX * TILE_SIZE, rayY * TILE_SIZE), 3)
        return distanceFinal, shadeAlpha

    def update(self):
        keys = pygame.key.get_pressed()

        move = 0

        if (keys[pygame.K_a]): 
            self.angle -= RAD
            if (self.angle < 0): 
                self.angle += 2 * PI
        if (keys[pygame.K_d]): 
            self.angle += RAD
            if (self.angle > 2 * PI):
                self.angle -= 2 * PI
        if (keys[pygame.K_w]): move = 1
        if (keys[pygame.K_s]): move = -1

        if (move != 0):
            xMove = math.cos(self.angle) * self.speed * move
            yMove = math.sin(self.angle) * self.speed * move

            if (MAP[getOnMap(self.x + xMove, self.y)] > 0):
                xMove = 0
            if (MAP[getOnMap(self.x, self.y + yMove)] > 0):
                yMove = 0

            self.x += xMove
            self.y += yMove

    def drawWorld(self, screen):
        fidelity = SCREEN_WIDTH
        rays = fidelity

        theta = 0
        step = self.fov / fidelity * RAD
        thetaOffset = self.fov / 2 * RAD

        for i in range(int(rays)):
            # GET DISTANCE FROM RAY CAST
            distance, shadeAlpha = self.castRay(screen, self.angle - thetaOffset + theta )
            distance = distance * TILE_SIZE

            if (distance == 0):
                distance = SCREEN_HEIGHT

            # WALL HEIGHT
            height = TILE_SIZE * SCREEN_HEIGHT / distance
            if (height < 0):
                height = 0
            if (height > SCREEN_HEIGHT):
                height = SCREEN_HEIGHT

            offset = SCREEN_HEIGHT / 2 - height / 2

            pygame.draw.line(screen, (0, 0, 200 * shadeAlpha),
                             (i, SCREEN_HEIGHT - offset),
                             (i, SCREEN_HEIGHT - height - offset))

            theta += step

        if (self.DEBUG_MODE):
            self.drawMap(screen)
            self.draw(screen)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x * TILE_SIZE, self.y * TILE_SIZE), 3)
        pygame.draw.line(screen, (255, 255, 255), 
                        (self.x * TILE_SIZE, self.y * TILE_SIZE), 
                        (self.x * TILE_SIZE + math.cos(self.angle) * 16, 
                         self.y * TILE_SIZE + math.sin(self.angle) * 16), 1)
        
    # Debug function used to draw the map representation (2D top down) of the world.
    def drawMap(self, screen):
        p = 0
        for t in MAP:
            tCol = (255, 255, 255) if MAP[p] > 0 else (0, 0, 0)
            pygame.draw.rect(screen, tCol, pygame.Rect(
                (p % MAP_WIDTH) * TILE_SIZE,
                math.floor(p / MAP_HEIGHT) * TILE_SIZE,
                TILE_SIZE - 1,
                TILE_SIZE - 1))
            p += 1

        