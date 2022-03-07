
#------------------------
#import library
#------------------------
import pygame

#-----------------------
#initialisation

#-----------------------
pygame.init()

screen = pygame.display.set_mode([500,500])
circle_pos = (250, 250)
circle_pos2 = (150, 150)
#variables
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
                circle_pos = (circle_pos[0]-10,circle_pos[1])
            if event.key == pygame.K_RIGHT:
                circle_pos = (circle_pos[0]+10,circle_pos[1])
            if event.key == pygame.K_UP:
                circle_pos = (circle_pos[0],circle_pos[1]-10)
            if event.key == pygame.K_DOWN:
                circle_pos = (circle_pos[0],circle_pos[1]+10)
                
                
    #------------------
    #update
    #------------------
    
    #Draw
    #Fill background
    #-------------------
    screen.fill((25, 245, 255))
    pygame.draw.circle(screen, (20, 255, 180), (circle_pos), 75)
    pygame.display.flip()
            
pygame.quit()


