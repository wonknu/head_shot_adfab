import pygame
from constantes.index import *
from components.heart.index import *

class Life:
  def __init__(self, screen, callback):
    self.screen = screen
    self.callback = callback
    self.kills = 0
    self.create()

  def draw(self):
    for heart in self.hearts:
      heart.draw()

  def create(self):
    self.hearts = []
    for item in range(HEART_COUNT - self.kills):
      self.hearts.append(Heart(self.screen, (WINDOW_WIDTH - 40) + (item * 13), 10))

  def hurts(self):
    self.kills += 1
    if self.kills == 3: self.callback()
    self.create()
