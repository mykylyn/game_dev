import pygame

# init MUST be included before pygame can do anything
pygame.init()

# creates a window that's 1280 pixels wide and 720 pixels tall
# display.setmode takes in a parameter of a tuple.
screen = pygame.display.set_mode((1280, 720))
# creates a clock that keeps track of time for us
clock = pygame.time.Clock()
running = True

# we want these outside of the loop, since we don't want to reset them every frame
x = 0
y = 0

# all code within the while loop is run over and over as long as running is true
while running:
    # iterates through every new event since the last time get() was called
    for event in pygame.event.get():
        # if one of those events is QUIT, set running to false
        if event.type == pygame.QUIT:
            running = False

    # keys is a list of 1s and 0s
    # if a key is pressed, it's position in the list will be a 1
    keys = pygame.key.get_pressed()
    # print(keys)

    # update position based on pressed keys
    if keys[pygame.K_w]:
        y -= 5
    if keys[pygame.K_s]:
        y += 5
    if keys[pygame.K_d]:
        x += 5
    if keys[pygame.K_a]:
        x -= 5

    # clears everything that was on screen
    screen.fill("grey")
    # draws a circle on the screen that's "red" at (x,y) with radius 50
    pygame.draw.circle(screen, "red", (x,y), 50)

    # flip() updates the display to show everything that has been drawn
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
