import pygame, os
from explosionEffect import ExplosionEffect
import settings_stats

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENEMY_IMG = os.path.join(BASE_DIR, "img", "sprite.jpg")

class Enemy(pygame.sprite.Sprite):
    def __init__(self, master):
        super(Enemy, self).__init__()
        self.master = master
        self.master_rect = self.master.get_rect()
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.x = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def get_image(self):
        im = pygame.image.load(ENEMY_IMG)
        x, y = im.get_size()
        im = im.subsurface(0, 0, x // 2, y)
        return im

    def draw(self):
        self.master.blit(self.image, self.rect)

    def update(self, effects_group, enemies):
        self.y += settings_stats.stat['speed_enemy']
        self.rect.y = self.y
        if self.rect.y > self.master_rect.bottom:
            effect = ExplosionEffect(self.rect.centerx, self.rect.centery)
            effects_group.add(effect)
            enemies.empty()
            settings_stats.stat['bg_color'] = "ff0000"
            settings_stats.stat['heart'] -= 1


