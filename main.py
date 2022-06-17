import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Classes import *

background = Background()
display = (background.display_x, background.display_y)

win = pygame.display.set_mode(display)
pygame.display.set_caption("Zizag Ball Game")

background_Image = pygame.image.load("images/bg1.jpg")
background_Img = pygame.transform.scale(background_Image, (500, 500))


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


ball1 = Ball()


def draw_game():

    win.fill((255, 255, 255))
    win.blit(background_Img, (0, 0))
    pygame.draw.line(win, background.line3_color, background.line3_start_position, background.line3_end_position,
                     background.line_width // 2)
    pygame.draw.line(win, background.line_color, background.line1_start_position, background.line1_end_position,
                     background.line_width)
    pygame.draw.line(win, background.line_color, background.line2_start_position, background.line2_end_position,
                     background.line_width)
    pygame.draw.circle(win, ball1.color, (ball1.x_position, ball1.y_position), ball1.radius, ball1.border_width)
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

    if pressed_key[pygame.K_RIGHT] and ball1.x_position < (background.line2_x_position - ball1.radius - 5):
        ball1.x_position += ball1.speed
    if pressed_key[pygame.K_LEFT] and ball1.x_position > (background.line1_x_position + ball1.radius + 6):
        ball1.x_position -= ball1.speed
    if pressed_key[pygame.K_UP] and ball1.y_position > (background.line3_y_position + ball1.radius + 4):
        ball1.y_position -= ball1.speed
    if pressed_key[pygame.K_DOWN] and ball1.y_position < (ball1.display_y - ball1.radius - 5):
        ball1.y_position += ball1.speed

    draw_game()

    pygame.display.flip()
    pygame.time.wait(10)


# main()