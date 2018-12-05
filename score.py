import os
filepath =  os.path.normpath('resc/scores.txt')

def get_scores():
	#get scores from file
	scores = list()
	with open(filepath) as file:
		line = file.readline().strip()
		while line:
			temp = int(line)
			scores.append(temp)
			line = file.readline().strip()
	return scores

def add_score(score):
	#add to file
<<<<<<< HEAD
	name = input("Input your name: ")
	scores = get_scores()
	scores[name]=score
	with open(filepath, 'r') as file:
		# read a list of lines into data
    		data = file.readlines()
	temp = ''.join(data).split(name+':'+str(scores[name])+'\n')
	data = temp[0] + name+':'+str(score)+'\n' + temp[1]
	with open(filepath, 'w') as file:
		#writes back to file
		file.add(data)
	scores[name]=score
=======
	data = list()
	with open(filepath, 'r') as file:
		# read a list of lines into data
		line = file.readline().strip()
		while line:
			temp = int(line)
			data.append(temp)
			line = file.readline().strip()
	if score > 0:
		data.append(score)
	data.sort(reverse = True)
	if len(data) > 10:
		data = data[:10]
	scores = ''
	for n in data:
		scores += str(n) + '\n'
	scores.strip()
	with open(filepath, 'w') as file:
		#writes back to file
		file.writelines(scores)
>>>>>>> 0ea248cd2325bd22d4840455da76482aa8b79f64
