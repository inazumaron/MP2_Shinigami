import pyglet
import bullet as bull
import random

class Enemy_1(object):
	"""docstring for Enemy_1"""
	def __init__(self, time):		#
		super(Enemy_1, self).__init__()
		self.x = 50
		self.y = 830
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
		self.id = "easy_1"
		self.right = True
		self.time = time


	def move(self):		#AI of enemy	
		self.y -= 5					###vertical speed as of now
		return self						###very basic ai movement, still experimenting for additional movements

	def shoot(self, time, player_point):
		if time%20 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -10
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None	

class Enemy_2(object):
	def __init__(self, time):		#
		super(Enemy_2, self).__init__()
		self.x = 50
		self.y = 850
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
		self.id = "easy_2"
		self.right = True
		self.time = time


	def move(self):		#AI of enemy	
		#follows a square path
		if self.x == 50 and self.y > 250:
			self.left = False
			self.down = True
			self.y -= 20
		if self.x < 550 and self.y == 250:
			self.down = False
			self.right = True
			self.x += 20
		if self.x == 550 and self.y < 750:
			self.right = False
			self.up = True
			self.y += 20
		elif self.x > 50 and self.y == 750:
			self.up = False
			self.left = True
			self.x -= 20
		return self

	def shoot(self, time, player_point):
		if time%20 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -10
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None		

class Enemy_3(object):
	def __init__(self, time):		#
		super(Enemy_3, self).__init__()
		self.x = 300
		self.y = 830
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
		self.id = "easy_3"
		self.right = True
		self.time = time


	def move(self):		#AI of enemy
		#always moves down but then chooses randomly to move left or right
		self.y -= 5	
		move = random.sample(['left','right'],1)
		if move == ['left']:
			self.x -= 5
		if move == ['right']:
			self.x += 5		
		return self	

	def shoot(self, time, player_point):
		if time%20 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -10
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None	

class Enemy_4(object):
	def __init__(self, time):		#
		super(Enemy_4, self).__init__()
		self.x = 425
		self.y = 830
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
		self.id = "easy_4"
		self.right = True
		self.time = time


	def move(self):		#AI of enemy	
		self.y -= 5					###vertical speed as of now
		return self	

	def shoot(self, time, player_point):
		if time%20 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -10
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None	

class Enemy_5(object):
	def __init__(self, time):		#
		super(Enemy_5, self).__init__()
		self.x = 550
		self.y = 830
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
		self.id = "med_1"
		self.right = True
		self.time = time


	def move(self):		#AI of enemy	
		self.y -= 5					###vertical speed as of now
		return self	

	def shoot(self, time, player_point):
		if time%20 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -10
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None			

class Enemy_6(object):
	"""docstring for Enemy_1"""
	def __init__(self):		#
		super(Enemy_6, self).__init__()
		self.x = 0
		self.y = 800
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
		self.id = "med_2"
		self.right = True

	def move(self):		#AI of enemy
		if self.right == True: 	#Move right till out of screen (600x800)	###check first if moving right 
			self.x += 10

		if self.x == 590:				###set to false when it reaches right boundary
			self.right = False

		if self.right == False:			
			self.x -= 10

		if self.x == 10:				###set to true when it reaches left boundary
			self.right = True	

		self.y -= 0.65					###vertical speed as of now
		return self						###very basic ai movement, still experimenting for additional movements

	def shoot(self, time, player_point):
		if time%20 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -10
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None		

class Enemy_7(object):
	"""docstring for Enemy_1"""
	def __init__(self):		#
		super(Enemy_7, self).__init__()
		self.x = 600
		self.y = 800
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
		self.id = "med_3"
		self.right = False

	def move(self):		#AI of enemy
		if self.right == False: 	#Move right till out of screen (600x800)	###check first if moving right 
			self.x -= 10

		if self.x == 10:				###set to false when it reaches right boundary
			self.right = True

		if self.right == True:			
			self.x += 10

		if self.x == 590:				###set to true when it reaches left boundary
			self.right = False	

		self.y -= 0.65					###vertical speed as of now
		return self						###very basic ai movement, still experimenting for additional movements

	def shoot(self, time, player_point):
		if time%20 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -10
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None		

class Enemy_8(object):
	"""docstring for Enemy_1"""
	def __init__(self):		#
		super(Enemy_8, self).__init__()
		self.x = 550
		self.y = 800
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
		self.id = "hard_1"
		self.right = False
		self.down = True

	def move(self):		#AI of enemy
		if self.y > 400 and self.down:
			self.y -= 5					###vertical speed as of now

		if self.y == 400:
			self.down = False

		if not self.down and self.x > 50:
			self.x -= 5	
		
		if self.x == 50:
			self.right = True

		if self.right and self.y < 750:
			self.y += 5

		if self.y == 750:
			self.down = True

		if self.down and self.x < 550:
			self.x += 5		

		if self.x == 550:
			self.right = False

		return self						###very basic ai movement, still experimenting for additional movements

	def shoot(self, time, player_point):
		if time%20 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -10
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None								

class Enemy_9(object):
	"""docstring for Enemy_1"""
	def __init__(self):		#
		super(Enemy_9, self).__init__()
		self.x = 50
		self.y = 800
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
		self.id = "hard_2"
		self.right = True
		self.down = True

	def move(self):		#AI of enemy
		if self.y > 50 and self.down:
			self.y -= 5					###vertical speed as of now

		if self.y == 50:
			self.down = False

		if not self.down and self.x < 250:
			self.x += 5	
		
		if self.x == 250:
			self.right = False

		if not self.right and self.y < 750:
			self.y += 5

		if self.y == 750:
			self.down = True

		if self.down and self.x > 50:
			self.x -= 5		

		if self.x == 50:
			self.right = True

		return self						###very basic ai movement, still experimenting for additional movements

	def shoot(self, time, player_point):
		if time%20 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -10
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None				

class Enemy_10(object):
	"""docstring for Enemy_1"""
	def __init__(self):		#
		super(Enemy_10, self).__init__()
		self.x = 550
		self.y = 800
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10 #Rate of fire
		self.id = "hard_3"
		self.right = False
		self.down = True

	def move(self):		#AI of enemy
		if self.y > 50 and self.down:
			self.y -= 5					###vertical speed as of now

		if self.y == 50:
			self.down = False

		if not self.down and self.x > 350:
			self.x -= 5	
		
		if self.x == 350:
			self.right = True

		if self.right and self.y < 750:
			self.y += 5

		if self.y == 750:
			self.down = True

		if self.down and self.x < 550:
			self.x += 5		

		if self.x == 550:
			self.right = False

		return self						###very basic ai movement, still experimenting for additional movements

	def shoot(self, time, player_point):
		if time%20 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -10
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None																
