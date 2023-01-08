import pygame
import math

pygame.init()

RED = (255,0, 0,)
GREEN = (0, 255,0)

SIZE = [800, 600]
SCREEN = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

x_pos, y_pos = SIZE[0]/2, SIZE[1]/2
x_coor, y_coor = SIZE[0]/5, SIZE[1]/5

def collision_check():
    distance = math.sqrt((x_pos - x_coor)**2 + (y_pos - y_coor)**2)
    if(distance < 50):
        return True
    else:
        return False

SCREEN.fill((0, 0, 0))

playing = True

while playing:  
   
    clock.tick(60)  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    pressed =  pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        y_pos -= 5
    if pressed[pygame.K_a]:
        x_pos -= 5
    if pressed[pygame.K_s]:
        y_pos += 5
    if pressed[pygame.K_d]:
        x_pos += 5
    if pressed[pygame.K_UP]:
        y_pos -= 5
    if pressed[pygame.K_LEFT]:
        x_pos -= 5
    if pressed[pygame.K_DOWN]:
        y_pos += 5
    if pressed[pygame.K_RIGHT]:
        x_pos += 5

    if collision_check():
        r = RED[0] + GREEN[0]
        if (r > 255):
            r = 255
        g = RED[1] + GREEN[1]
        if (g > 255):
            g = 255
        b = RED[2] + GREEN[2]
        if (b > 255):
            b = 255
        p_color = (r,g,b)
    else:
        p_color = RED

    pygame.draw.circle(SCREEN, GREEN, [x_coor, y_coor], 30)
    pygame.draw.circle(SCREEN, p_color, [x_pos, y_pos], 20)
    pygame.display.update()

pygame.quit()

