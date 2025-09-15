import pygame, os
import settings_stats

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HEART_IMG = os.path.join(BASE_DIR, "img", "hearts.png")

class Hearts:

    def __init__(self, master):
        self.master = master
        self.master_rect = self.master.get_rect()
        self.image = pygame.image.load(HEART_IMG)
        self.rect = self.image.get_rect()
        self.rect.x = self.master_rect.left + 20
        self.rect.y = self.master_rect.top + 20
        self.font = pygame.font.Font(None, 34)

    def draw(self):
        self.master.blit(self.image, self.rect)
        if self.__class__.__name__ == "Hearts":
            hearts = settings_stats.stat['heart']
            text_surface = self.font.render(str(hearts), True, "#ffffff")
            text_rect = text_surface.get_rect(center = self.rect.center)
            self.master.blit(text_surface, (text_rect.x - 1, text_rect.y - 2))





