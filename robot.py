import turtle
import math


class Shape:
    """ Abstract base class for shapes
    """
    def __init__(self, centre_x, centre_y, rotation):
        self._centre = (centre_x, centre_y)
        self._rotation = rotation

    def _move_to_draw_position(self, t):
        """ Move the turtle to the centre of the shape, pointing in the direction of rotation.
        :param t: The turtle
        :return: None
        """
        t.penup()
        t.goto(self._centre)
        t.setheading(self._rotation)

    def draw(self, t):
        """ Draw the shape. This is an abstract method.
        :param t: The turtle
        :return: None
        """
        raise NotImplementedError("Subclasses must implement draw!")


class Circle(Shape):
    def __init__(self, centre_x, centre_y, radius):
        # Rotating a circle does nothing, so circle does not need rotation
        Shape.__init__(self, centre_x, centre_y, 0)
        self._radius = radius

    def draw(self, t):
        # Divide the circle into steps
        num_steps = int(self._radius * 3)
        circumference = 2.0 * math.pi * self._radius
        step_length = circumference / num_steps
        step_angle = 360.0 / num_steps
        # Move to the edge of the circle
        self._move_to_draw_position(t)
        t.forward(self._radius)
        t.right(90)
        t.pendown()
        # Draw the circle
        for step in xrange(0, num_steps):
            t.forward(step_length)
            t.right(step_angle)


class Rectangle(Shape):
    def __init__(self, centre_x, centre_y, width, height, rotation=0):
        Shape.__init__(self, centre_x, centre_y, rotation)
        self._width = width
        self._height = height

    def draw(self, t):
        self._move_to_draw_position(t)
        t.penup()
        # Move to top right corner
        t.forward(self._width * 0.5)
        t.left(90)
        t.forward(self._height * 0.5)
        t.right(180)
        # Draw the four sides
        t.pendown()
        for side in xrange(4):
            t.forward(self._height if (side % 2) == 0 else self._width)
            t.right(90)


class Square(Rectangle):
    def __init__(self, centre_x, centre_y, side_length, rotation=0):
        Rectangle.__init__(self, centre_x, centre_y, side_length, side_length, rotation)


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self._points = [(x1, y1), (x2, y2), (x3, y3)]
        # Calculate centre point
        cx = (x1 + x2 + x3) / 3.0
        cy = (y1 + y2 + y3) / 3.0
        Shape.__init__(self, cx, cy, 0)

    def draw(self, t):
        # Move to the last point
        t.penup()
        t.goto(self._points[-1])
        # Draw the points
        t.pendown()
        for point in self._points:
            t.goto(point)


def main():
    """ The main function, which creates a turtle and uses it to draw a happy robot
    :return: None
    """
    t = turtle.Turtle()

    body = [Square(0, 0, 200)]
    head = [Circle(0, 200, 100),
            Circle(50, 230, 20),
            Circle(-50, 230, 20),
            Triangle(50, 170, 0, 150, -50, 170),
            Triangle(40, 300, 0, 340, -40, 300)
            ]
    arms = [Rectangle(150, 100, 100, 20, 10),
            Rectangle(200, 150, 100, 20, 70),
            Rectangle(-150, 80, 100, 20, 10),
            Rectangle(-200, 30, 100, 20, 70)
            ]
    legs = [Rectangle(100, -200, 20, 200, 5),
            Rectangle(-100, -200, 20, 200, -5)
            ]

    robot = body + arms + legs + head

    for shape in robot:
        shape.draw(t)

    t.hideturtle()
    turtle.done()


main()