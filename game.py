import pygame
from utils.index import *
from components.screen.index import *
from constantes.index import *
from scene.intro import *
from scene.game import *

pygame.init()
window = Screen(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_COLOR)
done = False
clock = pygame.time.Clock()

def onSceneChange(nextScene):
  global currentScene
  currentScene = nextScene

onSceneChange(SCENE_INTRO)

scene = {}
scene[SCENE_INTRO] = Intro(window.screen, onSceneChange)
scene[SCENE_GAME] = Game(window.screen, onSceneChange)
# SCENE_END

while not done:
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE and currentScene == SCENE_GAME: scene[currentScene].fire()
      elif event.key == pygame.K_RETURN and currentScene == SCENE_INTRO: onSceneChange(SCENE_GAME)

  window.draw()
  scene[currentScene].draw(events)

  pygame.display.flip()
  clock.tick(60)
