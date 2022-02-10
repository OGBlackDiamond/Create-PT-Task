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
    #Draw the player on the screen with its attributes
    def draw(self):
        WIN.blit(self.player_image, (self.playerx, self.playery))
        if self.shot:
            pygame.draw.rect(WIN, (255, 0, 0), self.bullet)
    #Allow for the player to move about the screen within reason.
    def movement(self, hit_wall = False):
        #If the player is hitting a barrier, dont allow them to move
        if self.hit_wall == False:
            #Free player movement
            if keys_pressed[pygame.K_RIGHT]:
                self.playerx += 5
            elif keys_pressed[pygame.K_LEFT]:
                self.playerx -= 5
            elif keys_pressed[pygame.K_UP]:
                self.playery -= 5
            elif keys_pressed[pygame.K_DOWN]:
                self.playery += 5
        #Contains the player within a set box on the screen by checking its position
        self.hit_wall = True
        if self.playerx <= 0:
            self.playerx += 5
        elif self.playerx >= 290:
            self.playerx -= 5
        elif self.playery <= 350:
            self.playery += 5
        elif self.playery >= 418:
            self.playery -= 5
        else:
            self.hit_wall = False
    #Allow the player to shoot bullets
    def shoot(self, shot = False):
        self.bullet = pygame.Rect(self.playerx / 2, self.playery / 2, 30, 60)
        if keys_pressed[pygame.K_RSHIFT]:
            self.shot = True
        if self.shot:
            self.bullet.x += 7
        else:
            self.bullet.x = self.playerx / 2
            self.bullet.y = self.playerx / 2
#End of class definition  


        
        
#Defining an enemy class so we can make more than one very easily
class Enemy:
    #Initializing the class variables
    def __init__(self, x, y):
        #Setting variables for the player
        self.enemyx, self.enemyy = x, y
        self.enemy_sizex, self.enemy_sizey = 30, 32
        self.hurtbox = pygame.Rect(self.enemyx, self.enemyy, self.enemy_sizex, self.enemy_sizey)
        #Getting the enemy (alien) image
        #All credit to the image used goes to:
        #https://supersmashbros.fandom.com/wiki/Boss_Galaga
        self.raw_enemy_image = pygame.image.load(os.path.join("Images", "Galaga Enemy.png"))
        self.enemy_image = pygame.transform.scale(self.raw_enemy_image, (self.enemy_sizex, self.enemy_sizey))
    #Drawing the enemy on the screen
    def draw(self):
        if self.hit == False:
            WIN.blit(self.enemy_image, (self.enemyx, self.enemyy))
    #Telling if the enemy has been hit
    def hurtbox_detection(self):
        if pygame.Rect.colliderect(player1.bullet, self.hurtbox):
            self.hit = True

#End of class definition

#Class instance definition
player1 = Player() 
#List containing all of the enemies on the screen, this can be appended and removed based
#On the actions being taken by the user
enemies = [Enemy(145, 150), Enemy(105, 150), Enemy(185, 150)]

#Function to allow the enemies to move across the screen in an orderly fashion
def enemy_movement():
    #Making the row of enemies bounce from each side of the screen
    if enemies[0].enemyx <= 0:
        movement_unitx = 3
        movement_unity = 1
    elif enemies[enemies.len()] >= 480:
        movement_unitx = -3
        movement_unity = 1
    #Loop to move all of the enemies by the movement unit
    for i in range(enemies.len()):
        enemies[i].enemyx += movement_unitx
        enemies[i].enemyy += movement_unity
        movement_unity = 0

#Draws all of the necessary elements on the screen
def draw():
    WIN.blit(BACKGROUND, (0, 0))
    player1.draw()
    #For loop to draw all of the enemies in the 'enemies' list on the screen
    for i in range(len(enemies)):
        enemies[i].draw()


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
    player1.movement()

    #Lets the code stop running when the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

#END OF LINE