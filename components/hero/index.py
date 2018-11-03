import pygame
from utils.index import *

class Hero:
  def __init__(self, screen, x, y):
    self.screen = screen
    self.x = x
    self.y = y
    self.width = 47
    self.height = 57
    # self.next = callback
    self.create()
    surface = pygame.display.get_surface()
    self.surfaceWidth = surface.get_width()
    
    self.speed = 0.0
    self.side = False

  def config(self, side):
    if self.side != side: 
      self.side = side
      self.speed = 0.0
    if self.speed > -3 and self.speed < 3:
      if self.side == 'left': self.speed -= 0.1
      if self.side == 'right': self.speed += 0.1

  def draw(self, events):
    found = False
    for event in events:
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
          self.side = False
          found = True
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT: 
          self.config('left')
          found = True
        elif event.key == pygame.K_RIGHT: 
          self.config('right')
          found = True

    if found == False and self.side != False: self.config(self.side)
    if self.side == False:
      if self.speed < 0.1 and self.speed > -0.1: self.speed = 0
      else: self.speed = self.speed * 0.9

    if self.x + self.speed > 0 and self.x + self.speed < self.surfaceWidth:
      self.x += self.speed

    self.screen.blit(self.hero, (self.x - self.width * 0.5, self.y - self.height))

  def create(self):
    self.hero = get_image('assets/images/logo.png')

  def getPosition(self):
    return self.x, self.y
    
  def getHeight(self):
    return self.height
    