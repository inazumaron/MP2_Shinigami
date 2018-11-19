import pyglet

class level(object):
	"""docstring for level"""
	def __init__(self, arg):
		super(level, self).__init__()
		self.time_elapse = 0
		self.difficulty = 0
		

def get_enemy(level,enemy_list):
	#check level
	return enemy_list