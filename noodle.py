from collections import deque
from enum import Enum
from random import choice, random, randrange

import graphics as g

from constants import *

Direction = Enum('Direction', 'UP DOWN LEFT RIGHT')


class Snake:
	def __init__(self):
		self.x = WIDTH // 2
		self.y = HEIGHT // 2
		self.direct = choice(tuple(Direction))
		self.body = deque()
		self.size = INITIAL_SIZE

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
		first = True
		for part in self.body:
			if first:
				first = False
				continue
			if self.x == part.p1.x and self.y == part.p1.y:
				return True
		return False

	def _newbodypart(self) -> g.Rectangle:
		p1 = g.Point(self.x, self.y)
		p2 = g.Point(self.x + SCALE, self.y + SCALE)

		rect = g.Rectangle(p1, p2)
		rect.setFill(BODY_COLOR)
		rect.setOutline(BODY_COLOR)

		return rect


class Apple:
	def __init__(self, win: g.GraphWin, exclude):
		self.big = random() < BIG_CHANCE

		while True:
			self.x = randrange(0, WIDTH, SCALE)
			self.y = randrange(0, HEIGHT, SCALE)

			if not self._checkcollision(exclude): break
			
		self.shape = self._draw(win)

	def _checkcollision(self, exclude) -> bool:
		test = None

		if self.big:
			test = lambda r: \
				self.x - SCALE <= r.p1.x <= self.x + SCALE and \
				self.y - SCALE <= r.p1.y <= self.y + SCALE
		else:
			test = lambda r: self.x == r.p1.x and self.y == r.p1.y

		return any(map(test, exclude))

	def _draw(self, win: g.GraphWin) -> g.Rectangle:
		p1 = g.Point(self.x, self.y)
		p2 = g.Point(self.x + SCALE, self.y + SCALE)

		if self.big:
			p1.move(-SCALE, -SCALE)
			p2.move(SCALE, SCALE)

		rect = g.Rectangle(p1, p2)
		rect.setFill(APPLE_COLOR)
		rect.setOutline(APPLE_COLOR)
		rect.draw(win)

		return rect
