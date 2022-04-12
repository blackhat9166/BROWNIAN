import pygame, sys
import random
import math

def bouncing_rect():
    global x_speed,y_speed, speed
    moving_rect.x += x_speed
    moving_rect.y += y_speed

    random.seed()
    # collision with border
    if moving_rect.right >= screen_width:
        x_speed = int((-1)*(random.uniform(1, 12)))
        if y_speed < 0:
            y_speed = int(-1*math.sqrt(math.fabs(speed-(x_speed*x_speed))))
        else:
            y_speed = int(math.sqrt(math.fabs(speed - (x_speed * x_speed))))
    if moving_rect.left <= 0:
        x_speed = int((1) * (random.uniform(1, 12)))
        if y_speed < 0:
            y_speed = int(-1 * math.sqrt(math.fabs(speed - (x_speed * x_speed))))
        else:
            y_speed = int(math.sqrt(math.fabs(speed - (x_speed * x_speed))))
    if moving_rect.bottom >= screen_height:
        y_speed = int((-1) * (random.uniform(1, 12)))
        if x_speed < 0:
            x_speed = int(-1 * math.sqrt(math.fabs(speed - (y_speed * y_speed))))
        else:
            x_speed = int(math.sqrt(math.fabs(speed - (y_speed * y_speed))))
    if moving_rect.top <= 0:
        y_speed = int((random.uniform(1, 12)))
        if x_speed < 0:
            x_speed = int(-1 * math.sqrt(math.fabs(speed - (y_speed * y_speed))))
        else:
            x_speed = int(math.sqrt(math.fabs(speed - (y_speed * y_speed))))

    pygame.draw.circle(screen, (0, 255, 0), moving_rect.center, 10)


pygame.init()
clock = pygame.time.Clock()
screen_width,screen_height = 800,800
screen = pygame.display.set_mode((screen_width,screen_height))

moving_rect = pygame.Rect(50,50,20,20)
x_speed,y_speed = 10, 15
speed = (x_speed*x_speed) + (y_speed*y_speed)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30,30,30))
    bouncing_rect()

    pygame.display.flip()
    clock.tick(60)
