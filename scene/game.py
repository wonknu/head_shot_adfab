import pygame
from utils.index import *
from constantes.index import *
from components.hero.index import *
from components.bomb.index import *
from components.life.index import *
from components.enemy.index import *
from components.background.index import *

class Game:
  def __init__(self, screen, callback):
    self.screen = screen
    self.callback = callback
    self.life = Life(self.screen, self.onDie)
    self.hero = Hero(self.screen, WINDOW_WIDTH / 2, WINDOW_HEIGHT - 10, self.life.hurts)
    self.bomb = False
    self.heroHeight = self.hero.getHeight()
    x, y = self.getHeroPosition()
    self.keepBomb = Bomb(self.screen, x, y - self.heroHeight, self.bombMove)
    self.enemy = Enemy(self.screen)
    self.background = Background(self.screen)
    self.hero.setEnemy(self.enemy)

  def bombMove(self, x, y):
    x, y
    # print(x, y)

  def onDie(self):
    self.callback(SCENE_END)

  def draw(self, events):
    self.background.draw(events, self.hero)
    if self.bomb: 
      if self.bomb.isDestroy(): self.bomb = False
      else: self.bomb.draw(events)
    self.hero.draw(events)
    self.enemy.draw(events)
    self.life.draw()

  def getHeroPosition(self):
    return self.hero.getPosition()

  def fire(self):
    if self.bomb == False:
      self.bomb = self.keepBomb
      self.bomb.setEnemy(self.enemy)
      x, y = self.getHeroPosition()
      self.bomb.setPosition(x, y - self.heroHeight)
      self.bomb.alive()
