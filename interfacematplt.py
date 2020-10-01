import matplotlib.pyplot as plt
import time
import pygame
import msvcrt

class InterfaceMatPlt:

    def __init__(self, width, length, markersize):
        self.width = width
        self.length = length
        self.markersize = markersize
        self.axis = plt.axis([0,width, 0, length])

    def change_direction(self, game):
        input_char = msvcrt.getch()
        if str(input_char.upper())[2] == 'Z': 
            game.direction = 'DOWN'
        if str(input_char.upper())[2] == 'S': 
            game.direction = 'UP'
        if str(input_char.upper())[2] == 'Q': 
            game.direction = 'LEFT'
        if str(input_char.upper())[2] == 'D': 
            game.direction = 'RIGHT'

    def refresh(self, snake, game, speed):
        plt.clf()
        X_snake=[]
        Y_snake=[]
        for square in snake.body:
            X_snake.append(square[0])
            Y_snake.append(square[1])
        X_ball = [game.new_ball[0]]
        Y_ball = [game.new_ball[1]]
        plt.plot(X_snake, Y_snake,'s', color='black', markersize=self.markersize)
        plt.plot(X_ball, Y_ball,'s', color='red', markersize=self.markersize)
        plt.axis([0,self.width, 0, self.length])
        
        plt.draw()
        speed=0.0001*speed
        plt.pause(speed)
        

