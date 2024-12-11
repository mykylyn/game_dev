import pygame

# init MUST be included before pygame can do anything
pygame.init()

# creates a window that's 1280 pixels wide and 720 pixels tall
# display.setmode takes in a parameter of a tuple.
screen = pygame.display.set_mode((1280, 720))

# while True keeps running forever
while True:
    # checks what is happening to the window (keyboard, clicking edges, other stuff you won't use)
    # your computer may think the window crashed if you don't check this
    pygame.event.get()
