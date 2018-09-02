from pygame.locals import *
import pygame, sys, random

class Auto(pygame.sprite.Sprite):
	def __init__(self, x, y, horientacion=1, estado=True):
		pygame.sprite.Sprite.__init__(self)
		self.sprs = (('sprites/abajo.png', 'sprites/arriba.png', 'sprites/izquierda.png', 'sprites/derecha.png'),('sprites/RAbajo.png', 'sprites/RArriba.png', 'sprites/RIzquierda.png', 'sprites/Rderecha.png'))
		self.horientacion = horientacion
		self.auto = pygame.image.load(self.sprs[random.randrange(2)][self.horientacion])
		self.rect = self.auto.get_rect()
		self.estado = estado 
		self.rect.centerx = x
		self.rect.centery = y
		self.movimiento = self.movi()

	def movi(self):
		if self.horientacion == 1:
			def direccion():
				self.rect.centery -= 10
				if self.rect.centery == -100:
					self.rect.centery = 750
		elif self.horientacion == 2:
			def direccion():
				self.rect.centerx -= 10
				if self.rect.centerx == -100:
					self.rect.centerx = 750
		elif self.horientacion == 3:
			def direccion():
				self.rect.centerx += 10
				if self.rect.centerx == 750:
					self.rect.centerx = -10
		elif self.horientacion == 0:
			def direccion():
				self.rect.centery +=10
				if self.rect.centery == 750:
					self.rect.centery = -10
		return direccion
		
	def run(self):
		self.movimiento()

	def paint(self, window):
		window.blit(self.auto, self.rect)

