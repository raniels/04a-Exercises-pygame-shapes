#!/usr/bin/env python
'''

For this exercise, draw randomly-sized, randomly-colored, rectangles in random locations on the screen
It might be helpful to define a list of colors you want to use
hint: where you place the screen.fill(black) will affect whether or not the squares persist on the screen

'''
import sys, pygame, random
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

screen_size = (800,600)
FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()



    while True:
        clock.tick(FPS)

        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        width = random.randint(0, 600)
        height = random.randint(0, 800)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        pygame.draw.rect(screen, color, (x, y, width, height))
        pygame.display.flip()


if __name__ == '__main__':
    main()