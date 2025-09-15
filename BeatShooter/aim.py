import pygame, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AIM_IMG = os.path.join(BASE_DIR, "img", "aim.gif")

class Aim:

    def __init__(self, master):
        self.master = master
        self.image = pygame.image.load(AIM_IMG)
        self.aim_rect = self.image.get_rect()
        self.master_rect = master.get_rect()
        self.aim_rect.centerx = self.master_rect.centerx
        self.center = float(self.aim_rect.centerx)
        self.aim_rect.bottom = self.master_rect.bottom
        self.mright = False
        self.mleft = False


    def output(self):
        self.master.blit(self.image, self.aim_rect)

    def update_aim(self):
        if self.mright and self.aim_rect.right < self.master_rect.right:
            self.center += 3.5

        if self.mleft and self.aim_rect.left > 0:
            self.center -= 3.5

        self.aim_rect.centerx = self.center

    def get_center(self):
        return self.aim_rect


