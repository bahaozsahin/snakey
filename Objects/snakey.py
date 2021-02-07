import random
import pygame
import sys
from Helpers.constants import Screen_Constants

class snake(object):
    def __init__(self):
        self.length = 1

        self.position = [((Screen_Constants.SCREEN_WIDTH/2), (Screen_Constants.SCREEN_HEIGHT/2))]

        self.direction = random.choice([Screen_Constants.UP,Screen_Constants.DOWN,
        Screen_Constants.LEFT, Screen_Constants.RIGHT])
        self.color = (17,24,47)

        self.score = 0

    def get_head_position(self):
        return self.position[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        current = self.get_head_position()
        x, y = self.direction
        new = (((current[0] + (x * Screen_Constants.GRID_SIZE)) % Screen_Constants.SCREEN_WIDTH),
        (current[1] + (y * Screen_Constants.GRID_SIZE)) % Screen_Constants.SCREEN_HEIGHT)

        if len(self.position) > 2 and new in self.position[2:]:
            # this is the self eating situation
            self.reset()
        else:
            # insert the head toward the new direction and pop the last element
            self.position.insert(0, new)
            if len(self.position) > self.length:
                self.position.pop()

    def reset(self):
        self.length = 1
        self.position = [(Screen_Constants.SCREEN_WIDTH/2),(Screen_Constants.SCREEN_HEIGHT/2)]
        self.direction = random.choice([Screen_Constants.UP,Screen_Constants.DOWN,
        Screen_Constants.LEFT, Screen_Constants.RIGHT])
        self.score = 0

    def draw(self, surface):
        for p in self.position:
            r = pygame.Rect((p[0], p[1]), (Screen_Constants.GRID_SIZE, Screen_Constants.GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            #pygame.draw.rect(surface, (93,216,228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(Screen_Constants.UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(Screen_Constants.DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(Screen_Constants.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(Screen_Constants.RIGHT)
