import pygame

# init MUST be included before pygame can do anything
pygame.init()

# creates a window that's 1280 pixels wide and 720 pixels tall
# display.setmode takes in a parameter of a tuple.
screen = pygame.display.set_mode((1280, 720))
running = True

# all code within the while loop is run over and over as long as running is true
while running:
    # iterates through every new event since the last time get() was called
    for event in pygame.event.get():
        # if one of those events is QUIT, set running to false
        if event.type == pygame.QUIT:
            running = False

    # draws a circle on the screen that's "red" at (0,0) with radius 100
    pygame.draw.circle(screen, "red", (0,0), 100)

    # flip() updates the display to show everything that has been drawn
    pygame.display.flip()

pygame.quit()
