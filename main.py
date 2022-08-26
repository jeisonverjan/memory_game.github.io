from sys import exit
import pygame
import random

pygame.init()
WIDTH = 600
HEIGHT = 400
FTP = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Test your memory')
clock = pygame.time.Clock()

backgroud_surf = pygame.image.load('graphics/backgruund2.png').convert_alpha()


colors = ['blue', 'green', 'red', 'orange', 'purple', 'gray', 'pink', 'aqua', 'yellow']
cont = 0
squares = []
squares_int = []
for i in range(3):
    for j in range(3):
        square_surf = pygame.Surface((60, 60))
        square_surf.fill(colors[cont])
        cont += 1
        squares_int.append(square_surf)
    squares.append(squares_int)
    squares_int = []

random.shuffle(squares)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #draw all our elementes
    #update everything
    screen.blit(backgroud_surf, (0,0))

    for index, element in enumerate(squares[0]):
        element_rect = element.get_rect(topleft = (WIDTH//4 + (index+1) * 65 , 100))
        screen.blit(element, element_rect)
    
    for index, element in enumerate(squares[1]):
        element_rect = element.get_rect(topleft = (WIDTH//4 + (index+1) * 65 , 165))
        screen.blit(element, element_rect)
        #squares[1][index] = element_rect
        
    for index, element in enumerate(squares[2]):
        element_rect = element.get_rect(topleft = (WIDTH//4 + (index+1) * 65 , 230))
        screen.blit(element, element_rect)
        #squares[2][index] = element_rect
    
    #mouse_pos = pygame.mouse.get_pos()
    #if squares[0][0].collidepoint(mouse_pos):
       #print('collision')
        
    pygame.display.update()
    clock.tick(FTP)