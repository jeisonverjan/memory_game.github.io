import pygame
from random import randint
from sys import exit

# Pygame start
pygame.init()

# Some variables to calculate the screen size
start_bottom_height = 50  
rectangle_size = 100
rectangles_number = 5

# Board class
class Rectangle:
    def __init__(self):
        self.show = True
        self.showed = False
        self.object = pygame.Surface((rectangle_size, rectangle_size))

# Creating the board
rectangles = []
rect_int = []
for i in range(rectangles_number):
    for j in range(rectangles_number):
        rectangle = Rectangle()
        rect_int.append(rectangle)
    rectangles.append(rect_int)
    rect_int = []

# screen size
screen_width = len(rectangles[0]) * rectangle_size
screen_height = len(rectangles) * rectangle_size + start_bottom_height
start_bottom_width = screen_width

# Screen init
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Memorey game!! - By Jverjan')

# Font set up
font_size = 20
font = pygame.font.SysFont("Arial", font_size)
x_font = int((start_bottom_width / 2) - (font_size / 2) - 30)
y_font = int(screen_height - start_bottom_height + 15)

# Creating start bottom
start_bottom = pygame.Rect(0, screen_height - start_bottom_height, start_bottom_width, screen_height)

def show_board(play_running):
    x_pos, y_pos = 0, 0
    for i in rectangles:
        x_pos = 0
        for element in i:
            if element.show:
                screen.blit(element.object, (x_pos, y_pos))
                element.object.fill('white')
            if not element.show:
                screen.blit(element.object, (x_pos, y_pos))
                element.object.fill('white')
            x_pos += rectangle_size            
        y_pos += rectangle_size
    
    for i in range(rectangles_number):
        pygame.draw.line(screen, 'black', (screen_width//rectangles_number *i,0), (screen_width//rectangles_number * i,(screen_height - start_bottom_height)))
        pygame.draw.line(screen, 'black', (0, (screen_height - start_bottom_height)//rectangles_number * i), (screen_width, (screen_height - start_bottom_height)//rectangles_number * i))

        # Drawing start bottom
    if play_running:
        pygame.draw.rect(screen, 'gray', start_bottom)
        screen.blit(font.render('', True, 'black'), (x_font, y_font))
    else:
        pygame.draw.rect(screen, 'green', start_bottom)
        screen.blit(font.render('Start Game', True, 'black'), (x_font, y_font))

# Flags
play_running = False
rectangle = None
random_array = []
generate_rect = False
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
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            y_absolute, x_absolute = event.pos
            x = x_absolute // rectangle_size
            y = y_absolute // rectangle_size
            if start_bottom.collidepoint(event.pos):
                play_running = True
                generate_rect = True
            if game_active:
                user_answer.append([x, y])
                if user_answer == random_array:
                    print('You win')
                    game_active = False
                    user_answer.clear()
                    corrects +=1
                    generate_rect = True
                else:
                    game_over = True               

    if hide_rect:
        rectangle.object.fill('White')
        hide_rect = False
          
    if generate_rect:
        if len(random_array) <= corrects:
            sx, sy = randint(0, len(rectangles)-1), randint(0, len(rectangles[0])-1)
            random_array.append([sx,sy])
        else:
            if cont  < len(random_array):
                x = random_array[cont][0]
                y = random_array[cont][1]        
                rectangle = rectangles[x][y]
                rectangle.object.fill('black')
                #rectangle.show = False
                cont += 1
                hide_rect = True
                #rectangle.show = True
            else:
                cont = 0
                generate_rect = False
                game_active = True             
    


    # Drawing the rectangles
    show_board(play_running)


    pygame.display.update()