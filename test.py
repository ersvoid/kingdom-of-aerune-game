from Functions.game import battle
from Functions.generate_character import initial_player, random_char, check_xp
from Classes.inventory import short_sword
from Classes.maps import dungeons

player = initial_player()
opponent = dungeons[0].pop[0]
player.display_stats()
opponent.display_stats()
battle(dungeons[0], player)
player = check_xp(player)
player.display_stats()
