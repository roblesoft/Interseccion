from pygame.locals import *
import pygame, sys
class Semaforo(pygame.sprite.Sprite):
	def __init__(self, x, y, window, horientacion=1, estado=0):
		pygame.sprite.Sprite.__init__(self)
		self.sprs = (('sprites/semaforo_horizontal.png', 'sprites/semaforo_horizontal2.png', 'sprites/semaforo_horizontal3.png'), ('sprites/semaforo_vertical1.png', 'sprites/semaforo_vertical2.png', 'sprites/semaforo_vertical3.png')) 
		self.horientacion = horientacion
		self.estado = estado 
		self.semaforo = pygame.image.load(self.sprs[self.horientacion][self.estado])
		self.rect = self.semaforo.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.window = window

	def run(self):
		self.paint()

	def paint(self):
		self.window.blit(self.semaforo, self.rect)

