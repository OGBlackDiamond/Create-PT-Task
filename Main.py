#Basic Imports for the game to run correctly
#Pete Shinners (2011). PyGame - Python Game Development
#http://www.pygame.org
import pygame
import sys  
import os
from pygame import K_RSHIFT, draw
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
        self.shot = False
        self.hit_wall = False
        self.lives = 3
        self.playerx, self.playery = 145, 400
        self.player_sizex, self.player_sizey = 30, 32
        self.hurtbox = pygame.Rect(self.playerx, self.playery, self.player_sizex, self.player_sizey)
        self.bullet = pygame.Rect(self.playerx + 13, self.playery, 3, 30)
        #Getting the player (spaceship) image
        #All credit to the image used goes to:
        #https://galaxian.fandom.com/wiki/Gyaraga
        self.raw_player_image = pygame.image.load(os.path.join("Images", "Galaga Ship.png"))
        self.player_image = pygame.transform.scale(self.raw_player_image, (self.player_sizex, self.player_sizey))
    #Draw the player on the screen with its attributes
    def draw(self):
        if self.shot:
            pygame.draw.rect(WIN, (255, 0, 0), player1.bullet)
        WIN.blit(self.player_image, (self.playerx, self.playery))
    #Allow for the player to move about the screen within reason.
    def movement(self):
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
    def shoot(self):
        #Shoots the bullet
        while self.shot:
            self.bullet.y -= 12

        #Resets the bullet
        if self.shot == False:
            self.bullet.x = self.playerx
            self.bullet.y = self.playery

    #Allow the player to lose a life when the enemies touch the player or the end of the screen
    #def lose_life(self):

        
#End of class definition  


        
        
#Defining an enemy class so we can make more than one very easily
class Enemy:
    #Initializing the class variables
    def __init__(self, x, y = 150):
        #Setting variables for the enemy
        self.hit = False
        self.hit_end = False
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
        if pygame.Rect.colliderect(player1.bullet, self.hurtbox) or pygame.Rect.colliderect(player1.hurtbox, self.hurtbox):
            self.hit = True
            player1.shot = False
        if self.enemyy + 32 == HEIGHT:
            self.hit_end == True

#End of class definition

#Class instance definition
player1 = Player() 
#List containing all of the enemies on the screen, this can be appended and removed based
#On the actions being taken by the user
enemies = [Enemy(145, 150), Enemy(105, 150), Enemy(185, 150)]

#Function to allow the enemies to move across the screen in an orderly fashion
def enemy_movement():
    movement_unitx, movement_unity = 0, 0
    #Making the row of enemies bounce from each side of the screen
    if enemies[0].enemyx <= 0:
        movement_unitx = 3
    elif enemies[len(enemies) - 1].enemyx >= 480:
        movement_unitx = -3
    elif enemies[round(len(enemies) / 2)] == 138:
        movement_unity = 32
    #Loop to move all of the enemies by the movement unit
    for i in range(len(enemies)):
        enemies[i].enemyx += movement_unitx
        enemies[i].enemyy += movement_unity

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
    enemy_movement()
    player1.movement()
    if keys_pressed[K_RSHIFT]:
        player1.shot = True
    if player1.bullet.x <= 0:
        player1.shot = False
    player1.shoot()
    #This loop checks if the enemy has been hit by one of the player's bullets
    for i in range(len(enemies) - 1):
        enemies[i].hurtbox_detection()
        #Removing the enemy from the list, should it be hit
        if enemies[i].hit:
            player1.shot = False
            del enemies[i]

    #Lets the code stop running when the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

#END OF LINE