import pygame, os
from hearts import Hearts
import settings_stats

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(BASE_DIR, "img", "score.png")

class Score(Hearts):

    def __init__(self, master):
        super().__init__(master)
        self.image = pygame.image.load(IMG_PATH)
        self.rect = self.image.get_rect()
        self.rect.topright = (self.master_rect.right - 40, 20)

    def draw(self):
        super().draw()
        score = settings_stats.stat['score']
        text_surface = self.font.render(str(score), True, "#ffffff")
        text_rect = text_surface.get_rect()
        text_rect.right = self.rect.left - 5
        text_rect.centery = self.rect.centery
        self.master.blit(text_surface, text_rect)



