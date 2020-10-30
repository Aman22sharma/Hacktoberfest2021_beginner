from random import randint
from sense_hat import SenseHat, ACTION_RELEASED
import time

sense = SenseHat()
lastDirection='left';
red = (255, 0, 0);
green = (0, 255, 0);
blue = (0, 0, 255);
off= (0,0,0);
points=0;
sense.clear();

def newFruit():
	global snake;
	global fruit;
	newFindFruit = True;
	while newFindFruit:
		x = randint(0, 7);
		y = randint(0, 7);
		fruit = Point(x,y);
		if not checkIfPointInside(snake, fruit, 0):
			newFindFruit = False;
	sense.set_pixel(x, y, blue)

def checkIfPointInside(snake, point, startIndex):
	for index in range(startIndex,len(snake)):
		if snake[index].x_pos == point.x_pos and snake[index].y_pos == point.y_pos:
			return True;
	return False;

class Point:
	global lastDirection;
	global gamePad;

	def __init__(self, x,y):
		self.x_pos=x;
		self.y_pos=y;
		sense.set_pixel(self.x_pos, self.y_pos, green)

	def updateFirstPoint(self):
		if lastDirection =='left':
			self.x_pos = (self.x_pos-1) % 8;
		elif lastDirection =='right':
			self.x_pos = (self.x_pos+1) % 8;
		elif lastDirection =='down':
			self.y_pos = (self.y_pos+1) % 8;
		elif lastDirection =='up':
			self.y_pos = (self.y_pos-1) % 8;
		self.pointOn(red);
	def pointOff(self):
		sense.set_pixel(self.x_pos, self.y_pos, off)

	def pointOn(self, color):
		sense.set_pixel(self.x_pos, self.y_pos, color)

gameOver = False;
snake = [Point(4,4),Point(5,4)]
newFruit();
while True:
	while not gameOver:
		for event in sense.stick.get_events():
			if event.action == ACTION_RELEASED:
				if event.direction == 'left' and lastDirection != 'right':
					lastDirection = event.direction;
				elif event.direction == 'right' and lastDirection != 'left':
					lastDirection = event.direction;
				elif event.direction == 'up' and lastDirection != 'down':
					lastDirection = event.direction;
				elif event.direction == 'down' and lastDirection != 'up':
					lastDirection = event.direction;

		for index in range ((len(snake)-1),0,-1):
			if index == (len(snake)-1):
				snake[index].pointOff();
			snake[index].x_pos=snake[index-1].x_pos;
			snake[index].y_pos=snake[index-1].y_pos;
			snake[index].pointOn(green);
		snake[0].updateFirstPoint();
		if checkIfPointInside(snake, snake[0], 1):
			sense.show_message("GameOver, Points: %d" %(points), text_colour=[200, 0, 200])
			gameOver=True;
			points=0;
		if snake[0].x_pos == fruit.x_pos and snake[0].y_pos == fruit.y_pos:
			snake.append(Point( snake[len(snake)-1].x_pos, snake[len(snake)-1].y_pos))
                        points +=1;
                        if points < 62 :
                            newFruit();
                        if points >= 62:
                            gameOver=True;
                            sense.show_message("GameOver, Points: %d" %(points), text_colour=[200,0,200]);
                            points=0;
		time.sleep(0.5);
	time.sleep(1.0);
	for event in sense.stick.get_events():
		if event.action == ACTION_RELEASED and event.direction == 'middle':
			gameOver=False;
			snake = [Point(4,4),Point(5,4)]
			newFruit();
