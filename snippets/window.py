import pygame as pg


class Game:

	def __init__(self, w, h):
		"Initialize main surface (screen) and starting the loop"
		self.w = w
		self.h = h
		self.size = w, h
		self.screen = pg.display.set_mode(self.size)
		self.loop()

	def close_window(self, event, game):
		"Close the window with the x button or Esc"
		quit = event.type == pg.QUIT
		escape = event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
		if quit or escape:
			game = 0
		return game

	def loop(self):
		"The loop that make the game go on"
		game = 1
		while game:
			for event in pg.event.get():
				game = self.close_window(event, game)
		pg.quit()


game = Game(400, 400)
