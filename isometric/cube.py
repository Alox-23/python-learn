import pygame

class Cube:
    def __init__(self, x, y):
        self.img = pygame.image.load("img/cube.png")

        self.height = self.img.get_height()
        self.width = self.img.get_width()

        self.rect = self.img.get_rect()
        self.rect.center = (x, y)

    def draw(self, surf):
        surf.blit(self.img, self.rect)

