import pygame
from utils.index import *

class Bomb:
  def __init__(self, screen, x, y, callback):
    self.screen = screen
    self.width = 29
    self.height = 46
    self.x = x - self.width * 0.5
    self.y = y - self.height
    self.callback = callback
    # self.next = callback
    self.create()
    self.speed = 0.1
    self.destroy = False

  def draw(self, events):
    self.speed = self.speed * 1.1
    self.y -= self.speed
    print(self.y, self.speed)
    self.screen.blit(self.bomb, (self.x, self.y))

    if self.y < -self.height: self.destroy = True
    self.callback(self.x, self.y)

  def create(self):
    self.bomb = get_image('assets/images/bomb.png')

  def isDestroy(self):
    return self.destroy

  def alive(self):
    self.destroy = False

  def getPosition(self):
    return self.x, self.y

  def setPosition(self, x, y):
    return self.x, self.y
