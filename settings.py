import pygame
# player
speed = 1.5
player_x = 300
player_y = 470
han_left = [pygame.image.load('textures/han_left.png'), pygame.image.load('textures/han_left_2.png')]
han_right = [pygame.image.load('textures/han_right.png'), pygame.image.load('textures/han_right_2.png')]
# fon
fon_x = 0
fon_y = 0
fon_mount = pygame.image.load("textures/fon_mount.jpg")
win = pygame.display.set_mode((600,600))
# flor
flor = pygame.image.load("textures/flor.png")
flor_x = [15, 300, 450, 700, 800, 950, 1200, 1400, 1500, 1600, 1700, 1850, 2000, 2200, 2300, 2400, 2500, 2600, 2800, 3000,
          3050, 3200, 3250, 3300, 3350, 3500, 3600, 3700, 3800, 3900]
flor_y = [400, 350, 300, 300, 300, 200, 400, 400, 300, 300, 300, 450, 400, 350, 350, 350, 350, 350, 300, 400, 500, 200,
          300, 400, 500, 350, 350, 350, 350, 350]
isonflor = True
# fox
fox_left = [pygame.image.load("textures/fox_left_1.png"), pygame.image.load("textures/fox_left_2.png")]
fox_right = [pygame.image.load("textures/fox_right_1.png"), pygame.image.load("textures/fox_right_2.png")]
# move
isjump = False
isfall = False
jumpcount = 92
gravitation = 4
left = False
right = True
# game
run = True
# han animation
han_anim = 0
i = 0
han_slide = han_right[0]
# fox animation
fox_anim = 0
f = 0
fox_side = [fox_left[0], fox_left[0], fox_left[0], fox_left[0], fox_left[0]]
fox_leftgo = [False, False, False, False, False]
fox_rightgo = [True, True, True, True, True]
# fox
fox_x = [800, 2000, 2200, 2800, 3500]
fox_y = [477, 477, 267, 477, 267]
fox_speed = 1
fox_walk = [0, 0, 0, 0, 0]
s = [0, 0, 0, 0, 0]
# egg
egg = pygame.image.load('textures/egg.png')
egg_x = [30, 900, 950, 2400, 2150, 1650, 2850, 3600, 3700]
egg_y = [360, 520, 160, 310, 520, 260, 520, 310, 310]
view = [True, True, True, True, True, True, True, True, True]
# score
score = 0
num = [pygame.image.load("textures/num/number_0.png"), pygame.image.load("textures/num/number_1.png"),
       pygame.image.load("textures/num/number_2.png"), pygame.image.load("textures/num/number_3.png"),
       pygame.image.load("textures/num/number_4.png"), pygame.image.load("textures/num/number_5.png"),
       pygame.image.load("textures/num/number_6.png"), pygame.image.load("textures/num/number_7.png"),
       pygame.image.load("textures/num/number_8.png"), pygame.image.load("textures/num/number_9.png")]

# finish
finish_x = 4500
finish_y = 400
you_win = pygame.image.load("textures/you win.png")
