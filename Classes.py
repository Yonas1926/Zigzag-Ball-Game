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

