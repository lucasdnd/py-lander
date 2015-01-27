import pygame
from pygame.locals import *
from lander import Lander

class App:

  def __init__(self):

    self._running = True
    self.screen = None
    self.size = self.weight, self.height = 640, 400

  #
  # Game setup
  #
  def on_init(self):

    pygame.init()
    self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    self._running = True
    pygame.display.set_caption("py-lander")

    # Create our Lander
    self.lander = Lander()

  #
  # Process input
  #
  def on_event(self, event):
    if event.type == pygame.QUIT:
      self._running = False

  #
  # Main game logic
  #
  def on_loop(self):
    pass

  #
  # Render
  #
  def on_render(self):
    self.lander.on_render(self.screen);
    pygame.display.flip()

  #
  # Ends the game
  #
  def on_cleanup(self):
    pygame.quit()

  #
  # Starts the game
  #
  def on_execute(self):
    if self.on_init() == False:
      self._running = False

    while(self._running):
      for event in pygame.event.get():
        self.on_event(event)
      self.on_loop()
      self.on_render()
    self.on_cleanup()

if __name__ == "__main__":
  theApp = App()
  theApp.on_execute()