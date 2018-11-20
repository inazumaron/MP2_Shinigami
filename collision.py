import math

def get_distance(x1,y1,x2,y2):
	distance = sqrt(((x1-x2)**2)+((y1-y2)**2))
	return distance

def check_collision(x1,x2,w1,w2,y1,y2,h1,h2):
	distance_x = abs(x1-x2)
	distance_y = abs(y1-y2)
	if ((w1+w2)/2)<distance_x and ((h1+h2)/2)<distance_y:
		return True
	else:
		return False