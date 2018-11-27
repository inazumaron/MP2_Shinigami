import pyglet

class Enemy_1(object):
	"""docstring for Enemy_1"""
	def __init__(self):		#
		super(Enemy_1, self).__init__()
		self.x = 0
		self.y = 800
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
		self.id = "easy_1"
		self.right = True

	def move(self):		#AI of enemy
		if self.right == True: 	#Move right till out of screen (600x800)	###check first if moving right 
			self.x += 10

		if self.x == 550:				###set to false when it reaches right boundary
			self.right = False

		if self.right == False:			
			self.x -= 10

		if self.x == 10:				###set to true when it reaches left boundary
			self.right = True	

		self.y -= 0.75					###vertical speed as of now
		return self						###very basic ai movement, still experimenting for additional movements
