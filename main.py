import pygame
import random
from pygame import surface, draw
#These are all the variables that are important to running the game.
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)
RED = (255, 0, 0)
PLAY_X = 10
PLAY_Y = 10
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PLAY_WIDTH = SCREEN_WIDTH - 20
PLAY_HEIGHT = SCREEN_HEIGHT - 20
BORDER_SIZE = 10
APPLE_X = random.randint(20, 600)
APPLE_Y = random.randint(20, 440)
x = 310
y = 230

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Snake")
while True:
    pygame.time.delay(60)
#MAKE SURE CODE IS IN THE RIGHT ORDER. DO NOT MOVE YOUR PLAYER AND THEN FILL THE SCREEN WITH BLACK BEFORE IT UPDATES.
#First numbers are coordinates (310,230 in this case) and the last 2 sets of numbers (20,20) are the width and height.
#Also a good reference point for the base coordinates for the center in case I need them again.



    window.fill(BLACK)
    #The code below draws the visible boundary for the player
    pygame.draw.rect(
        window,
        BLUE,
        (PLAY_X, PLAY_Y, PLAY_WIDTH, PLAY_HEIGHT),
        BORDER_SIZE
    )
#This code spawns the Apple.
    pygame.draw.rect(window, RED, (APPLE_X, APPLE_Y, 20, 20))
#Make sure to separate each line of code so they won't get bundled together on accident preventing keypresses from working correctly.
#Each if statement needs to be accurate to the barrier shown to the player for fair game play.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x > 20:
            x = x -5

    if keys[pygame.K_RIGHT]:
        if x < 600:
            x = x +5

    if keys[pygame.K_UP]:
        if y > 20:
            y = y -5

    if keys[pygame.K_DOWN]:
        if y < 440:
            y = y +5
#Fuck that guy that made programming languages like this once caps sensitive.
    pygame.draw.rect(window, WHITE, (x, y, 20, 20))

    player_rect = pygame.Rect(x, y, 20, 20)

    apple_rect = pygame.Rect(APPLE_X, APPLE_Y, 20, 20)
    if player_rect.colliderect(apple_rect):
        APPLE_X = random.randint(20, 600)
        APPLE_Y = random.randint(20, 440)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            pygame.quit()