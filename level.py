import pyglet
import enemy as enemy#

def get_enemy(time,difficulty,enemy_list):
	#check level
	if difficulty == 1:
		
		###comes in after 0 of a second and reappears every 5 seconds.
		if (time == 10 or time % 300 == 0) and time < 3600:
			print('0')
			enemy_list.append(enemy.Enemy_0(time,50))
			enemy_list.append(enemy.Enemy_0(time,175))
			enemy_list.append(enemy.Enemy_0(time,300))
			enemy_list.append(enemy.Enemy_0(time,425))
			enemy_list.append(enemy.Enemy_0(time,550))
		
		###comes in after 60 of a second and reappears every 10 seconds.
		if time >= 3600 and time % 300 == 0 and time < 7200:
			print('1')
			enemy_list.append(enemy.Enemy_1(time,50))
			enemy_list.append(enemy.Enemy_1(time,175))
			enemy_list.append(enemy.Enemy_1(time,300))
			enemy_list.append(enemy.Enemy_1(time,425))
			enemy_list.append(enemy.Enemy_1(time,550))

		###comes in after 30 seconds and reappears every 30 seconds.
		if time >= 1800 and time % 1800 == 0 and time < 7200:
			enemy_list.append(enemy.Enemy_2(time,50))
			enemy_list.append(enemy.Enemy_2(time,550))
			
		#spawns after 60 secs and respwans every 10 secs until 3 mins
		if time >= 3600 and time % 600 == 0 and time < 10800:
			enemy_list.append(enemy.Enemy_3(time,0))
			enemy_list.append(enemy.Enemy_3(time,600))

		#spawns after 90 secs and respwans every 10 secs until 3 mins
		if time >= 5400 and time % 600 == 0 and time < 10800:
			enemy_list.append(enemy.Enemy_4(time,0))
			enemy_list.append(enemy.Enemy_4(time,600))
		
		#spawns after 120 secs and respwans every 10 secs
		if time >= 7200 and time % 600 == 0:
			enemy_list.append(enemy.Enemy_5(time,50,800))
			enemy_list.append(enemy.Enemy_5(time,175,830))
			enemy_list.append(enemy.Enemy_5(time,300,850))
			enemy_list.append(enemy.Enemy_5(time,425,830))
			enemy_list.append(enemy.Enemy_5(time,550,800))	

		###comes in after 3 mins and reappears every 10 seconds
		if time >= 10800 and time % 600 == 0 and time < 18000:
			enemy_list.append(enemy.Enemy_6())
			enemy_list.append(enemy.Enemy_7())	

		###comes in after 6 mins and reappears every 20 seconds
		if time >= 14400 and time % 1200 == 0:
			enemy_list.append(enemy.Enemy_8(50))
			enemy_list.append(enemy.Enemy_8(550))
			
		###comes in after 7 mins and reappears every 30 seconds
		if time >= 18000 and time % 1800 == 0:
			enemy_list.append(enemy.Enemy_9())
			enemy_list.append(enemy.Enemy_10())

	return enemy_list
