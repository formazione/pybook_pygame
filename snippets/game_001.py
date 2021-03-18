import pygame, sys
from pygame.locals import *


class Game():
	"Start window"
	def init(self):
		"Initialize pygame"
		pygame.init()
	
	def set_screen(self):
		"Screen width and height and title"
		DISPLAYSURF = pygame.display.set_mode((400, 300))
		pygame.display.set_caption('Hello World!')

	def mainloop(self):
		"Game loop"
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
					pygame.display.update()
	
	def main_sequence(self):
		"Program flow chart"
		self.init()
		self.set_screen()
		self.mainloop()


game = Game()
game.main_sequence()