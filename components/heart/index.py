import pygame
from utils.index import *
from constantes.index import *

class Heart:
  def __init__(self, screen, x, y):
    self.screen = screen
    self.x = x
    self.y = y
    self.create()
    self.width, self.height = self.image.get_size()

  def draw(self):
    self.screen.blit(self.image, (self.x, self.y))

  def create(self):
    self.image = get_image(HEART_IMG, convert_alpha=True)
