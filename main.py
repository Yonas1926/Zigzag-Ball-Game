import random
import time
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Classes import *


def initialize_game():
    global background, display, win, background_Img, obstacles, best_score, start, score, ball1, MScore, SM_Score, time_spent, best
    pygame.init()
    win_icon = pygame.image.load("images/icon.jpg")
    background = Background()
    display = (background.display_x, background.display_y)
    win = pygame.display.set_mode(display)
    pygame.display.set_caption("Zizag Ball Game")
    pygame.display.set_icon(win_icon)
    background_Image = pygame.image.load("images/bg1.jpg")
    background_Img = pygame.transform.scale(background_Image, (500, 500))
    pygame.time.set_timer(USEREVENT + 1, random.randrange(1000, 2000))
    obstacles = []
    best_score = 0
    start = time.time()
    score = 0
    MScore = 1
    ball1 = Ball()
    SM_Score = 1
    best = [0, 0]



def init():
    pygame.init()
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
    global time_spent
    win.fill((255, 255, 255))
    win.blit(background_Img, (0, 0))

    # Drawing the borderlines
    pygame.draw.line(win, background.line_color, background.line1_start_position, background.line1_end_position,
                     background.line_width)
    pygame.draw.line(win, background.line_color, background.line2_start_position, background.line2_end_position,
                     background.line_width)
    pygame.draw.circle(win, ball1.color, (ball1.x_position, ball1.y_position), ball1.radius, ball1.border_width)

    # Left for debugging the hit area of the ball if needed
    # pygame.draw.circle(win, (255, 0, 0), ball1.hit_area[0], ball1.hit_area[1], 0)

    # Drawing the obstacles
    for obstaclee in obstacles:
        obstaclee.draw(win)

    # Drawing the Score and Time texts
    text_font = pygame.font.SysFont("comicsans", 18)

    text = text_font.render("Score: " + str(score), True, (255, 255, 255))
    timeSpentTxt = text_font.render("Time: " + str(time_spent), True, (255, 255, 255))

    # Positioning the Score and Time texts in the top right corner
    win.blit(text, (10, 10))
    win.blit(timeSpentTxt, (10, 50))

    pygame.display.update()


def gameOverScreen():
    global obstacles, score, best_score, start, time_spent, best
    obstacles = []
    run = True

    # Updating the best score and time if needed
    if score > best[0]:
        best[0] = score
        best[1] = time_spent

    while run:
        for this_event in pygame.event.get():
            if this_event.type == pygame.QUIT:
                run = False
                pygame.quit()

        win.fill((255, 255, 255))
        win.blit(background_Img, (0, 0))

        # Variables for text
        text = pygame.font.SysFont("comicsans", 25)
        game_Over_text = pygame.font.SysFont("comicsans", 50)

        gameOvertext = game_Over_text.render("Game Over!", True, (230, 230, 255))
        bestScore = text.render("Best Score: " + str(best[0]) + " in " + str(best[1]) + " sec", True, (180, 180, 255))
        newScore = text.render("Score: " + str(score) + " in " + str(time_spent) + " sec", True, (180, 180, 255))

        # Displaying the text in the variables
        win.blit(gameOvertext, ((display[1]/2 - gameOvertext.get_width()/2), 150))
        win.blit(bestScore, ((display[1]/2 - bestScore.get_width()/2), 245))
        win.blit(newScore, ((display[1] / 2 - newScore.get_width() / 2), 290))

        pygame.display.update()

        # Quick restart for the game
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_SPACE]:
            start = time.time()
            run = False
    score = 0


def generateObjects():
    rand_place = (random.randrange(110, 340), -50, 50, 50)

    bomb_Obstacle = Bomb_Obstacle(rand_place[0], rand_place[1], rand_place[2], rand_place[3])
    minimize_Score_Obstacle = MScore_Obstacle(rand_place[0], rand_place[1], rand_place[2], rand_place[3])
    slow_Obstacle = Slow_Down_Obstacle(rand_place[0], rand_place[1], rand_place[2], rand_place[3])

    Pause_Power_Up = P_Power_UP(rand_place[0], rand_place[1], rand_place[2], rand_place[3])
    Score_Multiplier = SM_Power_UP(rand_place[0], rand_place[1], rand_place[2], rand_place[3])
    Speed_Multiplier = Lightning(rand_place[0], rand_place[1], rand_place[2], rand_place[3])

    objects_list = [bomb_Obstacle, minimize_Score_Obstacle, slow_Obstacle, Pause_Power_Up, Score_Multiplier, Speed_Multiplier]

    rand_object_index = random.randrange(0, len(objects_list))
    obstacles.append(objects_list[rand_object_index])


def key_functionality():
    global obstacles, ball1, start
    
    # For pressing key functionality
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
    global start, MScore, SM_Score, time_spent
    difficulty = 1 + time_spent // 7

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
                if score > 2:
                    MScore *= 2

        # For the Pause Power Up
        if isinstance(obstacle, P_Power_UP):
            pausetext = pygame.font.SysFont("comicsans", 40)
            pause_text = pausetext.render("Pause of 2 Seconds!", True, (255, 255, 255))
            if obstacle.collide(ball1.hit_area):
                obstacles.pop(obstacles.index(obstacle))
                print("Collided with Pause Power UP")
                win.blit(pause_text, ((display[1] / 2 - pause_text.get_width() / 2), 120))
                pygame.display.update()
                time.sleep(2)

        # For the Score Multiplier Power Up
        if isinstance(obstacle, SM_Power_UP):
            if obstacle.collide(ball1.hit_area):
                obstacles.pop(obstacles.index(obstacle))
                print("Collided with Score Multiplier")
                SM_Score *= 2

        # For the Lighting Power Up
        if isinstance(obstacle, Lightning):
            if obstacle.collide(ball1.hit_area):
                print("Collided with Lightning")
                obstacles.pop(obstacles.index(obstacle))
                if ball1.speed < 16:
                    ball1.speed += 2

        # For Slow Down obstacle
        if isinstance(obstacle, Slow_Down_Obstacle):
            if obstacle.collide(ball1.hit_area):
                print("Collided with Slow Down Obstacle")
                obstacles.pop(obstacles.index(obstacle))
                if ball1.speed > 2:
                    ball1.speed -= 2


def main():
    global score, MScore, SM_Score, time_spent, start
    initialize_game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == USEREVENT + 1:
                generateObjects()

        time_spent = int(time.time() - start)
        draw_game()
        key_functionality()
        motion_of_obstacles_and_check_collision()
        calc_Score(MScore)
        pygame.display.flip()
        pygame.time.wait(10)


def calc_Score(MScore):
    global score
    score = int(((time.time() - start) * 1.4) * SM_Score) // MScore



main()
