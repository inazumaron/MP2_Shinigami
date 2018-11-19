import pyglet

def bullet_action(bullet,target_list):
	bullet.obj_x += bullet.obj_vx
	bullet.obj_y += bullet.obj_vy
	bullet.obj_vx += bullet.obj_ax
	bullet.obj_vy += bullet.obj_ay
	#Update bullet location
	#Just add more behavior like if bullet is homing etc
	#if bullet.modifiers["homing"]:
		#Do stuff here
		#find closest enemy within a 
		#certain distance from the list target_list (may be enemy or player)
	#Also check if in collision with target
	#if in collision:
	#return bullet,target
	#else:
	return bullet

class bullet(object):
	def __init__(self):
		super(bullet, self).__init__()
		self.obj_x = 0		#Initial position
		self.obj_y = 0		
		self.obj_vx = 0		#Initial velocity
		self.obj_vy = 0
		self.obj_ax = 0		#Acceleration (0 if bullet speed is constant)
		self.obj_ay = 0
		self.modifiers = {"homing":False,"explosive":False,"piercing":False} #piercing,homing, etc
		self.destroy = True
