import random
import time
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Classes import *


def initialize_game():
    global background, display, win, background_Img, obstacles, best_score, start, score, ball1
    pygame.init()
    background = Background()
    display = (background.display_x, background.display_y)
    win = pygame.display.set_mode(display)
    pygame.display.set_caption("Zizag Ball Game")
    background_Image = pygame.image.load("images/bg1.jpg")
    background_Img = pygame.transform.scale(background_Image, (500, 500))
    pygame.time.set_timer(USEREVENT + 1, random.randrange(1000, 2000))
    obstacles = []
    best_score = 0
    start = time.time()
    score = 0
    MScore = 0
    ball1 = Ball()


def init():
    pygame.init()
    # gameIcon = pygame.image.load()
    # pygame.display.set_icon("gameIcon")
    pygame.display.set_caption("Zizag Ball Game")
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def draw_grid():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor4f(0.0, 0.0, 0.0, 1.0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(-0.5, 1.0)
    glVertex2f(-0.5, -1.0)
    glVertex2f(0.5, 1.0)
    glVertex2f(0.5, -1.0)

    glEnd()
    glFlush()


def draw_game():

    win.fill((255, 255, 255))
    win.blit(background_Img, (0, 0))
    # pygame.draw.line(win, background.line3_color, background.line3_start_position, background.line3_end_position,
    #                  background.line_width // 2)
    pygame.draw.line(win, background.line_color, background.line1_start_position, background.line1_end_position,
                     background.line_width)
    pygame.draw.line(win, background.line_color, background.line2_start_position, background.line2_end_position,
                     background.line_width)
    pygame.draw.circle(win, ball1.color, (ball1.x_position, ball1.y_position), ball1.radius, ball1.border_width)
    # pygame.draw.circle(win, (255, 0, 0), ball1.hit_area[0], ball1.hit_area[1], 0)
    for obstaclee in obstacles:
        obstaclee.draw(win)
    text_font = pygame.font.SysFont("comicsans", 18)
    text = text_font.render("Score: " + str(score), True, (255, 255, 255))
    win.blit(text, (10, 10))
    pygame.display.update()


def gameOverScreen():
    global obstacles, score, best_score, start
    obstacles = []
    run = True

    while run:
        for this_event in pygame.event.get():
            if this_event.type == pygame.QUIT:
                run = False
                pygame.quit()
        win.fill((255, 255, 255))
        win.blit(background_Img, (0, 0))
        text = pygame.font.SysFont("comicsans", 40)
        bestScore = text.render("Best Score: " + str(best_score), True, (255, 255, 255))
        win.blit(bestScore, ((display[1]/2 - bestScore.get_width()/2), 120))
        newScore = text.render("Score: " + str(score), True, (255, 255, 255))
        win.blit(newScore, ((display[1] / 2 - newScore.get_width() / 2), 270))
        pygame.display.update()
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_SPACE]:
            start = time.time()
            run = False
    best_score = score
    score = 0


def generateObjects():
    rand_place = (random.randrange(110, 340), -50, 50, 50)

    bomb_Obstacle = Bomb_Obstacle(rand_place[0], rand_place[1], rand_place[2], rand_place[3])
    minimize_Score_Obstacle = MScore_Obstacle(rand_place[0], rand_place[1], rand_place[2], rand_place[3])

    Pause_Power_Up = P_Power_UP(rand_place[0], rand_place[1], rand_place[2], rand_place[3])
    # Score_Multiplier = SM_Power_UP(rand_place[0], rand_place[1], rand_place[2], rand_place[3])

    objects_list = [bomb_Obstacle, minimize_Score_Obstacle]
    rand_object_index = random.randrange(0, len(objects_list))
    obstacles.append(objects_list[rand_object_index])


def key_functionality():
    global obstacles, ball1, start
    # code for pressing key functionality
    pressed_key = pygame.key.get_pressed()
    # The -5 in the line below is for some gap between the line and the ball
    if pressed_key[pygame.K_RIGHT] and ball1.x_position < (background.line2_x_position - ball1.radius - 5):
        ball1.x_position += ball1.speed
        ball1.hit_area[0][0] += ball1.speed
    if pressed_key[pygame.K_LEFT] and ball1.x_position > (background.line1_x_position + ball1.radius + 6):
        ball1.x_position -= ball1.speed
        ball1.hit_area[0][0] -= ball1.speed
    if pressed_key[pygame.K_UP] and ball1.y_position > (50 + ball1.radius + 4):
        ball1.y_position -= ball1.speed
        ball1.hit_area[0][1] -= ball1.speed
    if pressed_key[pygame.K_DOWN] and ball1.y_position < (ball1.display_y - ball1.radius - 5):
        ball1.y_position += ball1.speed
        ball1.hit_area[0][1] += ball1.speed
        # To restart the game
    if pressed_key[pygame.K_SPACE]:
        obstacles = []
        ball1 = Ball()
        start = time.time()


def motion_of_obstacles_and_check_collision():
    global start, MScore
    difficulty = 1 + (score / 5)

    for obstacle in obstacles:
        obstacle.y += difficulty
        if obstacle.y < obstacle.height * -1:
            obstacles.pop(obstacles.index(obstacle))
        # For the Bomb Obstacle
        if isinstance(obstacle, Bomb_Obstacle):
            if obstacle.collide(ball1.hit_area):
                pygame.time.delay(1000)
                gameOverScreen()
        # For the Minimize Score Obstacle
        if isinstance(obstacle, MScore_Obstacle):
            if obstacle.collide(ball1.hit_area):
                print("Collided with MScore")
                obstacles.pop(obstacles.index(obstacle))
                if score > 5:
                    MScore += 5


def main():
    global score, MScore
    MScore = 0
    initialize_game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == USEREVENT + 1:
                generateObjects()

        draw_game()
        key_functionality()
        motion_of_obstacles_and_check_collision()
        calc_Score(MScore)
        pygame.display.flip()
        pygame.time.wait(10)


def calc_Score(MScore):
    global score
    score = int(time.time() - start) - MScore


main()
