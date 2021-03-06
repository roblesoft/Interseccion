import pygame, threading, sys
from semaforo import Semaforo
from Auto import Auto
from pygame.locals import * 

pygame.init()
pygame.display.set_caption("interseccion")
window = pygame.display.set_mode((700, 700))

auto = Auto(0, 270, window,  horientacion=3)
auto2 = Auto(650, 420, window,  horientacion=2)
auto3 = Auto(280, 0, window,  horientacion=0)
auto4 = Auto(430, 0, window,  horientacion=1)

semaforo = Semaforo(200, 345, window, estado=1) 
semaforo3 = Semaforo(495, 345, window, estado=1) 
semaforo5 = Semaforo(345, 205, window, horientacion=0) 
semaforo7 = Semaforo(345, 495, window, horientacion=0) 

def simulation():
	while True:
		window.fill((0, 0, 0))
		window.blit(pygame.image.load('sprites/interseccion.png'), (0, 0))
		auto.run()
		if semaforo.estado == 0 and auto.rect.centerx > 200 and auto.rect.centerx < 300:
			print("hello")
		else: 
			auto2.run()
		auto3.run()
		auto4.run()
		semaforo.cambios()
		semaforo.run()
		semaforo3.cambios()
		semaforo3.run()
		semaforo5.cambios()
		semaforo5.run()
		semaforo7.cambios()
		semaforo7.run()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()
if __name__ == '__main__':
	simulation()
