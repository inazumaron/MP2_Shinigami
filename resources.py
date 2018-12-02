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
player_sword.anchor_y = 0
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

bg_image = pyglet.resource.image("bg_1.png")
center_image(bg_image)
menu_image = pyglet.resource.image("menu_1.png")
center_image(menu_image)

dot_red = pyglet.resource.image("red_dot.png")
center_image(dot_red)
dot_blue = pyglet.resource.image("blue_dot.png")
center_image(dot_blue)