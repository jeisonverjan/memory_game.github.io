import pygame
import sys
import random

# Pygame start
pygame.init()

#some variables to calculate the screen size
start_bottom_height = 50  
rectangle_size = 200
user_answer = [] 

#creating the rectangles
colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown', 'pink', 'aqua', 'yellow']
random.shuffle(colors)
rectangles = []
rect_int = []
cont = 0
for i in range(3):
    for j in range(3):
        rectangle = pygame.Surface((rectangle_size, rectangle_size))
        rectangle.fill(colors[cont])
        cont += 1
        rect_int.append(rectangle)
    rectangles.append(rect_int)
    rect_int = []

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

# Screen init
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Memorey game!! - By Jverjan')

# Generate random array, this is gonna create the rectangle that the user needs to memorize
random_array = [[0, 0], [2,2]]


# Game loop
while True:
    for event in pygame.event.get():
        # Closing the game if the user press X bottom
        if event.type == pygame.QUIT:
            sys.exit()
        # If user clic and the game is avaiable
        elif event.type == pygame.MOUSEBUTTONDOWN and play_available:
            if start_bottom.collidepoint(event.pos):
                play_active = True
            if play_active:
            #getting mouser location
                pygame.time.wait(1000)
                rectangles[0][0].fill('black')
                pygame.time.wait(5000)
                rectangles[2][2].fill('black')
                x_pos, y_pos = event.pos
                if x_pos // rectangle_size >= len(rectangles[0]) or y_pos // rectangle_size >= len(rectangles):
                    continue
                user_answer.append([x_pos//rectangle_size, y_pos//rectangle_size])
                if user_answer == random_array:
                    print('Perfect!!')
                print(user_answer)
        else:
            if not play_available:
                continue
    
    # Drawing the rectangles
    x_pos, y_pos = 0, 0
    for i in rectangles:
        for element in i:
            screen.blit(element, (x_pos, y_pos))
            x_pos += rectangle_size
        y_pos += rectangle_size
        x_pos = 0

    # Drawing start bottom
    if play_active:
        pygame.draw.rect(screen, 'gray', start_bottom)
        screen.blit(font.render('Start Game', True, 'white'), (x_font, y_font))
    else:
        pygame.draw.rect(screen, 'white', start_bottom)
        screen.blit(font.render('Start Game', True, 'black'), (x_font, y_font))
    
    pygame.display.update()