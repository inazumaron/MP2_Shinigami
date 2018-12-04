import os
filepath =  os.path.normpath('resc/scores.txt')

def get_scores():
	#get scores from file
	scores = {"name":0} #format must be like this (0 is the score)
	scores = dict()
	with open(filepath) as fp:
        	line = fp.readline().strip()
        	while line:
        		temp = line.split(':')
        		scores[temp[0]] = int(temp[1])
        		line = fp.readline().strip()
	#scores = {"name":0} #format must be like this (0 is the score)
	return scores

def add_score(name, score):
	#add to file
	scores = get_scores()
	scores[name]=score
	with open(filepath, 'r') as file:
		# read a list of lines into data
    		data = file.readlines()
	data[data.index(name+':'+str(scores[name]))+'\n'] = name+':'+str(score)+'\n'
	scores[name]=score