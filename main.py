"""
main.py - The entry point into the game. This runs the main game loop.
"""

import pygame
import sys
import gamemap
import os
import gamedata
import userinterface
import enemymanager
import build_deck
import menu

"""
The dimensions for the screen. These should remain constant.
"""
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 700

"""
The max number of frames per second for the game.
"""
MAX_FPS = 60

"""
The game clock
"""
GameClock = None

"""
The title of the game. This should remain constant.
"""
TITLE = "Defensive Design"

"""
This performs initial setup of the game. Any global variables
should also be defined here (yes, I know most people say global
variables are bad, but there really isn't a simple solution).
"""
def setup():
   
    # Set the title of the game.
    pygame.display.set_caption(TITLE)
    # Set up a new window.
    global ScreenSurface
    ScreenSurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    pygame.font.init()
    
    # Set up the map
    global Map
    Map = gamemap.GameMap("map1", ScreenSurface)
    # Set up the starting game data
    global Data
    Data = gamedata.GameData()
    # Set up the UI
    global UI
    UI = userinterface.UserInterface()
    # Initialize the enemy manager
    global EnemyManager
    EnemyManager = enemymanager.EnemyManager(Map.getTileSize())
    global GameClock
    GameClock = pygame.time.Clock()
    #We start at a menu
    global GameState
    GameState = "MENU"
    global Menu
    Menu = menu.Menu()
    global BuildDeck
    BuildDeck = build_deck.BuildDeck()

"""
This handles a single pygame event.
"""
def handleEvent(event):
    global GameState
    if(event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
        handleKeyEvent(event)
    if event.type == pygame.QUIT:
        # Quit the program safely
        pygame.quit()
        sys.exit()
    if(event.type == pygame.MOUSEBUTTONDOWN):
        if(GameState == "MENU"):
            GameState = "BUILD_DECK"
        if(GameState == "BUILD_DECK"):
            BuildDeck.click(pygame.mouse.get_pos())
        if(GameState == "GAME"):

            x, y = pygame.mouse.get_pos()
            card_x = int(math.floor(SCREEN_WIDTH / CARD_ARRAY_SIZE))
            card_y = int(math.floor(SCREEN_HEIGHT / CARD_ARRAY_SIZE))
            card_x = x / card_x
            mouse_c = pygame.image.load("images/card.png").convert()
            print(card_x)
            print("\n")
        #screen.blit(mouse_c, (x, y))
        #deck[card_x].cType.image
    else:
        if(GameState == "GAME"):
            EnemyManager.spawnEnemy(event, Map.getStartingTile())

"""
This is the main game loop, called as many times as
the computer allows.
"""
def main():
    while(1):
        #Handle the event queue
        event = pygame.event.poll()
        # The event queue returns an event of type NOEVENT if the queue is empty
        while(event.type != pygame.NOEVENT):
            handleEvent(event)
            event = pygame.event.poll()
        # Delete anything already on the surface.
        ScreenSurface.fill((0, 0, 0))
        update() # Update the game objects
        draw() # Draw all the game objects
        pygame.display.flip()

        # Maintain the max frame rate
        GameClock.tick(MAX_FPS)
       

"""
Handles any updating of game objects. This is called
once per game loop.
"""
def update():
    global GameState
    if(GameState == "GAME"):
        # Update the enemies
        livesLost = EnemyManager.update(Map)
        Data.lives -= livesLost
        # Update the UI
        UI.update(Data)
        # Check if the game is over
        if(Data.lives <= 0):
            GameState = "GAME_LOST" # The game is over
            UI.showDefeat()
       

"""
Draws all game objects to the screen. This is called once
per game loop.
"""
def draw():
    if(GameState == "MENU"):
        Menu.draw(ScreenSurface)
    elif(GameState == "BUILD_DECK"):
        BuildDeck.draw(ScreenSurface)
    elif(GameState == "GAME"):
        # Draw the map
        Map.draw(ScreenSurface)
        # Draw the enemies
        EnemyManager.draw(ScreenSurface)
        # Draw the UI
        UI.draw(ScreenSurface)
    

"""
Handles a single keyboard event (both key down and key up).
The event passed in is assumed to be a key event, or else
nothing happens.
"""
def handleKeyEvent(event):
    if(event.type == pygame.KEYDOWN):
        # If the escape key has been pressed, quit the game safely
        if(event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    else:
        if(event.type == pygame.KEYUP):
            return # TODO: Add stuff for key up events here

pygame.init()
setup()
main()
