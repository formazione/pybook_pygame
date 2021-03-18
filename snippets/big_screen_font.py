import pygame
import sys


'''
big_screeb_code
	palette         definition the colors used in the game 24.1.2021


'''


class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((0, 0))
		self.clock = pygame.time.Clock()
		self.title_font_size = 32
		self.font_init()
		self.mainloop()

	def mainloop(self):
		"This runs until you quit or escape"
		self.game = 1 # bool that if 1 the game goes on
		while self.game:
			for event in pygame.event.get():
				self.game = self.check_exit(event) # quit or escape
			self.update_screen()
			pygame.display.update()
			self.clock.tick(60)
		self.quit() # exit from the game

	def update_screen(self):
		self.screen.blit(self.title_surface, (0, 0))
		self.fx_title_grow()


	def quit(self):
		"Exit from the game"
		pygame.quit()
		sys.exit()

	def check_exit(self, event):
		"Check if user presses quit or escape"
		quit = event.type == pygame.QUIT
		exit = event.type == pygame.KEYDOWN  and event.key == pygame.K_ESCAPE
		if quit or exit:
			self.game = 0
		return self.game

	def font_init(self):
		try:
			self.title_font = pygame.font.SysFont("Arial", self.title_font_size)
			# this is a surface
			self.title_surface = self.title_font.render("ARKANOID", 0, WHITE)
		except:
			print("Something's wrong with fonts")
			pass

	def fx_title_grow(self):
		"FX: the title grows"
		if self.title_font_size < 100:
			if self.title_font_size % 3 == 0:
				self.title_surface = self.title_font.render("ARKANOID", 0, pygame.Color("Coral"))
			else:
				self.title_surface = self.title_font.render("ARKANOID", 0, pygame.Color("Black"))

			self.title_font_size += 5
			self.title_font = pygame.font.SysFont("Arial", self.title_font_size)
			# self.font_init()
		else:
			self.title_surface = self.title_font.render("ARKANOID", 0, pygame.Color("White"))



Game()



