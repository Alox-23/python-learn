import pygame
from settings import *
import cube

pygame.init()
screan = pygame.display.set_mode((HRES, VRES))
display = pygame.Surface((HRES//ZOOM, VRES//ZOOM))
clock = pygame.time.Clock()

cubes = []

trans_vectori = pygame.math.Vector2(0.5*TILE_SIZE, 0.25*TILE_SIZE)
trans_vectorj = pygame.math.Vector2(-0.5*TILE_SIZE, 0.25*TILE_SIZE)

for i in range(9):
    for j in range(9):
        x = i*trans_vectori.x+j*trans_vectorj.x
        y = i*trans_vectori.y+j*trans_vectorj.y
        x += HRES//4
        y += VRES//4
        cubes.append(cube.Cube(x, y-i*10))

running = True
while running:
    display.fill((82, 176, 247))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in cubes:
        i.draw(display)

    clock.tick(FPS)

    screan.blit(pygame.transform.scale(display, (HRES, VRES)), (0,0))
    pygame.display.update()
