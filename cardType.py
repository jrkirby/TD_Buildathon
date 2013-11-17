'''
Created on Nov 16, 2013

@author: zeno
'''
import pygame
import towerType
class cardType:
    '''
    classdocs
    '''

    image = None
    imageName = []
    baseImage = "images/Card.png"
    isTower = False
    tType = None
    effects = []
    
    def __init__(self, typeOfCard, istower):
        '''
        Constructor
        Set up the images for each card and make it of a certain tower type        
        '''
        self.isTower = istower
        #if it's a tower, then it gets the tower type
        if(self.isTower == True):
            self.tType = typeOfCard
        self.imageName.append("Symbols/symbol_1.png")
        self.imageName.append("Symbols/symbol_2.png")
        self.imageName.append("Symbols/symbol_3.png")
        self.imageName.append("Symbols/symbol_4.png")
        self.imageName.append("Symbols/symbol_5.png")
        self.imageName.append("Symbols/symbol_6.png")
        self.imageName.append("Symbols/symbol_7.png")
        self.imageName.append("Symbols/symbol_8.png")
        self.imageName.append("Symbols/symbol_9.png")
        self.imageName.append("Symbols/symbol_10.png")
        self.imageName.append("Symbols/symbol_11.png")
        self.imageName.append("Symbols/symbol_12.png")
        self.imageName.append("Symbols/symbol_13.png")
        self.imageName.append("Symbols/symbol_14.png")
        self.imageName.append("Symbols/symbol_15.png")
        self.imageName.append("Symbols/symbol_16.png")
        self.imageName.append("Symbols/symbol_17.png")
        self.imageName.append("Symbols/symbol_18.png")
        self.imageName.append("Symbols/symbol_19.png")
        self.imageName.append("Symbols/symbol_20.png")
        self.imageName.append("Symbols/symbol_21.png")        
        
    
    def draw(self, surface, x, y):
        if(self.tType != None):
            self.image = pygame.image.load(self.imageName[self.tType]).convert()
            surface.blit(self.image, (x + 20 , y + 15))      
