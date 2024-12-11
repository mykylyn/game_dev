import pygame

# init MUST be included before pygame can do anything
pygame.init()

# creates a window that's 1280 pixels wide and 720 pixels tall
# display.setmode takes in a parameter of a tuple.
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
# file path: "placeholder sprite.png"
icon = pygame.image.load('placeholder sprite.png')

running = True

x = 0
y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        x+=2
    if keys[pygame.K_a]:
        x-=2
    
    if keys[pygame.K_s]:
        y+=2
    if keys[pygame.K_w]:
        y-=2
    
    #fills the screen with grey, everything before it is "erased"
    screen.fill("grey")

    #draw a circle
   # pygame.draw.circle(screen, "red", (x, y), 20)

    #draw a circle
    pygame.draw.circle(screen, "blue", (400, 200), 50)
    screen.blit(icon,(x,y))
    pygame.display.flip()    

    clock.tick(60)

pygame.quit()
