import pygame
import random
from random import randint
import time

pygame.init()
screen_width = 500
screen_height = 500
window = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Tom&jerry")
icon = pygame.image.load("Mouse.png")
pygame.display.set_icon(icon)
pygame.display.update()
Black = (0, 0, 0)
Sea = (135, 206, 255)
Island = (255, 255, 255)
Bridge = (0, 255, 0)
window.fill(Black)

def sea():
    pygame.draw.rect(window, Sea, [50, 50, 55, 55])
    pygame.draw.rect(window, Sea, [50, 106, 55, 55])
    pygame.draw.rect(window, Sea, [50, 162, 55, 55])
    pygame.draw.rect(window, Sea, [106, 50, 55, 55])
    pygame.draw.rect(window, Sea, [162, 50, 55, 55])
    pygame.draw.rect(window, Sea, [218, 50, 55, 55])
    pygame.draw.rect(window, Sea, [274, 50, 55, 55])
    pygame.draw.rect(window, Sea, [330, 50, 55, 55])
    pygame.draw.rect(window, Sea, [386, 50, 55, 55])
    pygame.draw.rect(window, Sea, [50, 218, 55, 55])
    pygame.draw.rect(window, Sea, [50, 274, 55, 55])
    pygame.draw.rect(window, Sea, [50, 330, 55, 55])
    pygame.draw.rect(window, Sea, [50, 386, 55, 55])
    pygame.draw.rect(window, Sea, [386, 106, 55, 55])
    pygame.draw.rect(window, Sea, [386, 162, 55, 55])
    pygame.draw.rect(window, Bridge, [386, 218, 55, 55])
    pygame.draw.rect(window, Sea, [386, 274, 55, 55])
    pygame.draw.rect(window, Sea, [386, 330, 55, 55])
    pygame.draw.rect(window, Sea, [386, 386, 55, 55])
    pygame.draw.rect(window, Sea, [106, 386, 55, 55])
    pygame.draw.rect(window, Sea, [162, 386, 55, 55])
    pygame.draw.rect(window, Sea, [218, 386, 55, 55])
    pygame.draw.rect(window, Sea, [274, 386, 55, 55])
    pygame.draw.rect(window, Sea, [330, 386, 55, 55])

def island():
    pygame.draw.rect(window, Island, [106, 106, 55, 55])
    pygame.draw.rect(window, Island, [106, 162, 55, 55])
    pygame.draw.rect(window, Island, [106, 218, 55, 55])
    pygame.draw.rect(window, Island, [106, 274, 55, 55])
    pygame.draw.rect(window, Island, [106, 330, 55, 55])
    pygame.draw.rect(window, Island, [162, 106, 55, 55])
    pygame.draw.rect(window, Island, [162, 162, 55, 55])
    pygame.draw.rect(window, Island, [162, 218, 55, 55])
    pygame.draw.rect(window, Island, [162, 274, 55, 55])
    pygame.draw.rect(window, Island, [162, 330, 55, 55])
    pygame.draw.rect(window, Island, [218, 106, 55, 55])
    pygame.draw.rect(window, Island, [218, 162, 55, 55])
    pygame.draw.rect(window, Island, [218, 218, 55, 55])
    pygame.draw.rect(window, Island, [218, 274, 55, 55])
    pygame.draw.rect(window, Island, [218, 330, 55, 55])
    pygame.draw.rect(window, Island, [274, 106, 55, 55])
    pygame.draw.rect(window, Island, [274, 162, 55, 55])
    pygame.draw.rect(window, Island, [274, 218, 55, 55])
    pygame.draw.rect(window, Island, [274, 274, 55, 55])
    pygame.draw.rect(window, Island, [274, 330, 55, 55])
    pygame.draw.rect(window, Island, [330, 106, 55, 55])
    pygame.draw.rect(window, Island, [330, 162, 55, 55])
    pygame.draw.rect(window, Island, [330, 218, 55, 55])
    pygame.draw.rect(window, Island, [330, 274, 55, 55])
    pygame.draw.rect(window, Island, [330, 330, 55, 55])

def tom():
   list_tomx = [106, 162, 218, 274, 330]
   list_tomy = [106,162,218,274,330]
   xt = random.choice(list_tomx)
   yt = random.choice(list_tomy)
   cat_view = pygame.image.load("Cat.jpg")
   cat_view = pygame.transform.scale(cat_view, (55, 55))
   window.blit(cat_view, (xt, yt))
   delay()

def mouse():
    list_mousex = [106, 162, 218, 274, 330, 386]
    list_mousey = [106, 162, 218, 274, 330, 386]
    random_xm = random.choice(list_mousex)
    random_ym = random.choice(list_mousey)
    mouse_posx = random.choice(list_mousex)
    mouse_posy = random.choice(list_mousey)
    current_pos = (mouse_posx, mouse_posy)
    coor = [[56, 0], [-56, 0], [0, -56], [0, 56]]
    i, j = random.choice(coor)
    mouse = pygame.image.load("Mouse.png")
    mouse = pygame.transform.scale(mouse, (55, 55))
    window.blit(mouse, (random_xm, random_ym))
    delay()
    mouse_posy += j
    mouse_posx += i
    current_pos = (mouse_posx, mouse_posy)
def delay():
    pygame.time.delay(200)

def senarios():
    if mouse == sea():
        window.fill(Sea)
        pygame.quit()
        exit()
    if time == 3:
        window.fill(Black)
        pygame.quit()
        exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    island()
    sea()
    tom()
    mouse()
    senarios()
    pygame.display.update()
