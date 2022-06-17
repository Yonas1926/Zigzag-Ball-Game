import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

display_x = 500
display_y = 500
display = (display_x, display_y)

win = pygame.display.set_mode(display)
pygame.display.set_caption("Zizag Ball Game")

background_Image = pygame.image.load("images/bg1.jpg")
background = pygame.transform.scale(background_Image, (500, 500))

ball_color = (0, 200, 255)
boundary_line_color = (150, 200, 255)
boundary_line3_color = (200, 210, 255)
ball_x_position = display_x/2
ball_y_position = display_y - 20

boundary_line1_x_position = display_x/5
boundary_line2_x_position = display_x * 4/5
boundary_line3_y_position = display_y/2

boundary_line1_start_position = (boundary_line1_x_position, 0)
boundary_line1_end_position = (boundary_line1_x_position, display_y)

boundary_line2_start_position = (boundary_line2_x_position, 0)
boundary_line2_end_position = (boundary_line2_x_position, display_y)

boundary_line3_start_position = (boundary_line1_x_position, boundary_line3_y_position)
boundary_line3_end_position = (boundary_line2_x_position, boundary_line3_y_position)

ball_radius = 15
border_width = 0
bound_line_width = 5
ball_speed = 3


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
    win.blit(background, (0, 0))
    # pygame.draw.line(win, boundary_line3_color, boundary_line3_start_position, boundary_line3_end_position,
    #                  bound_line_width // 2)
    pygame.draw.line(win, boundary_line_color, boundary_line1_start_position, boundary_line1_end_position,
                     bound_line_width)
    pygame.draw.line(win, boundary_line_color, boundary_line2_start_position, boundary_line2_end_position,
                     bound_line_width)
    pygame.draw.circle(win, ball_color, (ball_x_position, ball_y_position), ball_radius, border_width)
    pygame.display.update()


def main():
    pass


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
# code for pressing key functionality
    pressed_key = pygame.key.get_pressed()

    # The -5 in the line below is for some gap between the line and the ball

    if pressed_key[pygame.K_RIGHT] and ball_x_position < (boundary_line2_x_position - ball_radius - 5):
        ball_x_position += ball_speed
    if pressed_key[pygame.K_LEFT] and ball_x_position > (boundary_line1_x_position + ball_radius + 6):
        ball_x_position -= ball_speed
    if pressed_key[pygame.K_UP] and ball_y_position > (boundary_line3_y_position + ball_radius + 4):
        ball_y_position -= ball_speed
    if pressed_key[pygame.K_DOWN] and ball_y_position < (display_y - ball_radius - 5):
        ball_y_position += ball_speed

    draw_game()

    pygame.display.flip()
    pygame.time.wait(10)


# main()