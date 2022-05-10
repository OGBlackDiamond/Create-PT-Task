##########################################################
##                    Create PT Task                    ##
##                   Galaga-Esque Game                  ##
##########################################################
##########################################################

#CONTROLS:
#Arrow keys to move, right shift to fire, ESC to exit the game

##########################################################
##########################################################


#Basic Imports for the game to run correctly
#Pete Shinners (2011). PyGame - Python Game Development
#http://www.pygame.org
import pygame
from pygame import K_RSHIFT, draw
import sys  
import os
#Initializing the meathods for pygame
pygame.init()
#Initializing the font for the score
pygame.font.init()
#Setting the window title
pygame.display.set_caption("Create Task Entry")
#Defining and setting the window size
WIDTH, HEIGHT = 320, 450
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#Gets the background picture, I made the image
BACKGROUND = pygame.image.load(os.path.join('Images', 'Background.png')) 
#Setting the speed (Frames Per Second) at which the app runs
FPS = 60
#Timer variable to keep track of the current FPS
timer = 0


############################################################
############################################################
############################################################

#Defining a player class such that its meathods can be used more easily with minimal confusion
class Player:
    #Initializing the class variables
    def __init__(self):
        #Setting variables for the player
        self.score = 0
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
    #Function to draw the player on the screen with its attributes
    def draw(self):
        if self.shot:
            pygame.draw.rect(WIN, (255, 0, 0), player1.bullet)
        WIN.blit(self.player_image, (self.playerx, self.playery))
    #Function to let the player to move about the screen within set constraints.
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

    #Funtion to allow the player to shoot bullets
    def shoot(self):
        #Shoots the bullet
        if self.shot:
            self.bullet.y -= 10

        #Resets the bullet
        if self.shot == False:
            self.bullet.x = self.playerx
            self.bullet.y = self.playery
 
#End of class definition  


        
        
#Defining an enemy class so I can make more than one very easily
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
    #Function to draw the enemy on the screen
    def draw(self):
        if self.hit == False:
            self.hurtbox = pygame.Rect(self.enemyx, self.enemyy, self.enemy_sizex, self.enemy_sizey)
            WIN.blit(self.enemy_image, (self.enemyx, self.enemyy))
    #Funtion to tell if the enemy has been hit
    def hurtbox_detection(self):
        if pygame.Rect.colliderect(player1.bullet, self.hurtbox) or pygame.Rect.colliderect(player1.hurtbox, self.hurtbox):
            self.hit = True
        if self.enemyy + 32 == HEIGHT - 200:
            self.hit_end == True

#End of class definition

#Class instance definitions
player1 = Player() 
#List containing all of the enemies on the screen, this can be appended and removed based on the actions being taken by the user
#Making a filler object, so the list can be looped through effectivley
filler_enemy = Enemy(-1000, -1000)
enemies = [Enemy(105, 150), Enemy(145, 150), Enemy(185, 150), filler_enemy]


#Variable to keep track of the levels that have passed
current_level = 3
#Function that generates a new rows of enemies when the previous one has been cleared
def new_level(level):
    global movement_unitx
    spacing_ammount = 50
    starting_pos = ((level /2) * spacing_ammount)
    movement_unitx = -1
    for i in range(level):
        if level >= 5:
            if i >= ((level / 2) - 1):
                enemies.insert(0, Enemy(((((WIDTH / 2) + starting_pos) + spacing_ammount) - (level * 25)), 110))
            else:
                enemies.insert(0, Enemy((((WIDTH / 2) + starting_pos) + spacing_ammount) - (level * 5)))
        else:
            enemies.insert(0, Enemy(((WIDTH / 2) + starting_pos) + spacing_ammount))
<<<<<<< Updated upstream
        spacing_ammount += 40

=======
        spacing_ammount += 30
>>>>>>> Stashed changes

#Setting the enemy movement variables
movement_unitx = -1
#Function to allow the enemies to move across the screen in an orderly fashion
def enemy_movement():
    global movement_unitx
    #Making the row of enemies bounce from each side of the screen
    for i in range(len(enemies)):
        if enemies[i].enemyx == 0:
            movement_unitx = 1
            for j in range(len(enemies)):
                enemies[j].enemyy += 32
        elif enemies[i].enemyx == WIDTH - 30:
            movement_unitx = -1
        #Loop to move all of the enemies by the movement unit
        enemies[i].enemyx += movement_unitx
            
#Function to draw all of the necessary elements on the screen
def draw():
    WIN.blit(BACKGROUND, (0, 0))
    player1.draw()
    draw_text("Level: " + str(current_level - 2), 30 , 0, 0)
    draw_text(("Score: " + str(player1.score)), 30, 0, 30)
    #For loop to draw all of the enemies in the 'enemies' list on the screen
    for i in range(len(enemies)):
        enemies[i].draw()
    #Updates the screen
    pygame.display.update()  

#Function to draw text
def draw_text(text, size, posx, posy):
    global text_display
    font = pygame.font.Font(None , size)
    text_display =font.render(text, True, (255, 255, 255))
    WIN.blit(text_display,(posx, posy))


#Main game loop that runs all of the commands and functions
while True:
    #Using the FPS variable to run the app
    clock = pygame.time.Clock()
    clock.tick(FPS)
    timer += 1
    if timer == 60:
        timer = 0


    #Getting user input
    keys_pressed = pygame.key.get_pressed()

    #Body of the program
    draw()
    enemy_movement()
    player1.movement()
    #Checking if all of the enemies have been eliminated
    if len(enemies) <= 1:
        current_level += 1
        #Making a new row of enemies
        new_level(current_level)
    #Managing the player's ability to shoot
    if keys_pressed[K_RSHIFT]:
        player1.shot = True
    if player1.bullet.y <= 0:
        player1.shot = False
    player1.shoot()
    #This loop checks if the enemy has been hit by one of the player's bullets
    for i in range(len(enemies) - 1):
        #Only checks if the enemies have been hit if the player has shot a bullet
        if player1.shot == True:
            enemies[i].hurtbox_detection()
            #Removing the enemy from the list, should it be hit
            if enemies[i].hit:
                player1.score += 1
                player1.shot = False
                del enemies[i]
            #Removing the enemy if it has reached the bottom of the screen
            elif enemies[i].hit_end:
                player1.score -= 1
                del enemies[i]


    #Lets the code stop running when the window is closed or when the 'ESC' key is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

#END OF LINE