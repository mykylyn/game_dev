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
player = pygame.Rect(0,0,50,50)
player_vel_x = 0
player_vel_y = 0

block = pygame.Rect(200,200,400,25)

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

    # update velocity based on pressed keys
    if keys[pygame.K_w]:
        player_vel_y -= 1
    if keys[pygame.K_s]:
        player_vel_y += 1
    if keys[pygame.K_d]:
        player_vel_x += 1
    if keys[pygame.K_a]:
        player_vel_x -= 1

    # update position based on velocity
    player.x += round(player_vel_x)    
    player.y += round(player_vel_y)

    if (player.colliderect(block)):
        print("colliding")

    # dampen (slowly decrease) velocity
    player_vel_x *= 0.9
    player_vel_y *= 0.9

    # clears everything that was on screen
    screen.fill("grey")

    # draws a rectangle according to the Rect object repersenting the player
    pygame.draw.rect(screen, "red", player)
    pygame.draw.rect(screen, "black", block)

    # flip() updates the display to show everything that has been drawn
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
