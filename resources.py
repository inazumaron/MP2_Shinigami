import pyglet


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Tell pyglet where to find the resources
pyglet.resource.path = ['resc']
pyglet.resource.reindex()

# Load the three main resources and get them to draw centered
cover_image = pyglet.resource.image("cover_1.jpg")
center_image(cover_image)

button_start = pyglet.resource.image("start.png")
center_image(button_start)
button_continue = pyglet.resource.image("continue.png")
center_image(button_continue)
button_ng = pyglet.resource.image("ng.png")
center_image(button_ng)
button_score = pyglet.resource.image("score.png")
center_image(button_score)
button_help = pyglet.resource.image("help.png")
center_image(button_help)

cursor_1 = pyglet.resource.image("cursor.png")
center_image(cursor_1)

player_image = pyglet.resource.image("player_small_no_sword.png")
center_image(player_image)
player_image_shield = pyglet.resource.image("player_shield.png")
center_image(player_image_shield)
player_image_dash = pyglet.resource.image("player_dash.png")
center_image(player_image_dash)
player_image_shield_dash = pyglet.resource.image("player_shield_dash.png")
center_image(player_image_shield_dash)
player_sword = pyglet.resource.image("sword.png")
player_sword.anchor_y = player_sword.height
player_sword.anchor_x = player_sword.width / 2

bullet_enemy = pyglet.resource.image("bullet_e.png")
center_image(bullet_enemy)
bullet_player = pyglet.resource.image("bullet_p.png")
center_image(bullet_player)
bullet_homing = pyglet.resource.image("bullet_h.png")
center_image(bullet_homing)
bullet_explosive = pyglet.resource.image("bullet_x.png")
center_image(bullet_explosive)
bullet_piercing = pyglet.resource.image("bullet_i.png")
center_image(bullet_piercing)
bullet_exhoming = pyglet.resource.image("bullet_he.png")
center_image(bullet_exhoming)
bullet_explosion = pyglet.resource.image("explosion.png")
center_image(bullet_explosion)

enemy_1_image = pyglet.resource.image("enemy_small.png")
center_image(enemy_1_image)
enemy_2_image = pyglet.resource.image("enemy_2.png")
center_image(enemy_2_image)
enemy_3_image = pyglet.resource.image("enemy_3.png")
center_image(enemy_3_image)
enemy_4_image = pyglet.resource.image("enemy_4.png")
center_image(enemy_4_image)
enemy_5_image = pyglet.resource.image("enemy_5.png")
center_image(enemy_5_image)
enemy_6_image = pyglet.resource.image("enemy_6.png")
center_image(enemy_6_image)
enemy_7_image = pyglet.resource.image("enemy_7.png")
center_image(enemy_7_image)
enemy_8_image = pyglet.resource.image("enemy_8.png")
center_image(enemy_8_image)
enemy_9_image = pyglet.resource.image("enemy_9.png")
center_image(enemy_9_image)
enemy_10_image = pyglet.resource.image("enemy_10.png")
center_image(enemy_10_image)

buff_axe_image = pyglet.resource.image("buff_axe.png")
center_image(buff_axe_image)
buff_dash_c_image = pyglet.resource.image("buff_dash_c.png")
center_image(buff_dash_c_image)
buff_dash_d_image = pyglet.resource.image("buff_dash_d.png")
center_image(buff_dash_d_image)
buff_explosive_image = pyglet.resource.image("buff_explosive.png")
center_image(buff_explosive_image)
buff_homing_image = pyglet.resource.image("buff_homing.png")
center_image(buff_homing_image)
buff_life_image = pyglet.resource.image("buff_life.png")
center_image(buff_life_image)
buff_piercing_image = pyglet.resource.image("buff_piercing.png")
center_image(buff_piercing_image)
buff_shield_l_image = pyglet.resource.image("buff_shield_l.png")
center_image(buff_shield_l_image)
buff_shield_r_image = pyglet.resource.image("buff_shield_r.png")
center_image(buff_shield_r_image)
buff_spear_image = pyglet.resource.image("buff_spear.png")
center_image(buff_spear_image)
buff_speed_image = pyglet.resource.image("buff_speed.png")
center_image(buff_speed_image)
buff_sword_image = pyglet.resource.image("buff_sword.png")
center_image(buff_sword_image)

lvl_up_image = pyglet.resource.image("lvl.png")
center_image(lvl_up_image)

bg_image = pyglet.resource.image("bg_1.png")
center_image(bg_image)
menu_image = pyglet.resource.image("menu_1.png")
center_image(menu_image)

square_red = pyglet.resource.image("red_square.png")
center_image(square_red)
square_blue = pyglet.resource.image("blue_square.png")
center_image(square_blue)

#explosion_fx = pyglet.resource.media('explosion_sound_effect.wav', streaming=False)
#sword_fx = pyglet.resource.media('sword_sound_effect.wav', streaming=False)
#bg_music = pyglet.resource.media('bg_music.wav', streaming=False)
