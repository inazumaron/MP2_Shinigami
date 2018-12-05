import pyglet
import bullet as bull
import random


class Enemy_0(object):
	"""Moves down."""
	def __init__(self, time, x):
		super(Enemy_0, self).__init__()
		self.x = x
		self.y = 800
		self.life = 20
		self.attack = 'normal'
		self.damage = 5
		self.cooldown = 10
		self.id = 'easy_0'
		self.points = 5

	def move(self):
		self.y -= 2
		return self

	def shoot(self, time, player_point):
		if time%60 == 0 and time < 120:					###Shoots bullets every second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			###Initial position
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				###Initial velocity
			bullet.obj_vx = 0
			return bullet
		elif time >= 120 and time%40 == 0:					###Shoots bullets every 2/3 of a second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				
			bullet.obj_vx = 0
			return bullet	
		else:
			return None

class Enemy_1(object):
	"""Moves downwards on the left side of the screen."""
	def __init__(self, time,x):		
		super(Enemy_1, self).__init__()
		self.x = x							###Initial position
		self.y = 830						
		self.life = 40						###Health
		self.attack = "normal"				###Attack
		self.damage = 6					###Damage
		self.cooldown = 10 					#Rate of fire
		self.id = "easy_1"					###Identification
		self.right = True					
		self.time = time
		self.points = 8						#Points


	def move(self):		
		self.y -= 3							###Velocity
		return self						

	def shoot(self, time, player_point):
		if time%60 == 0:					###Shoots bullets every second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			###Initial position
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				###Initial velocity
			bullet.obj_vx = 0
			return bullet
		else:
			return None	

class Enemy_2(object):
	'''Moves on a square pattern at the top half of the screen., either clockwise or
		counter-clockwise depending on the starting point.'''
	def __init__(self, time, x):		
		super(Enemy_2, self).__init__()
		self.x = x
		self.y = 800
		self.life = 60
		self.attack = "normal"
		self.damage = 6
		self.cooldown = 10 
		self.id = "easy_2"
		self.right = True
		self.time = time
		self.points = 10
		self.direction = 'counter-clockwise'
		if x >= 300:
			self.direction = 'clockwise'

	def move(self):
		if self.direction == 'counter-clockwise':
			if self.x == 50 and self.y > 250:		###Moves downwards
				self.y -= 2.5
			if self.x < 550 and self.y == 250:		###Moves to the right
				self.x += 2.5
			if self.x == 550 and self.y < 750:		###Moves upwards
				self.y += 2.5
			elif self.x > 50 and self.y == 750:		###Moves to the left
				self.x -= 2.5
		elif self.direction == 'clockwise':
			if self.x == 550 and self.y > 250: ###moves downwards
				self.y -= 2.5					
			if self.x > 50 and self.y == 250:		###Moves to the left
				self.x -= 2.5
			if self.x == 50 and self.y < 750:		###Moves upwards
				self.y += 2.5
			elif self.x < 550 and self.y == 750:		###Moves to the right
				self.x += 2.5
		return self

	def shoot(self, time, player_point):
		if time%30 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -10
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None		

class Enemy_3(object):
	'''Moves upwards in a diagonal direction.''' 
	def __init__(self, time, x):		
		super(Enemy_3, self).__init__()
		self.x = x
		self.y = 300
		self.life = 70
		self.attack = "normal"
		self.damage = 7
		self.cooldown = 10 
		self.id = "easy_3"
		self.left = True
		self.time = time
		self.points = 15
		self.direction = 'right'
		if x >= 300:
			self.direction = 'left'


	def move(self):	
		if self.direction == 'left':
			self.y += 4			
			self.x -= 3
		elif self.direction == 'right':
			self.y += 4
			self.x += 3
		return self

	def shoot(self, time, player_point):
		if time%10 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -5
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None	

class Enemy_4(object):
	'''Moves upwards in a diagonal direction. Has two guns''' 
	def __init__(self, time, x):		
		super(Enemy_4, self).__init__()
		self.x = x
		self.y = 400
		self.life = 80
		self.attack = "normal"
		self.damage = 7
		self.cooldown = 10
		self.id = "easy_4"
		self.right = True
		self.time = time
		self.points = 20
		self.direction = 'right'
		if x >= 300:
			self.direction = 'left'

	def move(self):	
		if self.direction == 'left':
			self.y += 4			
			self.x -= 3
		elif self.direction == 'right':
			self.y += 4
			self.x += 3
		return self

	def shoot(self, time, player_point):
		if time%10 == 0:
			bullet = bull.bullet()
			bullet.obj_x = self.x
			bullet.obj_y = self.y
			bullet.obj_vy = -5
			bullet.obj_vx = (-self.x+player_point["x"])/player_point["y"]
			return bullet
		else:
			return None	

class Enemy_5(object):
	'''Moves downwards.'''
	def __init__(self, time, x,y):		#
		super(Enemy_5, self).__init__()
		self.x = x
		self.y = y
		self.life = 100
		self.attack = "normal"
		self.damage = 8
		self.cooldown = 10
		self.id = "med_1"
		self.right = True
		self.time = time
		self.points = 30


	def move(self):			
		self.y -= 3					
		return self	

	def shoot(self, time, player_point):
		if time%40 == 0 and time < 14400:					###Shoots bullets every second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			###Initial position
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				###Initial velocity
			bullet.obj_vx = 0
			return bullet
		elif time >= 14400 and time%40 == 0:					###Shoots bullets every 2/3 of a second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				
			bullet.obj_vx = 0
			return bullet	
		else:
			return None	

class Enemy_6(object):
	"""Moves on a zigzag pattern downwards."""
	def __init__(self):		#
		super(Enemy_6, self).__init__()
		self.x = 0
		self.y = 800
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10
		self.id = "med_2"
		self.right = True
		self.points = 40

	def move(self):		
		if self.right == True: 
			self.x += 2.5

		if self.x == 590:				
			self.right = False

		if self.right == False:			
			self.x -= 2.5

		if self.x == 10:				
			self.right = True	

		self.y -= 0.5					
		return self						

	def shoot(self, time, player_point):
		if time%10 == 0 and time <= 18000:					###Shoots bullets every second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			###Initial position
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				###Initial velocity
			bullet.obj_vx = 0
			return bullet
		elif time > 18000 and time%40 == 0:					###Shoots bullets every 2/3 of a second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				
			bullet.obj_vx = 0
			return bullet	
		else:
			return None

class Enemy_7(object):
	"""Moves in a zigzag pattern downwards."""
	def __init__(self):		
		super(Enemy_7, self).__init__()
		self.x = 600
		self.y = 800
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10
		self.id = "med_3"
		self.right = False
		self.points = 50

	def move(self):		
		if self.right == False: 	
			self.x -= 2.5

		if self.x == 10:			
			self.right = True

		if self.right == True:			
			self.x += 2.5

		if self.x == 590:				
			self.right = False	

		self.y -= 0.5					
		return self						

	def shoot(self, time, player_point):
		if time%10 == 0 and time <= 18000:					###Shoots bullets every second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			###Initial position
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				###Initial velocity
			bullet.obj_vx = 0
			return bullet
		elif time > 18000 and time%40 == 0:					###Shoots bullets every 2/3 of a second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				
			bullet.obj_vx = 0
			return bullet	
		else:
			return None	

class Enemy_8(object):
	"""Moves in a square pattern at the top half of the screen, either clockwise or
		counter-clockwise depending on the starting point."""
	def __init__(self,x):		
		super(Enemy_8, self).__init__()
		self.x = x
		self.y = 800
		self.life = 100
		self.attack = "normal"
		self.damage = 10
		self.cooldown = 10
		self.id = "hard_1"
		self.points = 65
		self.direction = 'counter-clockwise'
		if x >= 300:
			self.direction = 'clockwise'

	def move(self):
		if self.direction == 'counter-clockwise':
			if self.x == 50 and self.y > 250:		###Moves downwards
				self.y -= 2.5
			if self.x < 550 and self.y == 250:		###Moves to the right
				self.x += 2.5
			if self.x == 550 and self.y < 750:		###Moves upwards
				self.y += 2.5
			elif self.x > 50 and self.y == 750:		###Moves to the left
				self.x -= 2.5
		elif self.direction == 'clockwise':
			if self.x == 550 and self.y > 250: ###moves downwards
				self.y -= 2.5					
			if self.x > 50 and self.y == 250:		###Moves to the left
				self.x -= 2.5
			if self.x == 50 and self.y < 750:		###Moves upwards
				self.y += 2.5
			elif self.x < 550 and self.y == 750:		###Moves to the right
				self.x += 2.5
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
								#		_
class Enemy_9(object):			#	  _|_|	
	"""Moves in a slanted 8 pattern. |_|   """
	def __init__(self):		
		super(Enemy_9, self).__init__()
		self.x = 0
		self.y = 575
		self.life = 120
		self.attack = "normal"
		self.damage = 12
		self.cooldown = 10
		self.id = "hard_2"
		self.right = True
		self.down = False
		self.points = 80

	def move(self):		
		if self.y == 575 and self.x < 550 and not self.down:
			self.x +=2.5

		elif self.x == 550 and self.y < 750:
			self.y +=2.5

		elif self.y == 750 and self.x > 350:
			self.x -=2.5
			self.down = True

		elif self.x == 350 and self.y > 350 and self.down:
			self.y -= 2.5	

		elif self.y == 350 and self.x > 50:
			self.x -= 2.5
			self.down = False

		elif self.x == 50 and self.y < 575:						
			self.y += 2.5

								

		return self						

	def shoot(self, time, player_point):
		if time%20 == 0 and time <= 24000:					###Shoots bullets every second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			###Initial position
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				###Initial velocity
			bullet.obj_vx = 0
			return bullet
		elif time > 24000 and time%40 == 0:					###Shoots bullets every 2/3 of a second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				
			bullet.obj_vx = 0
			return bullet	
		else:
			return None			
									# _
class Enemy_10(object):				#|_|_
	"""Moves in a slanted 8 pattern.   |_|"""
	def __init__(self):		#
		super(Enemy_10, self).__init__()
		self.x = 600
		self.y = 575
		self.life = 120
		self.attack = "normal"
		self.damage = 15
		self.cooldown = 10 
		self.id = "hard_3"
		self.right = False
		self.down = False
		self.points = 100

	def move(self):		
		if self.y == 575 and self.x > 50 and not self.down:
			self.x -=2.5

		elif self.x == 50 and self.y < 750:
			self.y +=2.5

		elif self.y == 750 and self.x < 250:
			self.x +=2.5
			self.down = True

		elif self.x == 250 and self.y > 350 and self.down:
			self.y -= 2.5	

		elif self.y == 350 and self.x < 550:
			self.x += 2.5
			self.down = False

		elif self.x == 550 and self.y < 575:						
			self.y += 2.5

		return self				

	def shoot(self, time, player_point):
		if time%40 == 0 and time <= 24000:					###Shoots bullets every second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			###Initial position
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				###Initial velocity
			bullet.obj_vx = 0
			return bullet
		elif time > 24000 and time%20 == 0:					###Shoots bullets every 2/3 of a second.
			bullet = bull.bullet()
			bullet.obj_x = self.x 			
			bullet.obj_y = self.y 			
			bullet.obj_vy = -10				
			bullet.obj_vx = 0
			return bullet	
		else:
			return None
