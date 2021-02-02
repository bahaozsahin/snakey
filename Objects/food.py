import random
import pygame
from Helpers.constants import Screen_Constants

class apple(object):

    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomise_position()
    
    def randomise_position(self):
        self.position = (random.randint(0, Screen_Constants.GRID_WIDTH -1) * Screen_Constants.GRID_SIZE, 
        random.randint(0, Screen_Constants.GRID_HEIGHT - 1) * Screen_Constants.GRID_SIZE)
    
    def draw (self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (Screen_Constants.GRID_SIZE, Screen_Constants.GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)
