import pygame
import os

_image_library = {}
def get_image(path, convert=False, convert_alpha=False):
  global _image_library
  image = _image_library.get(path)
  if image == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    if convert != False: image = pygame.image.load(canonicalized_path).convert()
    elif convert_alpha != False: image = pygame.image.load(canonicalized_path).convert_alpha()
    else: image = pygame.image.load(canonicalized_path)
    _image_library[path] = image
  return image

def detectCollisions(x1, y1, w1, h1, x2, y2, w2, h2):
  if x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2: return 1
  elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2: return 2
  elif x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2: return 3
  elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2: return 4
  else: return 0
