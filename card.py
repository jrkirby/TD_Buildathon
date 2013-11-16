'''
Created on Nov 16, 2013

@author: zeno
'''
import cardType

class card:
    '''
    classdocs
    '''

    cType = None
    images = []
    onScreen = False
    position_x = -1
    position_y = -1
    
    
    def __init__(self, typeOfCard, booleanWhetherIsTower):
        '''
        Constructor
        '''
        self.cType = cardType(typeOfCard, booleanWhetherIsTower)         
    
    def draw(self):
        if(self.onScreen == True):
            self.cType.draw()
            
    
        
