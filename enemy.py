import pyglet

class Enemy_1(object):
	"""docstring for Enemy_1"""
	def __init__(self, arg):
		super(Enemy_1, self).__init__()
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
