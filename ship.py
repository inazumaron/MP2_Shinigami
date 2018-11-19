import pyglet
import math
import bullet as b

def ship_move(x,y,left,right,up,down):
	#Change coordinates as necessary
	#check if outside boundary
	if left:
		x-=5
	elif right:
		x+=5
	if up:
		y+=5
	elif down:
		y-=5
	return [x,y]

def ship_gun(x,y,modifiers):
	#modifiers = stats
	#create bullet object/class if cooldown = 0
	bullet = b.bullet() #??, make var bullet an object bullet from bullet.py
	bullet.obj_x = x
	bullet.obj_y = y
	bullet.obj_vy = 10
	return bullet

def ship_melee(x,y,modifiers):
	#modifiers=stats
	#create melee class if cooldown = 0
	return attack

def ship_dash(x,y,left,right,up,down,modifiers):
	#modifiers=stats
	#dahses to a certain direction
	return [x,y]

