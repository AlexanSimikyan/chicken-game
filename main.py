from settings import *
import pygame
pygame.init()
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(fon_mount, (fon_x, fon_y))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and fon_x < 0 and player_x <= 300:
        fon_x += speed
        finish_x += speed
        for n in range(0, len(flor_x)):
            flor_x[n] += speed
        for n in range(0, len(fox_x)):
            fox_x[n] += speed
        for n in range(0, len(egg_x)):
            egg_x[n] += speed
        left = True
        right = False
    elif keys[pygame.K_a] and player_x >= 15:
        player_x -= speed
        left = True
        right = False
    if keys[pygame.K_d] and fon_x > -4400 and player_x >= 300:
        fon_x -= speed
        left = False
        right = True
        finish_x -= speed
        for n in range(0, len(flor_x)):
            flor_x[n] -= speed
        for n in range(0, len(fox_x)):
            fox_x[n] -= speed
        for n in range(0, len(egg_x)):
            egg_x[n] -= speed
    elif keys[pygame.K_d] and player_x <= 505:
        player_x += speed
        left = False
        right = True
    if not(keys[pygame.K_a])and not(keys[pygame.K_d]):
        left = False
        right = False
    if not (isjump):
        if keys[pygame.K_w] and not (isfall):
            isjump = True
            isfall = False
    else:
        isfall = False
        if jumpcount >= -92:
            if jumpcount < 0:
                player_y += (jumpcount ** 2) / 1500
                for n in range(0, len(flor_x)):
                    if player_x >= flor_x[n]-50 and player_x <= flor_x[n]+80 and player_y+85 <= flor_y[n] and player_y+85 >= flor_y[n]-5:
                        isjump = False
                        isonflor=True
                        jumpcount = 92
                        break
                    else:
                        isonflor =False
            else:
                player_y -= (jumpcount ** 2) / 1500
            jumpcount -= 1
        else:
            isjump = False
            jumpcount = 92
    for n in range(0, len(flor_x)):
        if player_x >= flor_x[n] - 50 and player_x <= flor_x[n] + 80 and player_y + 85 <= flor_y[n] and player_y + 85 >= flor_y[n] - 5:
            isonflor = True
            break
        else:
            isonflor = False
    if not( isonflor ) and player_y <= 470 and not( isjump ):
        isfall = True
    else:
        isfall = False
    if isfall:
        player_y += gravitation
    for n in range(0, len(flor_x)):
        win.blit(flor, (flor_x[n], flor_y[n]))
    # han animation
    han_anim += 1
    if han_anim % 10 == 9:
        i += 1
    if left:
        han_slide = han_left[i % 2]
    elif right:
        han_slide = han_right[i % 2]
    win.blit(han_slide, (player_x, player_y))
    # fox
    for n in range(0, len(fox_x)):
        fox_walk[n] += 1
        if fox_walk[n] % 400 == 399:
            s[n] += 1
        if s[n] % 2 == 1:
            fox_x[n] -= fox_speed
            fox_leftgo[n] = True
            fox_rightgo[n]= False
        else:
            fox_x[n] += fox_speed
            fox_leftgo[n] = False
            fox_rightgo[n] = True

        fox_anim += 1
        if fox_anim % 50 == 49:
            f += 1

        if fox_leftgo[n]:
            fox_side[n] = fox_left[f % 2]
        elif fox_rightgo[n]:
            fox_side[n] = fox_right[f % 2]
        for j in range(0, len(fox_x)):
            win.blit(fox_side[j], (fox_x[n], fox_y[n]))

    for n in range(0,len(fox_x)):
        if player_x >fox_x[n]-60 and player_x < fox_x[n]+80 and player_y > fox_y[n]-70 and player_y < fox_y[n]+70:
            run = False
    # egg
    for n in range(0, len(egg_x)):
        if view[n]:
            win.blit(egg, (egg_x[n], egg_y[n]))
        if player_x > egg_x[n]-40 and player_x< egg_x[n]+30 and player_y > egg_y[n]-70 and player_y< egg_y[n]+20 and view[n]:
            score += 1
            view[n] = False
    pygame.draw.rect(win, (0, 255, 0), (finish_x, finish_y, 100, 170))
    win.blit(num[score], (250, 20))
    if player_x > finish_x-40 and player_x < finish_x + 90:
        if score == 9:
            win.blit(you_win, (0, 0))
    pygame.display.update()
