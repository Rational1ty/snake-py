from time import sleep

import graphics as g

from constants import *
from noodle import Apple, Snake


def gameover(win: g.GraphWin, score: int):
	center = g.Point(WIDTH // 2, HEIGHT // 2)

	# game over text
	text = g.Text(center, f'Game over!\nScore: {score}')
	text.setSize(36)
	text.setTextColor(FG_COLOR)
	text.draw(win)

	# text outline
	p1 = g.Point(center.x - 200, center.y - 70)
	p2 = g.Point(center.x + 200, center.y + 70)
	rect = g.Rectangle(p1, p2)
	rect.setOutline(FG_COLOR)
	rect.draw(win)

	g.update()

	win.getKey()


def main():
	window = g.GraphWin('Snake', WIDTH, HEIGHT, False)
	window.setBackground(BG_COLOR)
	window.master.geometry(f'{WIDTH}x{HEIGHT}+{WIN_X}+{WIN_Y}')

	snake = Snake()
	apple = Apple(window, ())

	while True:
		key = window.checkKey().upper()

		# check for key press
		if key:
			# end the game
			if key == 'ESCAPE':
				# display last snake movement
				g.update()
				sleep(0.5)

				# undraw everything
				for part in snake.body:
					part.undraw()
				apple.shape.undraw()

				# display gameover then exit
				gameover(window, snake.size)
				break

			# pause the game
			if key == 'SPACE':
				while window.getKey() != 'space':
					pass

			snake.setdirection(key)

		snake.move(window)

		if snake.checkcollision():
			# display last snake movement
			g.update()
			sleep(0.5)

			# undraw everything
			for part in snake.body:
				part.undraw()
			apple.shape.undraw()

			# display gameover then exit
			gameover(window, snake.size)
			break

		# check if snake eats apple
		d = SCALE if apple.big else 0
		
		if apple.x - d <= snake.x <= apple.x + d and apple.y - d <= snake.y <= apple.y:
			snake.size += APPLE_VALUE * (BIG_MULT if apple.big else 1)
			apple.shape.undraw()
			apple = Apple(window, snake.body)

		g.update(FRAMERATE)


if __name__ == '__main__':
	main()
