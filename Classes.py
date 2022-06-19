import pygame


class Window(object):
    def __init__(self, display_x=500, display_y=500):
        self.display_x = display_x
        self.display_y = display_y


class Ball(Window):
    def __init__(self):
        super().__init__()
        # For the ball
        self.color = (0, 200, 255)
        self.x_position = self.display_x / 2
        self.y_position = self.display_y - 20
        self.radius = 15
        self.border_width = 0
        self.speed = 3
        self.hit_area = [[self.x_position, self.y_position], self.radius, self.border_width]


class Background(Window):
    def __init__(self):
        super().__init__()

        # For boundary line 1 and 2 : color and start & end position

        self.line_color = (150, 200, 255)
        self.line_width = 5

        self.line1_x_position = self.display_x / 5
        self.line1_start_position = (self.line1_x_position, 0)
        self.line1_end_position = (self.line1_x_position, self.display_y)

        self.line2_x_position = self.display_x * 4 / 5
        self.line2_start_position = (self.line2_x_position, 0)
        self.line2_end_position = (self.line2_x_position, self.display_y)

        # For boundary_line 3 : color and start & end position

        self.line3_color = (200, 210, 255)

        self.line3_y_position = self.display_y // 2
        self.line3_start_position = (self.line1_x_position, self.line3_y_position)
        self.line3_end_position = (self.line2_x_position, self.line3_y_position)


class Obstacle(object):
    img = [pygame.transform.scale(pygame.image.load("images/bg2.jpg"), (50, 50)), pygame.transform.scale(pygame.image.load("images/bg2.jpg"), (50, 50))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit_area = (x, y, width, height)
        self.count = 0

    def draw(self, win):
        self.hit_area = (self.x, self.y, self.width, self.height)
        if self.count >= 4:
            self.count = 0
        win.blit(self.img[self.count//2], (self.x, self.y))
        self.count += 1
        pygame.draw.rect(win, (255, 0, 0), self.hit_area, 2)

    def collide(self, hit_area_of_circle):
        if hit_area_of_circle[0][1] + 17 >= self.hit_area[1] and hit_area_of_circle[0][1] - 17 <= self.hit_area[1]:
            if hit_area_of_circle[0][0] - 17 <= self.hit_area[0] + 50 and hit_area_of_circle[0][0] + 17 >= self.hit_area[0]:
                return True
        if hit_area_of_circle[0][1] + 17 >= self.hit_area[1] + 50 and hit_area_of_circle[0][1] - 17 <= self.hit_area[1] + 50:
                if hit_area_of_circle[0][0] - 17 <= self.hit_area[0] + 50 and hit_area_of_circle[0][0] + 17 >= self.hit_area[0]:
                    return True
        if hit_area_of_circle[0][0] + 17 >= self.hit_area[0] and hit_area_of_circle[0][0] - 17 <= self.hit_area[0]:
            if hit_area_of_circle[0][1] - 17 <= self.hit_area[1] + 50 and hit_area_of_circle[0][1] + 17 >= \
                    self.hit_area[1]:
                return True
        if hit_area_of_circle[0][0] + 17 >= self.hit_area[0] + 50 and hit_area_of_circle[0][0] - 17 <= \
                    self.hit_area[0] + 50:
                if hit_area_of_circle[0][1] - 17 <= self.hit_area[1] + 50 and hit_area_of_circle[0][1] + 17 >= \
                        self.hit_area[1]:
                    return True
        return False



class Obstacle2(Obstacle):
    img = [pygame.transform.scale(pygame.image.load("images/bg4.jpg"), (50, 50))]

    def draw(self, win):
        self.hit_area = (self.x, self.y, self.width, self.height)
        win.blit(self.img[0], (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0), self.hit_area, 2)

    def collide(self, hit_area_of_circle):
        if hit_area_of_circle[0][1] + 17 >= self.hit_area[1] and hit_area_of_circle[0][1] - 17 <= self.hit_area[1]:
            if hit_area_of_circle[0][0] - 17 <= self.hit_area[0] + 50 and hit_area_of_circle[0][0] + 17 >= \
                    self.hit_area[0]:
                return True
        if hit_area_of_circle[0][1] + 17 >= self.hit_area[1] + 50 and hit_area_of_circle[0][1] - 17 <= self.hit_area[
            1] + 50:
            if hit_area_of_circle[0][0] - 17 <= self.hit_area[0] + 50 and hit_area_of_circle[0][0] + 17 >= \
                    self.hit_area[0]:
                return True
        if hit_area_of_circle[0][0] + 17 >= self.hit_area[0] and hit_area_of_circle[0][0] - 17 <= self.hit_area[0]:
            if hit_area_of_circle[0][1] - 17 <= self.hit_area[1] + 50 and hit_area_of_circle[0][1] + 17 >= \
                    self.hit_area[1]:
                return True
        if hit_area_of_circle[0][0] + 17 >= self.hit_area[0] + 50 and hit_area_of_circle[0][0] - 17 <= \
                    self.hit_area[0] + 50:
                if hit_area_of_circle[0][1] - 17 <= self.hit_area[1] + 50 and hit_area_of_circle[0][1] + 17 >= \
                        self.hit_area[1]:
                    return True
        return False
