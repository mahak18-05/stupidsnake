import pygame
import sys
import random
pygame.init()
class Snake(object):
    def __init__(self):
        self.length=1
        self.positions=[((width/2),(height/2))]
        self.direction=random.choice([UP,DOWN,LEFT,RIGHT])
        self.color=green
    def get_head_position(self):
        return self.positions[0]
    def turn(self, point):
        if self.length > 1 and (point[0] * -1,point[1]*-1)==self.direction:
            return
        else:
            self.direction=point

    def move(self):
        current= self.get_head_position()
        x,y=self.direction
        new=(((current[0]+(x*grid_size)) % width),(current[1]+(y*grid_size))%height )
        if len(self.positions)>2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions)>self.length:
                self.positions.pop()

    def reset(self):
        self.length=1
        self.positions=[((width/2),(height/2))]
        self.direction=random.choice([UP,DOWN,LEFT,RIGHT])

    def draw(self, surface):
        for i, pos in enumerate(self.positions):
            radius = grid_size // 2
            center = (pos[0] + radius, pos[1] + radius)
        
            if i == 0:  # If it's the head
                pygame.draw.circle(surface, (0, 150, 0), center, radius + 2)  # Dark green head
                eye_offset_x = grid_size // 2
                eye_offset_y = grid_size // 4

                if self.direction == UP:
                    eye1 = (center[0] - eye_offset_x, center[1] - eye_offset_y)
                    eye2 = (center[0] + eye_offset_x, center[1] - eye_offset_y)
                elif self.direction == DOWN:
                    eye1 = (center[0] - eye_offset_x, center[1] + eye_offset_y)
                    eye2 = (center[0] + eye_offset_x, center[1] + eye_offset_y)
                elif self.direction == LEFT:
                    eye1 = (center[0] - eye_offset_y, center[1] - eye_offset_x)
                    eye2 = (center[0] - eye_offset_y, center[1] + eye_offset_x)
                elif self.direction == RIGHT:
                    eye1 = (center[0] + eye_offset_y, center[1] - eye_offset_x)
                    eye2 = (center[0] + eye_offset_y, center[1] + eye_offset_x)

                pygame.draw.circle(surface, black, eye1, 3)  # Left eye
                pygame.draw.circle(surface, black, eye2, 3)  # Right eye
            else:
                pygame.draw.circle(surface, self.color, center, radius)  # Normal body


    def handle_keys(self):
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key== pygame.K_UP:
                    self.turn(UP)
                elif event.key== pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key== pygame.K_RIGHT:
                    self.turn(RIGHT)
                elif event.key== pygame.K_LEFT:
                    self.turn(LEFT)
        


    

class Food(object):
    def __init__(self):
        self.position = (0,0)
        self.color = red
        self.randomize_position()
    def randomize_position(self):
        self.position = (random.randint(0, grid_width - 1) * grid_size, random.randint(0, grid_height - 1) * grid_size)

    def draw(self, surface):
    
        rect = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))

        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, black, rect, 1)


def drawgrid(surface):
    for y in range(0,int(grid_height)):
        for x in range(0,int(grid_width)):
            if((x+y)%2)==0:
                rect = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))

                pygame.draw.rect(surface,gray1 ,rect)
            else:
                rect = pygame.Rect((x*grid_size,y*grid_size),(grid_size,grid_size))
                pygame.draw.rect(surface ,gray2 ,rect)


width=480
height=480
grid_size=10
grid_width=width//grid_size
grid_height=height//grid_size
gray1=(120,120,120)
gray2=(170,170,170)
green=(0,255,0)
black=(0,0,0)
red=(255,0,0)
UP = (0,-1)
DOWN =(0,1)
LEFT =(-1,0)
RIGHT =(1,0)
font = pygame.font.Font('freesansbold.ttf',30)

def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen=pygame.display.set_mode((width,height),0,32)

    #surface=pygame.Surface(screen.get_size())
    surface = pygame.Surface(screen.get_size()).convert()


    drawgrid(surface)

    snake=Snake()
    food=Food()

    score=0
    while True:
        clock.tick(10)
        snake.handle_keys()
        drawgrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = font.render("Score: {0}".format(score), True, black)

        screen.blit(text, (5,10))

        pygame.display.update()

main()