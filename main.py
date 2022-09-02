import pygame
from random import randint
from sys import exit

# Pygame start
pygame.init()

# Variables definition:
start_bottom_height = 50  
rectangle_size = 100
rectangles_number = 5 # To calculate the number of rectangles on the board (5*5)
corrects = 0 # increment if the user matched the pattern.
cont = 0 # counter for traversing the matrices
rectangle = None # object that represent a single rectangle on the board
random_array = [] # to generate a new pattern
user_answer = [] # to save the users clicks possition

# Flags to manage the times of the game
play_running = False
generate_rect = False
hide_rect = False
game_active = False
game_over = False

# Board class, this class represent the rectangles on the board
class Rectangle:
    def __init__(self):
        self.show = True
        self.showed = False
        self.object = pygame.Surface((rectangle_size, rectangle_size))

# Creating the board, create a matriz of the object Rectagle class
rectangles = []
rect_int = []
for i in range(rectangles_number):
    for j in range(rectangles_number):
        rectangle = Rectangle()
        rect_int.append(rectangle)
    rectangles.append(rect_int)
    rect_int = []

# Screen size
screen_width = len(rectangles[0]) * rectangle_size
screen_height = len(rectangles) * rectangle_size + start_bottom_height

# Screen init
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Memorey game!! - By Jverjan')

# Start Buttom set up
start_bottom_width = screen_width
font_size = 30
font = pygame.font.SysFont("Arial", font_size)
x_font = int((start_bottom_width / 2) - (font_size / 2) - 40)
y_font = int(screen_height - start_bottom_height + 10)

# Creating start bottom
start_bottom = pygame.Rect(0, screen_height - start_bottom_height, start_bottom_width, screen_height)

# This method paint the board
def show_board(play_running):
    # Drawing the rectangles
    x_pos, y_pos = 0, 0
    for i in rectangles:
        x_pos = 0
        for element in i:
            if element.show:
                screen.blit(element.object, (x_pos, y_pos))
                element.object.fill('#FFCC00')
            x_pos += rectangle_size            
        y_pos += rectangle_size
    
    # Drawing the lines
    for i in range(rectangles_number):
        pygame.draw.line(screen, 'black', (screen_width//rectangles_number *i,0), (screen_width//rectangles_number * i,(screen_height - start_bottom_height)))
        pygame.draw.line(screen, 'black', (0, (screen_height - start_bottom_height)//rectangles_number * i), (screen_width, (screen_height - start_bottom_height)//rectangles_number * i))

        # Drawing start bottom
    if play_running:
        pygame.draw.rect(screen, 'gray', start_bottom)
        screen.blit(font.render('', True, 'black'), (x_font, y_font))
    else:
        pygame.draw.rect(screen, '#CC0000', start_bottom)
        screen.blit(font.render('Start Game', True, 'black'), (x_font, y_font))

# This method create a new possition for random_array
def generate_array():
    global random_array
    global rectangles
    x = randint(0, len(rectangles[0])-1)
    y = randint(0, len(rectangles)-1)
    compare_array = [x, y]
    if len(random_array) > 0:
        # To avoid that the new possition be same as the last one.
        if compare_array != random_array[len(random_array) - 1]:
            random_array.append(compare_array)
        else:
            generate_array()
    else:
        random_array.append(compare_array)

# This method create and show a new pattern.
def game_functionality():
    global rectangle
    global generate_rect
    global game_active
    global hide_rect
    global random_array
    global cont

    if hide_rect:
        rectangle.object.fill('#FFCC00')
        hide_rect = False
          
    if generate_rect:
        if len(random_array) <= corrects:
            generate_array()
        else:
            if cont  < len(random_array):
                x = random_array[cont][0]
                y = random_array[cont][1]        
                rectangle = rectangles[x][y]
                rectangle.object.fill('black')
                cont += 1
                hide_rect = True
            else:
                cont = 0
                generate_rect = False
                game_active = True

# This method is trigger when the user fail.
def game_overs():
    global corrects
    game_over_text = pygame.font.SysFont("Arial", font_size)        
    game_over_text = game_over_text.render('Game Over, you catched: ' + str(corrects), True, 'black', '#CC0000')
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (screen_width//2, (screen_height- start_bottom_height)//2 )
    screen.blit(game_over_text, game_over_rect)      

while True:
    pygame.time.Clock().tick(1)
    for event in pygame.event.get():
        # Closing the game if the user press X bottom
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            y_absolute, x_absolute = event.pos
            x = x_absolute // rectangle_size
            y = y_absolute // rectangle_size
            # If start buttom is pressed the game start
            if start_bottom.collidepoint(event.pos):
                corrects = 0 # This is neccesary when the user wants to start a new game after fail
                play_running = True
                generate_rect = True
                game_over = False
            if game_active:
                # Ignore the click if it is offsaid of the rectangles
                if x < len(rectangles[0]) and y < len(rectangles):
                    user_answer.append([x, y]) # insert user click possition
                else:
                    continue
                # Checking if the user matched the pattern
                if user_answer == random_array:
                    game_active = False # to ignore clicks until a new patters be showed
                    user_answer.clear()
                    corrects +=1
                    generate_rect = True
                else:
                    if len(user_answer) == len(random_array):
                        # Game over response
                        game_over = True    
                        play_running = False
                        random_array.clear()
                        user_answer.clear()
                        generate_rect = False
       
    game_functionality()

    # Drawing the rectangles
    show_board(play_running)
    
    if game_over:
        game_overs()

    pygame.display.update()