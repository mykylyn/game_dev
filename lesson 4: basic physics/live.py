import pygame

# init MUST be included before pygame can do anything
pygame.init()

# creates a window that's 1280 pixels wide and 720 pixels tall
# display.setmode takes in a parameter of a tuple.
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# creates a clock that keeps track of time for us
clock = pygame.time.Clock()
running = True

# we want these outside of the loop, since we don't want to reset them every frame
player = pygame.Rect(0,0,50,50)
player_vel_x = 0
player_vel_y = 0

# grab a font from the system the code is running on
font = pygame.font.SysFont(None,48)
# render the text as an image so it can be blitted later
text = font.render("Score = ",True, 'Black')

# create a block at the center of the screen
block = pygame.Rect((WIDTH - 400)/2, (HEIGHT - 400)/2,400,400)

# number collision just got replaced with number score and isn't used anymore lmao
number_collision = 0
number_score = 0


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
        player_vel_y -= 1
    if keys[pygame.K_s]:
        player_vel_y += 1
    if keys[pygame.K_d]:
        player_vel_x += 1
    if keys[pygame.K_a]:
        player_vel_x -= 1
    
    # 9.8 m/s^s is a lot less than 9.8 pixels / frame^2!
    # about 0.4 is enough
    player_vel_y += 0.4

    # move the player in the x direction
    # (round so that small negative values don't keep the player moving by -1 pixels)
    player.x += round(player_vel_x)

    # use colliderrect to see if the player rect and the block rect
    if (player.colliderect(block)):
        if (player_vel_x > 0):
            # if the player is moving right...
            while (player.colliderect(block)):
                # ... move them left one pixel at a time until they're not in the block anymore
                player.x -= 1
        else:
            while (player.colliderect(block)):
                player.x += 1

        # tick the score up if we're touching the block
        number_score += 1

        print("Score is ", number_score)
        # rerender the text with the new number
        text = font.render("Score = " + str(number_score), True, 'Black')

    # move the player in the y direction
    # round for the same reason as x
    player.y += round(player_vel_y)

    # same logic as collsion in the x direction
    if (player.colliderect(block)):
        if (player_vel_y > 0):
            while (player.colliderect(block)):
                # set vel_y to 0 if the player hits the block from the top
                # (i.e. is on the ground)
                # otherwise gravity causes the player to continously build speed
                player_vel_y = 0
                player.y -= 1
        else:
            while (player.colliderect(block)):
                player.y += 1

        number_score += 1

        print("Score is ", number_score)
        text = font.render("Score = " + str(number_score), True, 'Black')

    # dampen the player's velocity so that it doesn't acclerate to absurd speeds
    player_vel_x *= 0.9
    # for verical motion, with gravity active, I perfer to just let the vel_y be though
    # player_vel_y *= 0.9

    # bounce off left side of the screen
    if (player.left <= 0):
        # force the player all the way back out
        player.left = 0
        # set the velocity to positive so it bounces
        player_vel_x = abs(player_vel_x) * 0.7
    
    # right side
    if (player.right >= WIDTH):
        player.right = WIDTH
        player_vel_x = -abs(player_vel_x) * 0.7
    
    # top side
    if (player.top <= 0):
        player.top = 0
        player_vel_y = abs(player_vel_y) * 0.7
    
    # bottom side
    if (player.bottom >= HEIGHT):
        player.bottom = HEIGHT
        player_vel_y = -abs(player_vel_y) * 0.7

    # clears everything that was on screen
    screen.fill("grey")

    # render player and block
    pygame.draw.rect(screen, "red", player)
    
    pygame.draw.rect(screen, "green", block) 

    # render text
    screen.blit(text, (1000,25))

    # flip() updates the display to show everything that has been drawn
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()