import pygame
import random
from utils.index import *
from constantes.index import *

class Enemy:
  def __init__(self, screen):
    self.screen = screen
    self.create()
    self.width, self.height = self.image.get_size()
    self.halfHeight = self.height * 0.5
    self.x = (WINDOW_WIDTH * 0.5) - (self.width * 0.5)
    self.y = self.halfHeight
    self.setDirection()

  def setDirection(self):
    self.directionHorizontal = (-ENEMY_SPEED, ENEMY_SPEED)[bool(random.getrandbits(1))]
    self.directionVertical = (-ENEMY_SPEED, ENEMY_SPEED)[bool(random.getrandbits(1))]
  
  def draw(self, events):
    self.x += self.directionHorizontal
    self.y += self.directionVertical
    if self.x <= 0 or self.x + self.width >= WINDOW_WIDTH: self.directionHorizontal = self.directionHorizontal * -1
    if self.y <= 0 or self.y + self.height >= WINDOW_HEIGHT: self.directionVertical = self.directionVertical * -1
    self.screen.blit(self.image, (self.x, self.y))

  def create(self):
    self.image = get_image(ENEMY_IMG, convert_alpha=True)

  def getRect(self):
    return (self.x, self.y, self.width, self.height)
