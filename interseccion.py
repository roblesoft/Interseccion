import pygame, threading, time, sys
from semaforo import Semaforo
from Auto import Auto
from pygame.locals import * 

pygame.init()
pygame.display.set_caption("interseccion")
window = pygame.display.set_mode((700, 700))


auto = Auto(0, 270, horientacion=3)
auto2 = Auto(650, 420, horientacion=2)

def simulation():
	while True:
		window.fill((0, 0, 0))
		window.blit(pygame.image.load('sprites/interseccion.png'), (0, 0))
		auto.paint(window)
		auto.run()
		if auto.rect.centerx == 750:
			auto.rect.centerx = 0
		auto2.paint(window)
		auto2.run()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()
if __name__ == '__main__':
	simulation()
