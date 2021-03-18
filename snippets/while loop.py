import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((400, 400))


def close_game(event, game_on):
    "We're closing this game"
    QUIT = event.type == pygame.QUIT
    ESCAPE = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
    if QUIT or ESCAPE:
        game_on = False
    return game_on


def exit():
        pygame.quit()
        sys.exit()


game_on = True
# self.background(ORANGE)
while game_on:
    for event in pygame.event.get():
        game_on = close_game(event, game_on)
    # self.user_interactions(event)
    # self.show_player()
    pygame.display.update()
exit()












