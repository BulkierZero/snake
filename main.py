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
        
def end_check():
    for i in range(1, snake.length-1, 1):
        if snake.x[0] == snake.x[i] and snake.y[0] == snake.y[i]:
            global running
            running = False
            print("Game Over Noob! " + "Score:" + str(snake.length))

class Snake:    # the snake!
    def __init__(self):
        self.length = 1    # length of snake array
        self.speed = 40    # speed in pixels
<<<<<<< Updated upstream
        self.x = [360] * self.length    # position of snake in x
        self.y = [360] * self.length    # position of snake in y
=======
        self.x = [(screen_width/2) - (size/2)]    # position of snake in x
        self.y = [(screen_height/2) - (size/2)]    # position of snake in y
>>>>>>> Stashed changes
        self.dir_x = 0    # direction snake in x
        self.dir_y = 0    # direction of snake in y

    def draw(self):    # draws the snake to surface.
        for i in range(self.length):    # its supposed to run through the snake array and draw each x and y coordinate.
            pygame.draw.rect(screen, (255, 0, 0), [self.x[i], self.y[i], size-1, size-1])

    def move(self):    # changes x and y coordinates of snake
        for i in range(self.length-1, 0, -1):    # loop through array backwards changing next element to current
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        self.x[0] = self.x[0] + (self.speed * self.dir_x)    # takes the position of head and adds the vector to x
        self.y[0] = self.y[0] + (self.speed * self.dir_y)    # takes the position of head and adds the vector to y
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
        for i in range(1, self.length, 1):    # loop through array changing previous element value to current value...maybe
            self.x[i] = self.x[i-1] - self.x[i]
            self.y[i] = self.y[i-1]  - self.y[i]
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        # wraps snake from one side of screen to the other in both x and y
        if self.x == screen_width:
            self.x = 0
        elif self.x == -size:
            self.x = screen_width - size
        elif self.y == screen_height:
            self.y = 0
        elif self.y == -size:
            self.y = screen_height - size

    def grow(self):    # increases the x and y position arrays by 1
        self.length += 1


class Food:    # makes the foods
    def __init__(self):    # initial x and y coordinates
        self.x = random.randrange(0, screen_width - size, size)
<<<<<<< Updated upstream
        self.y = random.randrange(0, screen_height, size)
        
    def new_location(self):
        self.x = random.randrange(0, 760, 40)
        self.y = random.randrange(0, 760, 40)
=======
        self.y = random.randrange(0, screen_height - size, size)
        
    def new_location(self):
        self.x = random.randrange(0, screen_width - size, size)
        self.y = random.randrange(0, screen_height - size, size)
        for i in range(snake.length):
            if snake.x[i] == self.x and snake.y[i] == self.y:
                self.new_location()
>>>>>>> Stashed changes

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
    end_check()
    clock.tick(10)
    eaten()



    
