import pygame
import sys
from random import randint
import time

# Pygame start
pygame.init()
clock = pygame.time.Clock()
#some variables to calculate the screen size
start_bottom_height = 50  
rectangle_size = 200
user_answer = []
cont_win = 1
seconds_wait = 2 
colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown', 'pink', 'aqua', 'yellow']
cont_color = 0
current_time = 0
buttom_press_time = 0
random_array = []

# 
class Rectangle:
    def __init__(self):
        self.show = True
        self.showed = False
        self.object = pygame.Surface((rectangle_size, rectangle_size))

#creating the rectangles
rectangles = []
rect_int = []
for i in range(3):
    for j in range(3):
        rectangle = Rectangle()
        rect_int.append(rectangle)
    rectangles.append(rect_int)
    rect_int = []

rectangle = [Rectangle()]

# screen size
screen_width = (len(rectangles[0]) * rectangle_size) * 2
screen_height = (len(rectangles) * rectangle_size) + start_bottom_height
start_bottom_width = screen_width // 2

# Font set up
font_size = 20
font = pygame.font.SysFont("Arial", font_size)
x_font = int((start_bottom_width / 2) - (font_size / 2) - 30)
y_font = int(screen_height - start_bottom_height + 15)

# Creating start bottom
start_bottom = pygame.Rect(0, screen_height - start_bottom_height, start_bottom_width, screen_height)

# Flags
play_available = True
play_active = False
user_response = True

# Screen init
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Memorey game!! - By Jverjan')

# Generate random array, this creates rectangles which the user needs to memorize
def create_random_array(cont_win):
    global random_array
    for i in range(cont_win):
        array_int = []
        for j in range(2):
            array_int.append(randint(0, 2))
        random_array.append(array_int)
    return random_array

def start_game():
    global buttom_press_time
    global rectangle
    global random_array
    random_array = create_random_array(2)
    ##array = [[0,1]]
    ##rectangle = rectangles[array[0][0]][array[0][1]]
    for i in random_array:
         rectangle = rectangles[i[0]][i[1]]
         rectangle.show = False
    buttom_press_time = pygame.time.get_ticks()
    #rectangle.show = False
    #print(rectangles[i[0]][i[1]])
    #rectangle.show = False

 

# Game loop
while True:
    for event in pygame.event.get():
        # Closing the game if the user press X bottom
        if event.type == pygame.QUIT:
            sys.exit()
        # If user clic and the game is avaiable
        elif event.type == pygame.MOUSEBUTTONDOWN and play_available:
            if start_bottom.collidepoint(event.pos):
                start_game()
                play_active = True               

            if play_active:
                y_pos, x_pos = event.pos
                x = x_pos // rectangle_size
                y = y_pos // rectangle_size
                if x >= len(rectangles[0]) or y >= len(rectangles):
                    continue                
            else:
                if not play_available:
                    continue
    
    
    
    current_time = pygame.time.get_ticks()
    for i in random_array:
        rectangle = rectangles[i[0]][i[1]]
        if buttom_press_time > 0 and current_time - buttom_press_time > 2000:
            #rectangle.show = True
            #rectangles[0][0].object.fill('black')
            rectangle.show = True
            print('hola mundo')
            random_array = []

    # Drawing the rectangles
    x_pos, y_pos = 0, 0
    for i in rectangles:
        x_pos = 0
        for element in i:
            if element.show:
                screen.blit(element.object, (x_pos, y_pos))
                element.object.fill('blue')
            if not element.show:
                screen.blit(element.object, (x_pos, y_pos))
                element.object.fill('white')
            x_pos += rectangle_size            
        y_pos += rectangle_size


    # Drawing start bottom
    if play_active:
        pygame.draw.rect(screen, 'gray', start_bottom)
        screen.blit(font.render('Next', True, 'white'), (x_font, y_font))
    else:
        pygame.draw.rect(screen, 'white', start_bottom)
        screen.blit(font.render('Start Game', True, 'black'), (x_font, y_font))
    
    pygame.display.update()
