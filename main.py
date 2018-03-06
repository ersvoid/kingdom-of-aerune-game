from Functions.generate_character import initial_player, check_xp
from Functions.game import welcome_screen, game_stage
from Classes.maps import towns, houses, inns, shops, halls, dungeons


game_start = True
while game_start:
    player = initial_player()
    welcome_screen()
    gaming = True
    while gaming:
        level_one = True
        while level_one:
            _bool = game_stage(player, towns, shops, inns, houses, halls, dungeons)
            if _bool:
                player.quest += 1
                player = check_xp(player)
                print(player.quest)
