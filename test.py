from Functions.game import battle
from Functions.generate_character import Character, player_items, player_magic
from Classes.maps import dungeons


player = Character("Eric Stinson", 10, 500, 500, 500, 500, 500, player_magic, player_items)
player.display_stats()


battle(dungeons[9], player)
