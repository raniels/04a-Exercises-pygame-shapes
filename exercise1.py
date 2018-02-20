#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first two lines for you as an example


'''
import sys, pygame	# imports the sys and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

screen_size = (800,600) #variable represetning screen resolution
FPS = 60 #variable representing FPS

def main(): #creates main function
	pygame.init() # line that needs to be put in order for pygame to work
	screen = pygame.display.set_mode(screen_size) #sets screen rest
	clock = pygame.time.Clock() #starts a clock

	while True: # sets a loop taht will run until chagned to False
		clock.tick(FPS) # sets fps
		screen.fill((0,0,0)) #black background

		for event in pygame.event.get(): # for each event that runs
			if event.type == pygame.QUIT: # check to see if quit is the current event
				pygame.quit() # ends pygame
				sys.exit(0) # endds program

		pygame.display.flip() # lets program display an image all at once

if __name__ == '__main__': #makes sure it doesnt run without being called if its am odule
	main() #runs main