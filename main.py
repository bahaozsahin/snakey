import pygame
from Game.Objects.snakey import snake
from Game.Helpers.constants import Screen_Constants
from Game.Objects import snakey
from Game.Objects import food

def main():
    pygame.init()

# Setting the clock and the screen mode
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Screen_Constants.SCREEN_WIDTH, Screen_Constants.SCREEN_HEIGHT), 0, 32)

# Creating the surface
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)
    snake = snakey.snake()
    apple = food.apple()
    myfont = pygame.font.SysFont("monospace", 16)
    score = 0

    while (True):
        clock.tick(10)
        snakey.snake.handle_keys()
        draw_grid(surface)
        #handle events
        snakey.snake.move()
        #if snake eat the food
        if snakey.snake.get_head_position() == food.apple.position:
            snakey.snake.length += 1
            score += 1
            food.apple.randomise_position()
        screen.blit(surface, (0, 0))
        score_text = myfont.render("Score {0}".format(score), 1 ,(0, 0, 0))
        screen.blit(score_text, (5, 10))
        pygame.display.update()


def draw_grid(surface):
        for y in range(Screen_Constants.GRID_HEIGHT):
            for x in range(Screen_Constants.GRID_WIDTH):
                if (x + y) % 2 == 0:
                    rectangles = pygame.Rect((x*Screen_Constants.GRID_SIZE, y*Screen_Constants.GRID_SIZE), (Screen_Constants.GRID_SIZE, Screen_Constants.GRID_SIZE))
                    pygame.draw.rect(surface, (93, 216, 228), rectangles)
                else:
                    rrectangles = pygame.Rect((x*Screen_Constants.GRID_SIZE, y*Screen_Constants.GRID_SIZE), (Screen_Constants.GRID_SIZE, Screen_Constants.GRID_SIZE))
                    pygame.draw.rect(surface, (84, 194, 205), rrectangles)

main()
