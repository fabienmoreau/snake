import pygame
import random
from square import Square
edge = 40

class Snake:

    def __init__(self, width, length):
        self.body = list()
        square_xpos = 1+int(random.random() * (width-2))
        square_ypos = 1+int(random.random() * (length-2))
        self.body.append((square_xpos,square_ypos))
        self.last_pos = (square_xpos,square_ypos)

    def set_new_position(self, game):

        new_pos = self.body[0]

        if game.direction == 'DOWN':
            self.body[0] = (self.body[0][0], self.body[0][1] + 1)

        if game.direction == 'UP':
            self.body[0] = (self.body[0][0], self.body[0][1] - 1)

        if game.direction == 'LEFT':
            self.body[0] = (self.body[0][0] - 1, self.body[0][1])

        if game.direction == 'RIGHT':
            self.body[0] = (self.body[0][0] + 1, self.body[0][1])

        if len(self.body) > 1:
            for i in range(1, len(self.body)):
                self.last_pos = self.body[i]
                self.body[i] = new_pos
                new_pos = self.last_pos
        else:
            self.last_pos = new_pos