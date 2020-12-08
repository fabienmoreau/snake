from interfacematplt import InterfaceMatPlt
import matplotlib.pyplot as plt
import pygame
import random
from snake import Snake
from interfacepy import InterfacePy
import msvcrt
import sys

#GAME PARAMETERS
markersize = 10
width = 20
length = 20
speed = 300

#COLORS 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
grey = (200,200,200)

class Game:

    def __init__(self, width, length,snake):
        self.width = width
        self.length = length
        self.playing = False
        self.time = int()
        self.direction = ''
        self.new_ball = (0,0)
        self.grid = []
        for i in range(1,width-1):
            for j in range(1,length-1):
                self.grid.append((i,j))
        self.get_new_ball(snake)

    def get_started(self):
        self.playing = True

    def set_time(self):
        self.time = pygame.time.get_ticks()

    def get_new_ball(self, snake):
        self.new_ball = random.choice(list(set(self.grid)-set(snake.body)))
    
    def add_ball_to_snake(self, snake):
        snake.body.append(snake.last_pos)
        game.get_new_ball(snake)

    def is_it_over(self, snake):
        if snake.body[0][0]<1 or snake.body[0][0]>self.width-2 or snake.body[0][1]<1 or snake.body[0][1]>self.length-2:
            quit()

        if len(snake.body)>1:
            for i in range(1, len(snake.body)):
                if snake.body[0] == snake.body[i]:
                    quit()

    def game_over(self, snake):
        self.playing == False



if __name__ == '__main__':

    snake = Snake(width,length)
    game = Game(width,length,snake)
    param = str(sys.argv[1])
    pygame.init()

    if param == 'pygame':
        pix_edge = 40
        pix_width = width*pix_edge
        pix_length = length*pix_edge
        interface = InterfacePy(pix_width,pix_length,pix_edge, grey, red)

    if param == 'matpltlib':
        interface = InterfaceMatPlt(width,length, markersize)

    while True:
        if param == 'pygame':
            interface.screen.fill(black)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if game.playing == False:
                        game.get_started() 
                    interface.change_direction(event, game)
            
        if param == 'matpltlib' and msvcrt.kbhit() == True:
            if game.playing == False:
                game.get_started()
            interface.change_direction(game)
            
        if game.playing == True and (pygame.time.get_ticks()-game.time > speed):

            game.time = pygame.time.get_ticks()
            snake.set_new_position(game)

            if game.new_ball == snake.body[0]:
                game.add_ball_to_snake(snake)

            game.is_it_over(snake)
            

        if param == 'pygame':
            interface.refresh(snake, game)

        if param == 'matpltlib':
            interface.refresh(snake, game, speed)

        

        