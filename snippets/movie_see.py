import moviepy
from moviepy.editor import *
import pygame


clip = VideoFileClip('pygame4.mp4').resize((600, 400))
clip.preview()

pygame.quit()