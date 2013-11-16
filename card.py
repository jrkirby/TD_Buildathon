'''
Created on Nov 16, 2013

@author: zeno
'''
import cardType

class card:
    '''
    classdocs
    '''

    card_type = None
    images = []
    onScreen = False
    position = (-1, -1)
    
    
    def __init__(self, t):
        '''
        Constructor
        '''
        self.card_type = cardType(t)
        self.getImage    
    
    def draw(self, surface):
        if(self.onScreen == True):
            self.card_type.draw(surface, self.position)
    
        