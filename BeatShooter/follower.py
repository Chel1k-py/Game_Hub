import pygame, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FOLLOWER_IMG = os.path.join(BASE_DIR, "img", "line.png")

class Follower(pygame.sprite.Sprite):
    def __init__(self, master, aim):
        super(Follower, self).__init__()
        self.master = master
        self.image = pygame.image.load(FOLLOWER_IMG)
        self.rect = pygame.Rect(0, 0, 50, 1)
        self.rect.centerx = aim.aim_rect.centerx
        self.rect.top = aim.aim_rect.top
        self.rect.y += 35


    def update(self, aim):
        self.rect.centerx = aim.aim_rect.centerx - 0

    def draw_follower(self):
        self.master.blit(self.image, (self.rect.x - 50, self.rect.y))
