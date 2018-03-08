from Functions.game import battle
from Functions.generate_character import initial_player, random_char, check_xp
from Classes.inventory import short_sword
from Classes.maps import dungeons

player = initial_player()
player.display_stats()
player.xp = 10
player = check_xp(player)
player.display_stats()