import pygame

pygame.init()

screen=pygame.display.set_mode((800, 400))

pygame.display.set_caption('Space Game')



test_font=pygame.font.Font('Pixeltype.ttf',69)

name= test_font.render("Space Game", False, "Blue")

#color = (0, 0, 255)

#screen.fill(color) 

while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              pygame.quit()
              exit()

    screen.blit(name,[100, 100])
    pygame.display.update()   
    pygame.display.flip()
