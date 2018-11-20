import pyglet

class Enemy_1(object):
	"""docstring for Enemy_1"""
	def __init__(self):		#
		super(Enemy_1, self).__init__()
		self.x = 0
		self.y = 600
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
		self.id = "easy_1"

	def move(self):		#AI of enemy
		self.x += 10 	#Move right till out of screen (600x800)
		return self
