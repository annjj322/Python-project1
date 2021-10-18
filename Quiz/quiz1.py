import pygame
from random import *
from time import sleep
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, SCRAP_BMP
from pygame.surfarray import pixels_green

pygame.init()

pygame.display.set_caption("JJ Game")


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))


character = pygame.image.load("C:/Users/junje/Desktop/Python-project1/Quiz/quiz_character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_pos_x = screen_width/2 - character_width/2
character_pos_y = screen_height - character_height

clock = pygame.time.Clock()

def collision():
    sleep(3)
    running = False


background = pygame.image.load("C:/Users/junje/Desktop/Python-project1/Quiz/quiz_back.png")

enemy = pygame.image.load("C:/Users/junje/Desktop/Python-project1/Quiz/quiz_enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_pos_x = randrange(0,screen_width-character_width)
enemy_pos_y = 0
enemy_speed = 6

time_spot=1

to_x = 0
move = 1


pygame.mouse.set_visible(0)

running = True
while running:
    dt = clock.tick(30)

    enemy_pos_y += enemy_speed
    
    if enemy_pos_y > screen_height:
        enemy_pos_y = 0
        enemy_pos_x = randrange(0,screen_width-enemy_width)
    
    for event in  pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            to_x -= move
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            to_x += move
    
        
            
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0

    character_pos_x += to_x * dt


    if character_pos_x < 0:
        character_pos_x = 0
    if character_pos_x > screen_width - character_width:
        character_pos_x = screen_width - character_width


    character_rect = character.get_rect()
    character_rect.left = character_pos_x
    character_rect.top = character_pos_y

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_pos_x
    enemy_rect.top = enemy_pos_y
    
    if character_rect.colliderect(enemy_rect):
        running = False


    screen.blit(background,(0,0))
    screen.blit(character,(character_pos_x,character_pos_y))
    screen.blit(enemy,(enemy_pos_x,enemy_pos_y))


    pygame.display.update()




pygame.quit()