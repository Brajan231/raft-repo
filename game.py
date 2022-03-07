
#------------------------
#import library
#------------------------
import pygame

#-----------------------
#initialisation

#-----------------------
pygame.init()

screen = pygame.display.set_mode([500,500])
playerrect = (250, 250)

#variables

playerimg = pygame.image.load('png/kenney_piratepack/PNG/Default size/Ships/ship (1).png')
playerimg.convert()
playerrect = playerimg.get_rect()
playerrect.center = 250, 250
#----------------------
running = True
#----------------------

#-----------------------
#loop
#-----------------------
while running:
    #-------------------
    #input
    #-------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerrect = (playerrect[0]-10,playerrect[1])
            if event.key == pygame.K_RIGHT:
                playerrect = (playerrect[0]+10,playerrect[1])
            if event.key == pygame.K_UP:
                playerrect = (playerrect[0],playerrect[1]-10)
            if event.key == pygame.K_DOWN:
                playerrect = (playerrect[0],playerrect[1]+10)
                
                
    #------------------
    #update
    #------------------
    
    #Draw
    #Fill background
    #-------------------
    screen.fill((25, 245, 255))
    screen.blit(playerimg, playerrect)
    pygame.display.flip()
    
pygame.quit()


