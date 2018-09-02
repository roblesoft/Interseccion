import pygame, threading, time, sys
from semaforo import Semaforo
from Auto import Auto
from pygame.locals import * 

pygame.init()
pygame.display.set_caption("interseccion")
window = pygame.display.set_mode((700, 700))


auto = Auto(0, 270, horientacion=3)
auto2 = Auto(650, 420, horientacion=2)
auto3 = Auto(280, 0, horientacion=0)
auto4 = Auto(430, 0, horientacion=1)

def simulation():
	while True:
		window.fill((0, 0, 0))
		window.blit(pygame.image.load('sprites/interseccion.png'), (0, 0))
		auto.paint(window)
		auto.run()
		auto2.paint(window)
		auto2.run()
		auto3.paint(window)
		auto3.run()
		auto4.paint(window)
		auto4.run()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()
if __name__ == '__main__':
	simulation()
