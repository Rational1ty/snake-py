import graphics as g


def make_square(x: int, y: int, side_len: int) -> g.Rectangle:
	p1 = g.Point(x, y)
	p2 = g.Point(x + side_len, y + side_len)
	return g.Rectangle(p1, p2)


def contains(self: g.Rectangle, other: g.Rectangle) -> bool:
	return \
		self.p1.x <= other.p1.x <= other.p2.x <= self.p2.x and \
		self.p1.y <= other.p1.y <= other.p2.y <= self.p2.y


def pad(self: g.Rectangle, amount: int):
	self.p1.x -= amount
	self.p1.y -= amount
	self.p2.x += amount
	self.p2.y += amount


# add methods to graphics.Rectangle
setattr(g.Rectangle, 'contains', contains)
setattr(g.Rectangle, 'pad', pad)
