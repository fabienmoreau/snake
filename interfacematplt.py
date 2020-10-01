import matplotlib.pyplot as plt
import time
import pygame

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

edge = 1
width = 10
length = 15
X=[0,2]
Y=[15,11]
i=15

class Interfacematplt:

    def __init__(self, width, length):
        self.axis = plt.axis([0,width, 0, length])

    def clear_dots(self):
        plt.clf()
    
    def refresh(self, snake, game, speed):
        
        X_snake=[]
        Y_snake=[]
        for square in snake.body:
            X_snake.append(square[0])
            Y_snake.append(square[1])
        X_ball = [game.new_ball[0]]
        Y_ball = [game.new_ball[1]]
        plt.plot(X_snake, Y_snake,'s', color='black', markersize=30)
        plt.plot(X_ball, Y_ball,'s', color='red', markersize=30)
        plt.axis([0,15, 0, 20])
        
        plt.draw()
        speed=0.0009*speed
        plt.pause(speed)
        

"""
while i>0: 
    plt.clf()
    plt.plot(X, Y,'s', color='black', markersize=30)
    plt.axis([0,width, 0, length])

    plt.draw()
    plt.pause(1)
    print(Y)
    Y[0]+= -1
    i+= -1
"""
