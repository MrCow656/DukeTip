#!/usr/bin/env python3
#from sys import exit
import sys, pygame, pygame.mixer
from pygame.locals import *
import pygame
from pygame.locals import *
from sys import exit


cory_health = 3
enemy_health = 1
laser_duration = 1
laser_cooldown = .5



bkgrnd_img = "cory_in_the_house.png" #change name and picture
mouse_image_filename = "Good_Cory.png"
projectile_thing = "good_bullet"

pygame.init()



screen = pygame.display.set_mode((800,650), 0, 32)
background = pygame.image.load(bkgrnd_img).convert()
pygame.display.set_caption("i dont think ur ready")
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#pygamedisplays=pygame.display.set_mode(display_width,display_height)
clock = pygame.time.Clock()

speed = 250

#def bullet(x, y)
#    gamedisplays.blit(projectile_thing,(x,y))

screen.blit(background, (0,0))
def bullet_move:


while True:

    for event in pygame.event.get(): #goes through stored pygame events(?)
        if event.type == pygame.QUIT: #checks if user presses x button
            exit()


    if (cory_health == 0):
        break



    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0
    distance_moved = time_passed_seconds * speed


#mouse follow code
    x, y = pygame.mouse.get_pos()
    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2
    screen.blit(mouse_cursor, (x, y))

    if(event.type == pygame.MOUSEBUTTONDOWN):
        print("The mouse was clicked")
        x, y = pygame.mouse.get_pos()
        x -= mouse_cursor.get_width()/2
        y -= mouse_cursor.get_height()/2
        screen.blit(mouse_cursor, (x, y))
        screen.blit(pygame.image.load('good_bullet.jpg'), (x, y))



    pygame.display.update()
