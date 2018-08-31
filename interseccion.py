import pygame, threading, time, sys
from semaforo import Semaforo
from pygame.locals import * 

pygame.init()
pygame.display.set_caption("interseccion")
window = pygame.display.set_mode((700, 700))


def simulation():
	while True:
		window.fill((0, 0, 0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
if __name__ == '__main__':
	simulation()
