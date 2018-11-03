import pygame
from utils.index import *
from constantes.index import *
from components.hero.index import *
from components.bomb.index import *

class Game:
  def __init__(self, screen, callback):
    self.screen = screen
    self.callback = callback
    self.hero = Hero(self.screen, WINDOW_WIDTH / 2, WINDOW_HEIGHT - 10)
    self.bomb = False
    self.heroHeight = self.hero.getHeight()
    x, y = self.getHeroPosition()
    self.keepBomb = Bomb(self.screen, x, y - self.heroHeight, self.bombMove)

  def bombMove(self, x, y):
    print(x, y)

  def draw(self, events):
    if self.bomb: 
      if self.bomb.isDestroy(): self.bomb = False
      else: self.bomb.draw(events)
    self.hero.draw(events)

  def getHeroPosition(self):
    return self.hero.getPosition()

  def fire(self):
    self.bomb = self.keepBomb
    x, y = self.hero.getPosition()
    self.bomb.setPosition(x, y)
    self.bomb.alive()
