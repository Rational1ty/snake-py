from collections import deque
from time import sleep
import graphics as g

from constants import *
from noodle import Apple, Snake


def frame():
	global window, keys, snake, apple

	if len(keys) > 0:
		snake.setdirection(keys.popleft())

	snake.move(window)

	if snake.checkcollision():
		gameover()
		raise StopIteration()

	# check if snake eats big apple
	if apple.big:
		if (apple.x - SCALE <= snake.x <= apple.x + SCALE and
			apple.y - SCALE <= snake.y <= apple.y + SCALE):
			snake.size += APPLE_VALUE * BIG_MULT
			apple.shape.undraw()
			apple = Apple(window, snake.body)

	# check if snake eats normal apple
	if snake.x == apple.x and snake.y == apple.y:
		snake.size += APPLE_VALUE
		apple.shape.undraw()
		apple = Apple(window, snake.body)


def gameover():
	global window, snake, apple

	# display last movement
	g.update()
	sleep(0.5)

	# undraw everything
	for part in snake.body:
		part.undraw()
	apple.shape.undraw()

	# display gameover then exit
	display_score()


def display_score():
	global window, snake

	center = g.Point(WIDTH // 2, HEIGHT // 2)

	# game over text
	text = g.Text(center, f'Game over!\nScore: {snake.size}')
	text.setSize(36)
	text.setTextColor(FG_COLOR)
	text.draw(window)

	# text outline
	p1 = g.Point(center.x - 200, center.y - 70)
	p2 = g.Point(center.x + 200, center.y + 70)
	rect = g.Rectangle(p1, p2)
	rect.setOutline(FG_COLOR)
	rect.draw(window)

	g.update()

	window.getKey()


def main():
	global window, keys, snake, apple

	window = g.GraphWin('Snake', WIDTH, HEIGHT, False)
	window.setBackground(BG_COLOR)
	window.master.geometry(f'{WIDTH}x{HEIGHT}+{WIN_X}+{WIN_Y}')

	snake = Snake()
	apple = Apple(window, ())

	keys = deque()
	count = 1

	while True:
		key = window.checkKey().upper()

		# check for key press
		if key:
			# end the game
			if key == 'ESCAPE':
				gameover()
				break

			# pause the game
			if key == 'SPACE':
				while window.getKey() != 'space':
					pass

			keys.append(key)

		# graphics updates; runs at FRAME_RATE
		if count % REFRESH_PER_FRAME == 0:
			count = 0
			try:
				frame()
			except StopIteration:
				break

		count += 1
		g.update(REFRESH_RATE)


if __name__ == '__main__':
	main()
