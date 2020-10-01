from interfacematplt import Interfacematplt
import pygame
import random
from square import Square
from snake import Snake
from interfacepy import InterfacePy
import msvcrt

width = 600
length = 800
edge = 40
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

speed = 200

pygame.init()

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

    def change_direction(self, event):

        if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

            if event.key == pygame.K_DOWN and self.direction != 'UP':
                game.direction = 'DOWN'
            elif event.key == pygame.K_UP and self.direction != 'DOWN':
                game.direction = 'UP'
            elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                game.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                game.direction = 'RIGHT'

            if self.playing == False:
                self.get_started()


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
    a=1
    snake = Snake(15,20)
    game = Game(15,20,snake)
    
    if a==1:
        interface = InterfacePy(600,800,40)

    if a==2:
        interface = Interfacematplt(15,20)

    while True:

        if a==1:
            interface.screen.fill(black)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                elif event.type == pygame.KEYDOWN:
                    
                    game.change_direction(event)

        if a==2:
            input_char = msvcrt.getch()
            if str(input_char.upper())[2] == 'A': 
                print('YES')
                game.direction = 'RIGHT'
                if game.playing == False:
                    game.get_started()
            interface.clear_dots()

        
        
                
        if game.playing == True and (pygame.time.get_ticks()-game.time > speed):

            game.time = pygame.time.get_ticks()
            snake.set_new_position(game)

            if game.new_ball == snake.body[0]:
                game.add_ball_to_snake(snake)

            game.is_it_over(snake)
            

        if a==1:
            interface.refresh(snake, game)

        if a==2:
            interface.refresh(snake, game, speed)

        

        