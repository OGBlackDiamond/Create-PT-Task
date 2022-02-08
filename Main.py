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
#Gets the background image. I made it myself
BACKGROUND = pygame.image.load(os.path.join('Images', 'Background.png'))
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
        #Setting variables for the player
        self.playerx, self.playery = 145, 400
        self.player_sizex, self.player_sizey = 30, 32
        self.hurtbox = pygame.Rect(self.playerx, self.playery, self.player_sizex, self.player_sizey)
        #Getting the player (spaceship) image
        #All credit to the image used goes to:
        #https://galaxian.fandom.com/wiki/Gyaraga
        self.raw_player_image = pygame.image.load(os.path.join("Images", "Galaga Ship.png"))
        self.player_image = pygame.transform.scale(self.raw_player_image, (self.player_sizex, self.player_sizey))

    def draw(self):
        WIN.blit(self.player_image, (self.playerx, self.playery))

        
        
#Defining an enemy class so we can make more than one very easily
class Enemy:
    #Initializing the class variables
    def __init__(self):
        #Setting variables for the player
        self.enemyx, self.enemyy = 145, 150
        self.enemy_sizex, self.enemy_sizey = 30, 32
        self.hurtbox = pygame.Rect(self.enemyx, self.enemyy, self.enemy_sizex, self.enemy_sizey)
        #Getting the enemy (alien) image
        #All credit to the image used goes to:
        #https://supersmashbros.fandom.com/wiki/Boss_Galaga
        self.raw_enemy_image = pygame.image.load(os.path.join("Images", "Galaga Enemy.png"))
        self.enemy_image = pygame.transform.scale(self.raw_enemy_image, (self.enemy_sizex, self.enemy_sizey))

    def draw(self):
        WIN.blit(self.enemy_image, (self.enemyx, self.enemyy))

#Class instance definition
player1 = Player() 
enemies = [Enemy()]
#Draws all of the necessary elements on the screen
def draw():
    WIN.blit(BACKGROUND, (0, 0))
    player1.draw()
    enemies[0].draw()
    #Updates the screen
    pygame.display.update()  

#Making the game loop
while True:
    #Using the FPS variable to run the app
    clock = pygame.time.Clock()
    clock.tick(FPS)
    timer += 1
    if timer == 60:
        timer = 0


    #Getting user input
    keys_pressed = pygame.key.get_pressed()

    #Main game loop
    draw()

    #Lets the code stop running when the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()



