'''
Created on Nov 16, 2013

@author: zeno
'''
from cardType import cardType
import os
import pygame

"""
The size of the font to use in the user interface
"""
FONT_SIZE = 10

"""
The number of pixels of padding to use between the font
and the screen.
"""
FONT_PADDING = 10

"""
The color of the font (this is an RGB value)
"""
FONT_COLOR = (0, 0, 0)

"""
The color used for the background behind the font.
"""
FONT_BACKGROUND = (255, 255, 255)

"""
The number of pixels between two lines of text on the screen.
"""
FONT_LINESPACE = 4

class card:
    '''
    classdocs
    '''

    
    
    def __init__(self, ctype):
        '''
        Constructor
        '''
        self.ctype = ctype
        self.images = []
        self.images.append(pygame.image.load("images/Card.png"))
        self.position = (-1, -1)
        self.onScreen = False
    
    def draw(self, surface):
        self.font = pygame.font.Font(os.path.join("UI", "larabie.ttf"), FONT_SIZE, )
        surface.blit(self.images[0], (self.position[0], self.position[1]))    #base image
        
        # image = pygame.image.load(self.imageName[self.tType]).convert()
        # surface.blit(image, (self.position[0] + 20 , self.position[1] + 15))

    def click_on(self, x, y):
        return True
    
        
