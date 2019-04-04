from Functions.game import battle
from Functions.generate_character import player_items, player_magic, check_xp
from Classes.maps import q9_dung
from Classes.character import Character

player = Character("Aeric Greene", 50, 50, 50, 50, 50, 50, player_magic, player_items, money=100)
player.maxhp = 1000
player.maxmp = 1000
player.reset()


battle(q9_dung, player)



