import pygame
from pygame import surface, draw

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
x = 310
y = 230

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Snake")
while True:
    pygame.time.delay(60)

#First numbers are coordinates (310,230 in this case) and the last 2 sets of numbers (20,20) are the width and height.
    pygame.draw.rect(window, WHITE, (310,230,20,20))

    window.fill(BLACK)
#Make sure to separate each line of code so they won't get bundled together on accident preventing keypresses from working correctly.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x -20

    if keys[pygame.K_RIGHT]:
        x = x +20

    if keys[pygame.K_UP]:
        y = y -20

    if keys[pygame.K_DOWN]:
        y = y +20

    pygame.draw.rect(window, WHITE, (x, y, 20, 20))


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            pygame.quit()