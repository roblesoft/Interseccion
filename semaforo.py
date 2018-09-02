from pygame.locals import *
import pygame, sys, time
class Semaforo(pygame.sprite.Sprite):
	def __init__(self, x, y, window, horientacion=1, estado=0):
		pygame.sprite.Sprite.__init__(self)
		self.sprs = (('sprites/semaforo_horizontal.png', 'sprites/semaforo_horizontal2.png', 'sprites/semaforo_horizontal3.png'), ('sprites/semaforo_vertical1.png', 'sprites/semaforo_vertical2.png', 'sprites/semaforo_vertical3.png')) 
		self.horientacion = horientacion
		self.estado = estado 
		self.semaforo = pygame.image.load(self.sprs[self.horientacion][self.estado])
		self.rect = self.semaforo.get_rect()
		self.x = x
		self.y = y
		self.rect.centerx = x
		self.rect.centery = y
		self.window = window
		if self.estado == 1:
			self.i = 69
		else:
			self.i = 0

	def cambios(self):
		self.i += 1
		if self.i == 40:
			self.semaforo = pygame.image.load(self.sprs[self.horientacion][1])
		if self.i == 70:
			self.estado = 0
			self.semaforo = pygame.image.load(self.sprs[self.horientacion][2])
		if self.i == 140:
			self.semaforo = pygame.image.load(self.sprs[self.horientacion][0])
			self.i = 0	
			self.estado = 1

	
	def run(self):
		self.paint()

	def paint(self):
		self.window.blit(self.semaforo, self.rect)

