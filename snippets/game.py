# This is imported by game.py
# pygame_book 3: added background color and control mouse click - 2.1.2020
import pygame as pg
import time
from voice import Voice


ORANGE = (255, 128, 0)
speak = Voice.speak.Speak
class Game:

	def __init__(self, w, h):
		"Initialize main surface (screen) and starting the loop"
		self.window_size(w, h)
		self.player = self.load_image("man1", 100, 50)
		self.player_speak = self.load_image("man1b", 100, 50)
		self.current_frame = self.player
		self.main_surface()
		self.counter = 0
		self.loop()

	def window_size(self, w, h):
		"Define the width and height of the window"
		self.width = w
		self.height = h
		self.size = self.width, self.height

	def main_surface(self):
		"Creates the main surface of the screen"
		self.screen = pg.display.set_mode(self.size)

	def close_window(self, event, game_on):
		"Close the window with the x button or Esc"
		quit = event.type == pg.QUIT
		escape = event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
		if quit or escape:
			game_on = 0
		return game_on

	def user_interactions(self, event):
		"Checks for the mouse input"
		mousedown = event.type == pg.MOUSEBUTTONDOWN
		
		if mousedown:
			self.do_player_speak()
		else:
			self.do_player_mute()

	def do_player_speak(self):
		"Make visible the image that speaks"
		self.current_frame = self.player_speak
		speak("Ciao")

	def do_player_mute(self):
		"Make visible the image that does not speak"
		self.current_frame = self.player
	
	def background(self, color):
		"Gives the screen a color"
		self.screen.fill(color)

	def load_image(self, name, x, y):
		"image 14x64"
		self.image = pg.image.load(f"imgs/{name}.png")
		self.player_x = x
		self.player_y= y
		return self.image

	def show_player(self):
		"Show player on the screen"
		self.screen.blit(
			self.current_frame,
			(self.player_x, self.player_y))

	def loop(self):
		"The loop that make the game go on"
		game_on = 1
		self.background(ORANGE)
		while game_on:
			for event in pg.event.get():
				game_on = self.close_window(event, game_on)
				self.user_interactions(event)
			self.show_player()

			pg.display.update()
		pg.quit()


time.sleep(3)
if __name__ == "__main__":
    game = Game(50*14, 7*64)
speak("Come stai?")






