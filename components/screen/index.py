import pygame
import os

class Screen:
  def __init__(self, width ,height, color):
    self.width = width
    self.height = height
    self.color = color
    # delete later
    position = 1679 - int(width), 1049 - int(height)
    os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
    self.screen = pygame.display.set_mode((width, height))

  def draw(self):
    self.screen.fill(self.color)
