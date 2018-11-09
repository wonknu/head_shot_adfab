import pygame
from utils.index import *
from constantes.index import *
from components.ui.button.index import *

class End:
  def __init__(self, screen, callback):
    self.screen = screen
    self.callback = callback
    self.btnPlay = Button()

  def draw(self, events):
    for event in events:
      if event.type == MOUSEBUTTONDOWN:
        if self.btnPlay.pressed(pygame.mouse.get_pos()):
          self.callback(SCENE_GAME)
    
    # self, surface, color, x, y, length, height, width, text, text_color
    self.btnPlay.create_button(self.screen, (0,0,0), WINDOW_WIDTH * 0.5 - 50, WINDOW_HEIGHT * 0.5 - 35, 100, 30, 0, "Play again!", (255,255,255))
