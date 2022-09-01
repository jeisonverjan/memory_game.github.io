import pygame
import sys
from random import randint
import time

# Pygame start
pygame.init()

# Some variables to calculate the screen size
start_bottom_height = 50  
rectangle_size = 200
current_time = 0
time_counter = 0
rectangle = None
random_array = []
user_answer = []
correct = 1

# Board class
class Rectangle:
    def __init__(self):
        self.show = True
        self.showed = False
        self.object = pygame.Surface((rectangle_size, rectangle_size))

# Creating the board
rectangles = []
rect_int = []
for i in range(3):
    for j in range(3):
        rectangle = Rectangle()
        rect_int.append(rectangle)
    rectangles.append(rect_int)
    rect_int = []

# screen size
screen_width = 3 * rectangle_size
screen_height = (3 * rectangle_size) + start_bottom_height
start_bottom_width = screen_width

# Font set up
font_size = 20
font = pygame.font.SysFont("Arial", font_size)
x_font = int((start_bottom_width / 2) - (font_size / 2) - 30)
y_font = int(screen_height - start_bottom_height + 15)

# Creating start bottom
start_bottom = pygame.Rect(0, screen_height - start_bottom_height, start_bottom_width, screen_height)

# Screen init
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Memorey game!! - By Jverjan')

# Flags
play_available = True
play_running = False
user_response = False

def show_puzzle(correct):
    global rectangles
    global time_counter
    global rectangle
    global random_array
    for i in range(correct):
        array_int = []
        for j in range(2):
            array_int.append(randint(0, 2))
        random_array.append(array_int)

    for i in random_array:
         rectangle = rectangles[i[0]][i[1]]
         rectangle.show = False

    time_counter = pygame.time.get_ticks()
    print(random_array)
    print(user_answer)

def start_game():
    global play_running
    global user_response
    print('game started')
    show_puzzle(correct)
    play_running = True
    user_response = False

while True:
    for event in pygame.event.get():
        # Closing the game if the user press X bottom
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and play_available:
            y_absolute, x_absolute = event.pos
            x = x_absolute // rectangle_size
            y = y_absolute // rectangle_size
            if start_bottom.collidepoint(event.pos):
                if not play_running:                    
                    start_game()
            elif user_response:
                if len(random_array) > len(user_answer):
                    user_answer.append([x, y])
                else:
                    if random_array == user_answer:
                        print('Congratulation')
                        correct += 1
                        user_answer = []
                        random_array = []
                        start_game()
                    else:
                        print('You lost')
                        sys.exit()
            else:
                if not play_running:                                      
                    continue            

    current_time = pygame.time.get_ticks()
    for i in random_array:
        rectangle = rectangles[i[0]][i[1]]
        if time_counter > 0 and current_time - time_counter > 4000:
            rectangle.show = True
            user_response = True
 
    # Drawing the rectangles
    x_pos, y_pos = 0, 0
    for i in rectangles:
        x_pos = 0
        for element in i:
            if element.show:
                screen.blit(element.object, (x_pos, y_pos))
                element.object.fill('blue')
            if not element.show:
                if time_counter > 0 and current_time - time_counter > 2000:
                    screen.blit(element.object, (x_pos, y_pos))
                    element.object.fill('white')
            x_pos += rectangle_size            
        y_pos += rectangle_size
    
    # Drawing start bottom
    if play_running:
        pygame.draw.rect(screen, 'gray', start_bottom)
        screen.blit(font.render('Next', True, 'black'), (x_font, y_font))
    else:
        pygame.draw.rect(screen, 'green', start_bottom)
        screen.blit(font.render('Start Game', True, 'black'), (x_font, y_font))

    pygame.display.update()