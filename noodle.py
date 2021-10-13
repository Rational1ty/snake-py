from collections import deque
from enum import Enum
import random

import graphics as g

from constants import *
from functions import square

Direction = Enum('Direction', 'UP DOWN LEFT RIGHT')


class Snake:
	def __init__(self):
		w_half, h_half = WIDTH // 2, HEIGHT // 2

		# snake starts at the center of the board
		# the subtracted part is needed to keep the snake aligned with the grid
		self.x = w_half - (w_half % SCALE)
		self.y = h_half - (h_half % SCALE)

		self.direct = random.choice(tuple(Direction))
		self.size = INITIAL_SIZE
		self.body = deque()

	def setdirection(self, d: str):
		if d == 'UP' or d == 'W':
			if self.direct != Direction.DOWN:
				self.direct = Direction.UP
		if d == 'DOWN' or d == 'S':
			if self.direct != Direction.UP:
				self.direct = Direction.DOWN
		if d == 'LEFT' or d == 'A':
			if self.direct != Direction.RIGHT:
				self.direct = Direction.LEFT
		if d == 'RIGHT' or d == 'D':
			if self.direct != Direction.LEFT:
				self.direct = Direction.RIGHT

	def move(self, win: g.GraphWin):
		if self.direct == Direction.UP:
			self.y -= SCALE
		if self.direct == Direction.DOWN:
			self.y += SCALE
		if self.direct == Direction.LEFT:
			self.x -= SCALE
		if self.direct == Direction.RIGHT:
			self.x += SCALE

		self._wrap()

		# remove part at end of snake and undraw it unless snake needs to grow
		if len(self.body) == self.size:
			self.body.pop().undraw()

		# add new part to head of snake and draw it
		head = self._newbodypart()
		self.body.appendleft(head)

		try:
			head.draw(win)
		except g.GraphicsError:
			pass

	def _wrap(self):
		if self.x < 0:
			self.x = WIDTH - abs(self.x)
		if self.x >= WIDTH:
			self.x = 0
		if self.y < 0:
			self.y = HEIGHT - abs(self.y)
		if self.y >= HEIGHT:
			self.y = 0

	def checkcollision(self) -> bool:
		head = square(self.x, self.y, SCALE)
		first = True

		for part in self.body:
			if first:
				first = False
				continue
			if head.contains(part):
				return True

		return False

	def _newbodypart(self) -> g.Rectangle:
		part = square(
			self.x + SNAKE_PADDING, 
			self.y + SNAKE_PADDING, 
			SCALE - (2 * SNAKE_PADDING)
		)

		part.setFill(BODY_COLOR)
		part.setOutline(BODY_COLOR)

		return part


class Apple:
	def __init__(self, win: g.GraphWin, exclude):
		self.big = random.random() < BIG_CHANCE

		while True:
			bound = SCALE if self.big else 0
			self.x = random.randrange(bound, WIDTH - bound, SCALE)
			self.y = random.randrange(bound, HEIGHT - bound, SCALE)
			self.shape = self._getshape()

			if not self._checkcollision(exclude): break
			
		self.shape.draw(win)

	def _checkcollision(self, exclude) -> bool:
		return any(map(self.shape.contains, exclude))

	def _getshape(self) -> g.Rectangle:
		shape = square(self.x, self.y, SCALE)

		if self.big:
			shape.pad(BIG_PAD)
		
		shape.setFill(APPLE_COLOR)
		shape.setOutline(APPLE_COLOR)

		return shape
