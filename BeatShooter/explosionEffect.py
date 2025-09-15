import pygame, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPRITE_IMG = os.path.join(BASE_DIR, "img", "sprite.jpg")

class ExplosionEffect(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(ExplosionEffect, self).__init__()
        self.image = self.get_image()
        self.rect = self.image.get_rect(center=(x, y))
        self.life = 30

    def get_image(self):
        im = pygame.image.load(SPRITE_IMG)
        x, y = im.get_size()
        im = im.subsurface(x // 2, 0, x // 2, y)
        return im

    def update(self):
        self.life -= 1
        if self.life <= 0:
            self.kill()

