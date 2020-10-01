import pygame
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
edge = 40

class Square:
    def __init__(self, xpos, ypos, color):
        self.edge = edge
        self.xpos = xpos*self.edge
        self.ypos = ypos*self.edge
        self.rect = pygame.Rect((xpos, ypos), (xpos+edge, ypos+edge))
        self.image = pygame.Surface((edge, edge))
        self.image .fill(color)  
        
