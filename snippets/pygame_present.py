import pygame
import sys


'''
big_screeb_code
	palette         definition the colors used in the game 24.1.2021


'''

text_for_slides = """
La Costituzione
legge fondamentale dello Stato
al vertice del sistema legislativo
2 giugno 1946
Vince la Repubblica sulla monarchia
Suffragio universale
Votano le donne per la prima volta
Sud: vince la monarchia
Nord: vince la Repubblica
Prevale la il voto alla Repubblica
è composta da 139 articoli
1-12 principi fondamentali""".splitlines()


class Game:
	def __init__(self, text):
		pygame.init()
		self.screen = pygame.display.set_mode((800, 500))
		self.clock = pygame.time.Clock()
		self.title_font_size = 64
		self.font_init(text)
		self.slides_counter = 0
		self.mainloop()

	def mainloop(self):
		"This runs until you quit or escape"
		self.game = 1 # bool that if 1 the game goes on
		while self.game:
			for event in pygame.event.get():
				self.game = self.check_exit(event) # quit or escape
				self.keypressed(event)
			# self.update_screen()
			pygame.display.update()
			self.clock.tick(60)
		self.quit() # exit from the game

	def update_screen(self):
		self.screen.blit(self.title_surface, (30, 50))
		# self.fx_title_grow()

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

	def keypressed(self, event):
		"Makes the slides go on with right, back with left"
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				self.screen.fill((0, 0, 0))
				if self.slides_counter < len(text_for_slides) - 1:
					self.slides_counter += 1
					print("RIGHT")
			if event.key == pygame.K_LEFT:
				if self.slides_counter > 0:
					self.slides_counter -= 1
				self.screen.fill((0, 0, 0))
			self.font_init(text_for_slides[self.slides_counter])


	def font_init(self, text):
		self.text = text
		self.title_font = pygame.font.SysFont("Arial", self.title_font_size)
		if len(self.text.split()) < 3:
			self.title_surface = self.title_font.render(self.text, 0, (255, 255, 255))
		if len(self.text.split()) < 6:
			t1 = " ".join(self.text.split()[:3])
			t2 = " ".join(self.text.split()[3:])
			self.title_surface = pygame.Surface((800, 300))
			self.t1 = self.title_font.render(t1, 0, (255, 255, 255))
			self.title_surface.blit(self.t1, (0, 0))
			self.t2 = self.title_font.render(t2, 0, (255, 255, 255))
			self.title_surface.blit(self.t2, (0, 70))
		
		self.screen.blit(self.title_surface, (30, 50))


	def fx_title_grow(self):
		"FX: the title grows"
		if self.title_font_size < 100:
			if self.title_font_size % 3 == 0:
				self.title_surface = self.title_font.render(self.text, 0, pygame.Color("Coral"))
			else:
				self.title_surface = self.title_font.render(self.text, 0, pygame.Color("Black"))

			self.title_font_size += 5
			self.title_font = pygame.font.SysFont("Arial", self.title_font_size)
			# self.font_init()
		else:
			self.title_surface = self.title_font.render(self.text, 0, pygame.Color("White"))



Game("Hello World")


