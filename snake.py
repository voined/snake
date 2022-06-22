import pygame
import random

pygame.init()
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

screen_width = 600
screen_height = 600

bg_color = (0, 0, 0)
snake_color = (0, 255, 0)
food_color = (255, 0, 0)

win = pygame.display.set_mode((screen_width, screen_height))

snakeImg = pygame.image.load('snake.png')
foodImg = pygame.image.load('food.png')

class snake(object):
	def __init__(self, width, height):
		self.x = -25
		self.y = 0
		self.width = width
		self.height = height

		self.xvel = 25
		self.yvel = 0

		self.vel = self.width


	def display(self):
		win.blit(snakeImg, (self.x, self.y))


	def move(self):
		KEYS = pygame.key.get_pressed()
		if KEYS[pygame.K_w]:
			self.xvel = 0
			self.yvel = -self.vel
		elif KEYS[pygame.K_s]:
			self.xvel = 0
			self.yvel = self.vel
		elif KEYS[pygame.K_a]:
			self.xvel = -self.vel
			self.yvel = 0
		elif KEYS[pygame.K_d]:
			self.xvel = self.vel
			self.yvel = 0

		self.x += self.xvel
		self.y += self.yvel



	def eat(self):
		global food
		if self.x == food.x and self.y == food.y:
			food.respawn = True



	def offlimits(self):
		global snake_length
		if self.x + self.width <= 0:
			self.x = screen_width-self.width
		elif self.x >= screen_width:
			self.x = 0

		if self.y + self.height <= 0:
			self.y = screen_height-self.height
		elif self.y >= screen_height:
			self.y = 0



	def death(self):
		global snake_length
		for i in range(len(snake_length)):
			if i < len(snake_length)-1:
				if snake_length[len(snake_length)-1].x == snake_length[i].x and snake_length[len(snake_length)-1].y == snake_length[i].y:
					snake_length = [snake(25, 25)]
			

			





class food(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.respawn = False

	def display(self):
		win.blit(foodImg, (self.x, self.y))
		self.respawn = False







	
score = 0
score_font = pygame.font.SysFont('8-Bit-Madness', 25)

snake_length = [snake(25,25)]

food = food(random.randint(0, (screen_height-25)/25)*25, random.randint(0, (screen_height-25)/25)*25, 25, 25)
new_snake = 0
def refreshwindow():
	global food
	global new_snake
	global snake_length

	pygame.draw.rect(win, bg_color, (0, 0, screen_width, screen_height))



	if food.respawn:
		food.x = random.randint(0, (screen_height-25)/25)*25
		food.y = random.randint(0, (screen_height-25)/25)*25
		new_snake = snake(25, 25)

		snake_length.insert(0, new_snake)

		food.respawn = False



	food.display()







	for i in range(len(snake_length)):

		if i < len(snake_length)-1:
			snake_length[i].display()
			snake_length[i].x = snake_length[i+1].x
			snake_length[i].y = snake_length[i+1].y
			


		if i == len(snake_length)-1:
			snake_length[i].eat()
			snake_length[i].display()
			snake_length[i].move()
			snake_length[i].offlimits()
			snake_length[i].death()






		score = len(snake_length)

		score_text = score_font.render('SCORE : ' + str(score), False, (255, 255, 255))

		win.blit(score_text, (250, 15))
		



		






	pygame.display.update()







run = True
while run:
	clock.tick(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False



	refreshwindow()






pygame.quit()