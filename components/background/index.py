import pygame
from utils.index import *
from constantes.index import *

class Background:
  def __init__(self, screen):
    self.screen = screen
    self.create()

    self.width, self.height = self.image.get_size()
    self.halfHeight = self.height * 0.5

    self.x = -(self.width - WINDOW_WIDTH) * 0.5
    self.y = -self.halfHeight

  def calculateLeftDelta(self, x):
    return -(x - (WINDOW_WIDTH * 0.5)) / 10

  def draw(self, events, hero):
    left = self.calculateLeftDelta(hero.getPosition()[0])
    self.y += BACKGROUND_SPEED
    if self.y > 0: self.y = -self.halfHeight
    self.screen.blit(self.image, (self.x + left, self.y))

  def create(self):
    self.image = get_image(BACKGROUND_IMG, convert=True)
