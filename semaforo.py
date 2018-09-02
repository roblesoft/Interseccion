from pygame.locals import *
import pygame, sys
class Semaforo(pygame.sprite.Sprite):
	def __init__(self, x, y, horientacion='v', estado=True ):
		pygame.sprite.Sprite.__init__(self)
		self.semaforo = pygame.imamge.load("")
		self.horientacion = horientacion
		self.x = x
		self.y = y
		self.estado = estado

	def run(self):
		pass


	def paint(self, window):
		window.blit(self.semaforo, self.rect)

