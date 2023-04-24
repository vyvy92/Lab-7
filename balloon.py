# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 14:19:27 2023

@author: vytha
"""


import pgzrun
import pygame
import pgzero
from pgzero.builtins import Actor
from random import randint
import smtplib, ssl
import time
from sys import exit

WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon")
balloon.pos = 400,300

bird = Actor("bird-up")
bird.pos = randint(800,1600), randint(10,200)


bird2 = Actor("bird-up")
bird2.pos = randint(800,1600), randint(20,200)


house = Actor("house1")
house.pos = randint(800,1600), 480

tree = Actor("tree1")
tree.pos =randint(800,1600), 500

house2 = Actor("house1")
house2.pos = randint(800,1600), 480

tree2 = Actor("tree1")
tree2.pos =randint(800,1600), 500



bird_up = True
bird2_up = True
up = False
game_over = False
score = 0
number_of_updates =  0
life = 500

scores = []

def update_high_scores():
    global score, scores
    filename = r"D:/Thao Vy/2023/spring 2023/EE 104/lab/lab 7/Chapter 8 Balloon Flight/high scores.txt"
    scores = []
    with open(filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
        for high_score in high_scores:
            if(score > int(high_score)):
                scores.append(str(score) + " ")
                score = int(high_score)
            else:
                scores.append(str(high_score) + " ")
    with open(filename, "w") as file:
        for high_score in scores:
            file.write (high_score)
def display_high_scores():
    screen.draw.text("HIGH SCORES", (350,150), color = "black")
    y=175
    position =1
    for high_score in scores:
        screen.draw.text(str(position) + "." + high_score, (350, y), color="black")
        y +=25
        position +=1

def draw():
    screen.blit ("background1", (0,0))
    if not game_over:
        balloon.draw()
        bird.draw()
        bird2.draw()
       
        house.draw()
        tree.draw()
        house2.draw()
        tree2.draw()
        
        
        screen.draw.text("HP: " + str(life), (400, 5), color = 'black')
        
        screen.draw.text("Score: " + str(score), (700, 5), color="black")
    else :
        display_high_scores()

def on_mouse_down():
    global up
    up =True
    balloon.y -= 50
    
def on_mouse_up():
    global up
    up = False
    
def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True
    
    global bird2_up
    if bird2_up:
        bird2.image = "bird-down"
        bird2_up = False
    else:
        bird2.image = "bird-up"
        bird2_up = True
    



def update():


    global game_over, score, number_of_updates, life
    if not game_over:
        if not up:
            balloon.y += 1
        

    
        if bird.x > 0:
            
            bird.x  -= 8
            if number_of_updates ==9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates +=1
        else:
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)
            score += 1
            number_of_updates = 0
        
        if bird2.x > 0:
            
            bird2.x  -= 8
            if number_of_updates ==9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates +=1
        else:
            bird2.x = randint(800, 1600)
            bird2.y = randint(10, 200)
            score += 1
            number_of_updates = 0
            

            
        
        if house.right > 0:
            house.x -= 2
        else:
            house.x = randint(800,1600)
            score +=1
        
        
        if tree.right > 0:
            tree.x -= 2
        else:
            tree.x = randint(800,1600)
            score +=1
            
        if house2.right > 0:
            house2.x -= 2
        else:
            house2.x = randint(800,1600)
            score +=1
        
        
        if tree2.right > 0:
            tree2.x -= 2
        else:
            tree2.x = randint(800,1600)
            score +=1
    
            
        if balloon.top < 0 or balloon.bottom >560:
            life -= 1
            
            if life == 0:
                game_over = True
                update_high_scores()
            
            
        if balloon.collidepoint(bird.x, bird.y) or\
           balloon.collidepoint(bird2.x, bird2.y) or\
           balloon.collidepoint(house.x, house.y) or\
           balloon.collidepoint(tree.x, tree.y) or\
           balloon.collidepoint(house2.x, house.y) or\
           balloon.collidepoint(tree2.x, tree.y):
               life -= 1
               if life == 0:
                   game_over = True
                   update_high_scores()
                   
               
    

pgzrun.go()
               
    


