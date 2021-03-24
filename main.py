import pygame
import random

# initialize random shit
size = 40   # size of block
screen_width = 1000    # screen width
screen_height = 1000    # screen height
random = random.Random()    # random object for new location of food after eaten... i think


def eaten():    # function for when food is eaten by snake.
    if snake.x[0] == food.x and snake.y[0] == food.y:  # if snake head and food coordinates match
        food.new_location()    # gives new food location
        snake.grow()    # increases snakes length by 1


class Snake:    # the snake!
    def __init__(self):
        self.length = 1    # length of snake array
        self.speed = 40    # speed in pixels
        self.x = [360]    # position of snake in x
        self.y = [360]    # position of snake in y
        self.dir_x = 0    # direction snake in x
        self.dir_y = 0    # direction of snake in y

    def draw(self):    # draws the snake to surface.
        for i in range(self.length):    # its supposed to run through the snake array and draw each x and y coordinate.
            # This is the shit that dont work!
            pygame.draw.rect(screen, (255, 0, 0), [self.x[i], self.y[i], size, size])

    def move(self):    # changes x and y coordinates of snake
        self.x[0] = self.x[0] + (self.speed * self.dir_x)    # takes the position of head and adds the vector to x
        self.y[0] = self.y[0] + (self.speed * self.dir_y)    # takes the position of head and adds the vector to y
        for i in range(1, self.length, 1):    # loop through array changing previous element value to current value...maybe
            self.x[i] = self.x[i-1] - 40
            self.y[i] = self.y[i-1] - 40
        # wraps snake from one side of screen to the other in both x and y
        if self.x[0] == screen_width:
            self.x[0] = 0
        elif self.x[0] == -size:
            self.x[0] = screen_width - size
        elif self.y[0] == screen_height:
            self.y[0] = 0
        elif self.y[0] == -size:
            self.y[0] = screen_height - size

    def grow(self):    # increases the x and y position arrays by 1
        self.length += 1
        self.x.append(self.x[-1])
        self.y.append(self.y[-1])
        

class Food:    # makes the foods
    def __init__(self):    # initial x and y coordinates
        self.x = random.randrange(0, 760, 40)
        self.y = random.randrange(0, 760, 40)

    def new_location(self):
        self.x = random.randrange(0, screen_width - size, size)
        self.y = random.randrange(0, screen_height - size, size)

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), [self.x, self.y, size, size])


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
snake = Snake()
food = Food()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake.dir_y == 1:
                snake.dir_y = -1
                snake.dir_x = 0
            elif event.key == pygame.K_DOWN and not snake.dir_y == -1:
                snake.dir_y = 1
                snake.dir_x = 0
            elif event.key == pygame.K_RIGHT and not snake.dir_x == -1:
                snake.dir_x = 1
                snake.dir_y = 0
            elif event.key == pygame.K_LEFT and not snake.dir_x == 1:
                snake.dir_x = -1
                snake.dir_y = 0
            elif event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0, 0, 0))
    snake.draw()
    food.draw()
    pygame.display.update()
    snake.move()
    clock.tick(10)
    eaten()
