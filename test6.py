import pygame
import sys
from random import randint

# Pygame start
pygame.init()

# Some variables to calculate the screen size
start_bottom_height = 50  
rectangle_size = 100

# Board class
class Rectangle:
    def __init__(self):
        self.show = True
        self.showed = False
        self.object = pygame.Surface((rectangle_size, rectangle_size))

# Creating the board
rectangles = []
rect_int = []
for i in range(5):
    for j in range(5):
        rectangle = Rectangle()
        rectangle.object.fill('blue')
        rect_int.append(rectangle)
    rectangles.append(rect_int)
    rect_int = []

# screen size
screen_width = len(rectangles[0]) * rectangle_size
screen_height = len(rectangles) * rectangle_size
start_bottom_width = screen_width

# Screen init
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Memorey game!! - By Jverjan')

rectangle = None
random_array = []
generate_rect = True
hide_rect = False
cont = 0
corrects = 0
user_answer = []
game_active = False


while True:
    pygame.time.Clock().tick(1)
    for event in pygame.event.get():
        # Closing the game if the user press X bottom
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            y_absolute, x_absolute = event.pos
            x = x_absolute // rectangle_size
            y = y_absolute // rectangle_size
            
            if game_active:
                print('write your answer')
                user_answer.append([x, y])
                if user_answer == random_array:
                    user_answer.clear()
                    corrects +=1
                    generate_rect = True            
            

    if hide_rect:
        rectangle.object.fill('blue')
        hide_rect = False
          
    if generate_rect:
        if len(random_array) <= corrects:
            sx, sy = randint(0, len(rectangles)-1), randint(0, len(rectangles[0])-1)
            random_array.append([sx,sy])
            print('random', random_array)
        else:
            if cont  < len(random_array):
                x = random_array[cont][0]
                y = random_array[cont][1]        
                rectangle = rectangles[x][y]
                rectangle.object.fill('black')
                rectangle.show = False
                cont += 1
                hide_rect = True
                rectangle.show = True
            else:
                cont = 0
                generate_rect = False
                game_active = True               
                
    # Drawing the rectangles
    x_pos, y_pos = 0, 0
    for i in rectangles:
        x_pos = 0
        for element in i:
            if element.show:
                screen.blit(element.object, (x_pos, y_pos))
                #element.object.fill('blue')
            if not element.show:
                screen.blit(element.object, (x_pos, y_pos))
                element.object.fill('white')
            x_pos += rectangle_size            
        y_pos += rectangle_size
    
    for i in range(5):
        pygame.draw.line(screen, 'black', (screen_width//5 *i,0), (screen_width//5 * i,screen_height))
        pygame.draw.line(screen, 'black', (0, screen_height//5 * i), (screen_width, screen_height//5 * i))

    pygame.display.update()