import pygame
from utils.index import *
from constantes.index import *

class Bomb:
  def __init__(self, screen, x, y, callback):
    self.screen = screen
    self.create()
    self.width, self.height = self.bomb.get_size()
    self.x = x - self.width * 0.5
    self.y = y - self.height
    self.callback = callback
    self.speed = BOMB_DEFAULT_SPEED
    self.destroy = False
    self.enemy = False

  def draw(self, events):
    self.speed = self.speed * BOMB_INCREASE_SPEED
    self.y -= self.speed
    self.screen.blit(self.bomb, (self.x, self.y))

    if self.y < -self.height:
      self.destroy = True
      self.speed = BOMB_DEFAULT_SPEED
    self.callback(self.x, self.y)

    if self.enemy:
      x, y, w, h = self.enemy.getRect()
      if detectCollisions(self.x, self.y, self.width, self.height, x, y, w, h): print('kill enemy')

  def create(self):
    self.bomb = get_image(BOMB_IMG, convert_alpha=True)

  def isDestroy(self):
    return self.destroy

  def alive(self):
    self.destroy = False

  def getPosition(self):
    return self.x, self.y

  def setPosition(self, x, y):
    self.x = x - self.width * 0.5
    self.y = y - self.height

  def setEnemy(self, enemy):
    self.enemy = enemy
