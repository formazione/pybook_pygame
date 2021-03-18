'''framerate indipendence


1) find time between frames (delta_time)
'''
import time

fr = 60 # frame rate
now = time.time
before = now()
def dt():
	"Tells you how much time passed\
	 from the last time you called this\
	 func"
	global before

	diff = now() - before
	print(diff * fr)
	before = now()

dt()
