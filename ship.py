import pyglet
import math
import bullet as b
import gui as gui

def ship_move(x,y,left,right,up,down,speed):
	#Change coordinates as necessary
	#check if outside boundary

	if left and 50 < x: ###While the ship is still within the boundaries(50 < x < 550 and 50 < y < 750), move the ship by 'speed' distance.
		x-=speed
	elif right and x < 550:
		x+=speed
	if up and y < 750:
		y+=speed
	elif down and 50 < y:
		y-=speed
	return [x,y]

def ship_gun(x,y,ex,ho,pi,dam):
	#modifiers = stats
	#create bullet object/class if cooldown = 0
	bullet = b.bullet() #??, make var bullet an object bullet from bullet.py
	bullet.obj_x = x
	bullet.obj_y = y
	bullet.obj_vy = 10
	bullet.modifiers["explosive"] = ex
	bullet.modifiers["homing"] = ho
	bullet.modifiers["piercing"] = pi
	bullet.damage = dam
	return bullet

def ship_dash(x,y,left,right,up,down,modifiers,dis):
	#modifiers=stats
	#dahses to a certain direction
	if left and up and x >= 100 and y <= 700:		###If the ship is at least 'dis' distance away from the boundary,
		x -= dis 									### dash by 'dis' distance.
		y += dis

	elif left and up and x < 100 and y > 700:		###If dash distance goes over the boundary
		x = 50										###just teleport to the corner/side so it won't go out of bounds.	
		y = 750

	elif left and down and x >= 100 and y >= 100:
		x -= dis
		y -= dis

	elif left and down and x < 100 and y < 100:
		x = 50
		y = 50

	elif right and up and x <= 500 and y <= 700:
		x += dis
		y += dis

	elif right and up and x > 500 and y > 700:
		x = 550
		y = 750

	elif right and down and x <= 500 and y >= 100:
		x += dis
		y -= dis

	elif right and down and x > 500 and y < 100:
		x = 550
		y = 100
	
	elif left and x >= 100:
		x -= dis

	elif left and x < 100:
		x = 50

	elif right and x <= 500:
		x += dis

	elif right and x > 500:
		x = 550

	elif up and y <= 700:
		y += dis

	elif up and y > 700:
		y = 750

	elif down and y >= 100:
		y -= dis

	elif down and y < 100:
		y = 50
				
	return [x,y]
