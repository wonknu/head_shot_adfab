import pygame
from utils.index import *
from constantes.index import *

class Hero:
  def __init__(self, screen, x, y, callback):
    self.screen = screen
    self.callback = callback
    self.x = x
    self.y = y
    self.create()
    self.width, self.height = self.hero.get_size()
    surface = pygame.display.get_surface()
    self.surfaceWidth = surface.get_width()
    self.isHurts = 0
    self.speed = HERO_DEFAULT_SPEED
    self.enemy = False
    self.side = False
    self.blink = False

  def config(self, side):
    if self.side != side: 
      self.side = side
      self.speed = HERO_DEFAULT_SPEED
    if self.speed > -HERO_MAX_SPEED and self.speed < HERO_MAX_SPEED:
      if self.side == HERO_LEFT_SIDE: self.speed -= HERO_INCREASE_SPEED
      if self.side == HERO_RIGHT_SIDE: self.speed += HERO_INCREASE_SPEED

  def draw(self, events):
    found = False
    for event in events:
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
          self.side = False
          found = True
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT: 
          self.config(HERO_LEFT_SIDE)
          found = True
        elif event.key == pygame.K_RIGHT: 
          self.config(HERO_RIGHT_SIDE)
          found = True

    if self.enemy:
      x, y, w, h = self.enemy.getRect()
      if detectCollisions(self.x, self.y, self.width, self.height, x, y, w, h) and self.isHurts == 0: 
        self.isHurts = 15
        self.callback()

    if found == False and self.side != False: self.config(self.side)
    if self.side == False:
      if self.speed < HERO_MIN_SPEED and self.speed > -HERO_MIN_SPEED: self.speed = HERO_DEFAULT_SPEED
      else: self.speed = self.speed * HERO_DELTA_SPEED

    if self.x + self.speed < -self.width: self.x = self.surfaceWidth - self.speed
    elif self.x + self.speed > self.surfaceWidth + self.width: self.x = self.speed
    else: self.x += self.speed

    hero = self.hero
    if self.side == HERO_LEFT_SIDE: hero = self.hero_left
    elif self.side == HERO_RIGHT_SIDE: hero = self.hero_right

    if self.isHurts > 0:
      if self.blink: self.isHurts -= 1
      else : self.blink = not self.blink
    if self.isHurts % 2 == 0 or self.isHurts == 0: self.screen.blit(hero, (self.x - self.width * 0.5, self.y - self.height))

  def create(self):
    self.hero = get_image(HERO_IMG, convert_alpha=True)
    self.hero_left = get_image(HERO_IMG_LEFT, convert_alpha=True)
    self.hero_right = get_image(HERO_IMG_RIGHT, convert_alpha=True)

  def getPosition(self):
    return self.x, self.y
    
  def getHeight(self):
    return self.height

  def setEnemy(self, enemy):
    self.enemy = enemy
