#Basic Imports for the game to run correctly
#Pete Shinners (2011). PyGame - Python Game Development
#http://www.pygame.org
import pygame
import sys  
import os
from pygame import draw
#Initializing the meathods for pygame
pygame.init()
#Setting the window title
pygame.display.set_caption("Create Task Entry")
#Defining and setting the window size
WIDTH, HEIGHT = 320, 450
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#Setting the speed (Frames Per Second) at which the app runs
FPS = 60
#Timer variable to keep track of the current FPS
timer = 0
############################################################
############################################################
############################################################
#Defining a player class such that its meathods can be used more easily
class Player:
    #Initializing the class variables
    def __init__(self):
        self.playerx, self.playery = 0, 0
        self.hurtbox = pygame.Rect(self.playerx, self.playery, 0, 0)
        
#Defining an enemy class so we can make more than one very easily
class Enemy:
    #Initializing the class variables
    def __init__(self):
        #Some code here
        self.bazinga = "beans"


#Making the game loop
while True:
    #Using the FPS variable to run the app
    clock = pygame.time.Clock()
    clock.tick(FPS)
    timer += 1
    if timer >= 60:
        timer = 0

    #Getting user input
    keys_pressed = pygame.key.get_pressed()


    #Lets the code stop running when the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()



