from Functions.generate_character import random_bandit, check_xp
from Classes.maps import Location
from Classes.inventory import Item, display_shop_menu, player_choice, generate_scroll, enchant_weapon, enchantment_check

choices = ["1. Attack", "2. Magic", "3. Items", "4. Run"]


def display_board(player, enemy):
    print("                HP           MP")
    print("{}   {}/{}        {}/{}".format(player.name, player.hp, player.maxhp, player.mp, player.maxmp))
    print("{}   {}/{}        {}/{}".format(enemy.name, enemy.hp, enemy.maxhp, enemy.mp, enemy.maxmp))


def death(char):
    if char.death_check():
        return True


def sleep_check(enemy, player):
    if death(enemy):
        return
    if enemy.sleep:
        print("The enemy is sleeping.")
        enemy.take_damage(player.items["weapon"].item_value() + player.get_str())
        save = enemy.will()
        spell = player.get_wis()
        if save < spell:
            print("Your opponent is still sleeping!")
        else:
            enemy.sleep = False
            print("Your opponent has woken up!")
            return enemy.sleep


def fire_check(enemy):
    if death(enemy):
        return
    save = enemy.reflex()
    if save > 15:
        enemy.fire = 0
        return enemy.fire
    if enemy.fire > 0:
        print("The enemy is on fire!")
        enemy.take_damage(5)
        enemy.fire -= 1
        return enemy.fire


def player_turn(player, enemy):
    if death(player) or death(enemy):
        return
    for c in choices:
        print(c)
    choice = input("'Well?' ")
    while choice == "":
        choice = input("'Well?'")
    while not choice.isdigit():
        choice = input("'Well?' ")
    choice = int(choice)
    if choice == 1:
        if player.items["weapon"].elem == "Magic":
            if player.attack() + 5 > enemy.ac_rating():
                enemy.take_damage(player.damage() + 10)
        elif player.items["weapon"].elem == "Fire":
            if player.attack() > enemy.ac_rating():
                enemy.fire = 5
                enemy.take_damage(player.damage())
        elif player.items["weapon"].elem == "Death":
            if enemy.will() < player.will():
                enemy.hp = 0
                print("A black ray pierces the heart of your enemy...")
            else:
                enemy.take_damage(player.magic[choice].get_val())
        else:
            if player.attack() > enemy.ac_rating():
                enemy.take_damage(player.damage())
            else:
                print(player.name, " missed!")
    elif choice == 2:
        c = 1
        for m in player.magic:
            print("{}. {} for {} MP".format(c, m.name, m.cost))
            c += 1
        choice = input("'Well?' ")
        while choice == "":
            choice = input("'Well?'")
        while not choice.isdigit():
            choice = input("'Well?' ")
        choice = int(choice) - 1
        mana = player.magic[choice].cost
        if player.mp - mana < 0:
            print("Spell failed...")
        else:
            player.take_mp(mana)
            if player.magic[choice].type == "attack":
                if player.magic[choice].elem == "Fire":
                    enemy.fire = 5
                    enemy.take_damage(player.magic[choice].get_val())
                elif player.magic[choice].elem == "Death":
                    if enemy.will() < player.will():
                        enemy.hp = 0
                        print("A black ray pierces the heart of your enemy...")
                    else:
                        print("A black ray shoots from your fingers...")
                        enemy.take_damage(player.magic[choice].get_val())
                else:
                    enemy.take_damage(player.magic[choice].get_val())
            elif player.magic[choice].type == "heal":
                player.heal(player.magic[choice].get_val())
            elif player.magic[choice].type == "alter":
                if enemy.will() >= player.will():
                    print("Your opponent is unaffected by your spell.")
                else:
                    enemy.sleep += player.magic[choice].get_val()
                    print("The enemy is sleeping.")
    elif choice == 3:
        c = 1
        for i in player.items["items"]:
            print("{}. {}".format(c, i.name))
            c += 1
        choice = input("'Well?' ")
        while choice == "":
            choice = input("'Well?'")
        while not choice.isdigit():
            choice = input("'Well?' ")
        choice = int(choice) - 1
        p_item = player.items["items"][choice]
        if not p_item.check_item():
            print("You have no more of that item!")
        else:
            if p_item.type == "potion":
                player.heal(p_item.item_value())
            elif p_item.type == "elixir":
                player.rest(p_item.item_value())
            elif p_item.type == "scroll":
                if p_item.elem == "Fire":
                    enemy.fire = 5
                    enemy.take_damage(p_item.item_value())
                elif p_item.elem == "Magic":
                    enemy.take_damage(p_item.item_value())
                elif p_item.elem == "Heal":
                    player.heal(p_item.item_value())
                elif p_item.elem == "Death":
                    if enemy.will() < player.will():
                        enemy.hp = 0
                        print("A black ray pierces the heart of your enemy...")
                    else:
                        print("A black ray shoots from your fingers...")
                        enemy.take_damage(p_item.item_value())
                elif p_item.elem == "Alter":
                    if enemy.will() >= player.will():
                        print("Your opponent is unaffected by your spell.")
                    else:
                        enemy.sleep = 5
                        print("The enemy is sleeping.")
            p_item.use_item()
            if not p_item.check_item():
                p_item.__del__()
                player.items["items"].remove(p_item)
    elif choice == 4:
        print("You try to run but cannot escape!")
    else:
        choice = input("Your turn: ")


b_potions = True
b_elixirs = True


def enemy_turn(enemy, player):
    global b_potions, b_elixirs
    if death(enemy) or death(player):
        return
    if enemy.sleep:
        return
    if enemy.id == "bandit":
        if player.ac_rating() < enemy.attack():
            print(enemy.name, " attacks ", player.name)
            player.take_damage(enemy.damage())
        else:
            print(enemy.name, " missed!")
    elif enemy.id == "leader":
        if (enemy.hp / enemy.maxhp) * 100 < 30:
            if not b_potions:
                if player.ac_rating() < enemy.attack():
                    print(enemy.name, " attacks ", player.name)
                    player.take_damage(enemy.damage())
                else:
                    print(enemy.name, " missed!")
            else:
                enemy.heal((enemy.items["potions"].item_value()))
                enemy.items["potions"].use_item()
                b_potions = False
                return b_potions
        else:
            if player.ac_rating() < enemy.attack():
                print(enemy.name, " attacks ", player.name)
                player.take_damage(enemy.damage())
            else:
                print(enemy.name, " missed!")
    elif enemy.id == "wizard":
        if (enemy.hp / enemy.maxhp) * 100 < 30:
            if not b_potions:
                if enemy.items["weapon"].elem == "Magic":
                    player.take_damage(enemy.damage())
                    print("The enemy has cast magic missile!")
                elif enemy.items["weapon"].elem == "Fire":
                    player.fire += 5
                    player.take_damage(enemy.damage())
                    print("The player has caught on fire!")
                elif enemy.items["weapon"].elem == "Alter":
                    val = enemy.damage()
                    if val > player.will():
                        player.sleep = True
                        print("The player has fallen asleep!")
                    else:
                        print("Enemy spell failed.")
                elif enemy.items["weapon"].elem == "Death":
                    if enemy.will() > player.will():
                        player.hp = 0
                        print("A black ray pierces your heart!")
                    else:
                        player.take_damage(enemy.damage())
                        print("A black mist chokes you..")
            else:
                enemy.heal((enemy.items["potions"].item_value()))
                enemy.items["potions"].use_item()
                b_potions = False
                return b_potions
        elif (enemy.mp / enemy.maxmp) * 100 < 30:
            if not b_elixirs:
                if enemy.items["weapon"].elem == "Magic":
                    player.take_damage(enemy.damage())
                    print("The enemy has cast magic missile!")
                elif enemy.items["weapon"].elem == "Fire":
                    player.fire += 5
                    player.take_damage(enemy.damage())
                    print("The player has caught on fire!")
                elif enemy.items["weapon"].elem == "Alter":
                    val = enemy.damage()
                    if val > player.will():
                        player.sleep = True
                        print("The player has fallen asleep!")
                    else:
                        print("Enemy spell failed.")
                elif enemy.items["weapon"].elem == "Death":
                    if enemy.will() > player.will():
                        player.hp = 0
                        print("A black ray pierces your heart!")
                    else:
                        player.take_damage(enemy.damage())
                        print("A black mist chokes you..")
            else:
                enemy.heal((enemy.items["elixirs"].item_value()))
                enemy.items["elixirs"].use_item()
                b_elixirs = False
                return b_elixirs
        else:
            if enemy.items["weapon"].elem == "Magic":
                player.take_damage(enemy.damage())
                print("The enemy has cast magic missile!")
            elif enemy.items["weapon"].elem == "Fire":
                player.fire += 5
                player.take_damage(enemy.damage())
                print("The player has caught on fire!")
            elif enemy.items["weapon"].elem == "Alter":
                val = enemy.damage()
                if val > player.will():
                    player.sleep = True
                    print("The player has fallen asleep!")
                else:
                    print("Enemy spell failed.")
            elif enemy.items["weapon"].elem == "Death":
                if enemy.will() > player.will():
                    player.hp = 0
                    print("A black ray pierces your heart!")
                else:
                    player.take_damage(enemy.damage())
                    print("A black mist chokes you..")


def battle(loc, player):
    global battle_on, _round
    enemy = loc.pop[0]
    print("{} has entered the arena.".format(enemy.name))
    player_init = player.ac_rating()
    enemy_init = enemy.ac_rating()
    _round = True
    while _round:
        display_board(player, enemy)
        if death(enemy) or death(player):
            break
        sleep_check(enemy, player)
        fire_check(enemy)
        if player_init > enemy_init:
            print("You are faster.")
            player_turn(player, enemy)
            if death(enemy):
                break
            enemy_turn(enemy, player)
        elif player_init < enemy_init:
            print("Your opponent is faster.")
            enemy_turn(enemy, player)
            if death(player):
                break
            player_turn(player, enemy)
    print("ROUND OVER!!!!")
    if player.hp <= 0:
        print("You are dead.")
        return False
    else:
        print("You have won this battle!")
        player.win_gold(enemy.money)
        player.get_xp(enemy.xp)
        print("You have gained {} XP.".format(enemy.xp))
        loc.pop.pop(0)
        return True


def continue_screen():
    print("\n")
    input("press any key to continue")
    print("\n")


def welcome_screen():
    print("""Welcome to the Kingdom of Aerune!  You have made your way to the outskirts of the empire, where wilderness 
and wonder await any brave adventurer.  You disembark from the carriage and set down the footpath towards the 
town in the distance.  The town is small, with no protective walls or towers.  These people are completely 
exposed to the elements and dangers of the wild.""")
    continue_screen()


def game_screen(loc, char):
    c = 1
    print("You stand on the dirt street.")
    for l in loc.lst:
        print("{}. {}".format(c, l.name))
        c += 1
    num = len(loc.lst) + 1
    print("{}. Patrol Town".format(num))
    print("{}. Compose Spell".format(num + 1))
    if char.lvl > 4:
        print("{}. Enchant Weapon".format(num + 2))
    val = input("Choose one: ")
    while val == "":
        val = input("Choose one: ")
    while not val.isdigit():
        val = input("Choose one: ")
    else:
        val = int(val) - 1
    while val < 0 or val > num + 2:
        val = int(input("Choose: "))
    else:
        return val


def quest_func(loc, player):
    global battle_on
    print("\n")
    print(loc.i1)
    continue_screen()
    print(loc.i2)
    continue_screen()
    print(loc.i3)
    continue_screen()
    loc.__str__()
    battle_on = True
    print("\n")
    while battle_on:
        val = battle(loc, player)
        if val:
            player.quest += 1
            continue_screen()
            print(loc.o1)
            continue_screen()
            print(loc.o2)
            continue_screen()
            battle_on = False
            return battle_on
        else:
            break
    battle_on = False
    return battle_on


def shopping(loc, player):
    global shop_on
    loc.__str__()
    loc.pop[0].talk()
    print("You have " + str(player.money) + "gp.")
    print("1. Buy")
    print("2. Sell")
    print("3. Goodbye")
    val = input("'What\'ll it be then?' ")
    while val == "":
        val = input("'What\'ll it be then?'")
    while not val.isdigit():
        val = input("'I don't understand yer fancy inner-empire speak! ")
    val = int(val)
    if val == 1:
        print("You have " + str(player.money) + "gp.")
        loc.pop[0].sell(player)
    elif val == 2:
        print("You have " + str(player.money) + "gp.")
        loc.pop[0].buy(player)
    elif val == 3:
        shop_on = False
        return shop_on
    else:
        int(input("'What did you say?' "))


def innkeeper(loc, player):
    global inn_on
    loc.__str__()
    loc.pop[0].talk()
    print("1. 'I'd like a room for the night, sir.'")
    print("2. 'Give me a drink for the road.'")
    print("3. 'Nothing for me..'")
    val = input("'Well?' ")
    while val == "":
        val = input("'Well?' ")
    while not val.isdigit():
        val = input("Number: ")
    val = int(val)
    if val == 1:
        print("'That'll be 25gp.'")
        if player.money < 25:
            print("'Get out of here!'")
            inn_on = False
            return inn_on
        else:
            print("'Here take this key. Give it back when you're done.'")
            player.spend_gold(25)
            player.reset()
            print("You spend the night at the inn and wake up feeling refreshed.")
            inn_on = False
            return inn_on
    elif val == 2:
        print("You have " + str(player.money) + "gp.")
        display_shop_menu()
        drink = player_choice()
        if drink.cost > player.money:
            print("NO SALE")
        else:
            print("1 is yes. 2 is no.")
            y_n = input("That'll be {} gp. Cool? ".format(drink.cost))
            while y_n == "":
                y_n = input("'Well?'")
            while not y_n.isdigit():
                y_n = input("'Well?' ")
            y_n = int(y_n)
            if y_n == 1:
                loc.pop[0].sell_drink(player, drink)
            else:
                pass
    elif val == 3:
        print("The innkeeper waves goodbye.")
        inn_on = False
        return inn_on
    else:
        int(input("'Well?' "))


def housing(loc):
    global house_on
    loc.__str__()
    loc.pop[0].talk()
    house_on = False
    return house_on


a1 = "'Please accept this bounty as a gift of our gratitude.'"
c1 = "'Thank you!'"
d1 = "'Thank you again for your help.'"


def mayor_hall(loc, player, dungeon, a=a1, b=100, c=c1, d=d1):
    global hall_on
    loc.__str__()
    if player.quest == 0:
        print("Will you help the village with their bandit problem?")
        print("1. Yes")
        print("2. No")
        val = input("'Well?' ")
        while val == "":
            val = input("'Well?'")
        while not val.isdigit():
            val = input("'Well?' ")
        val = int(val)
        if val == 1:
            print(d)
            hall_on = False
            quest_func(dungeon, player)
        elif val == 2:
            print("Goodbye.")
            hall_on = False
            return hall_on
        else:
            int(input("'Well?' "))
    elif player.quest == 20:
        print("'The people of both frontier towns thank you for your protection.'")
        hall_on = False
        return hall_on
    elif player.quest % 2 != 0:
        print(a)
        player.win_gold(b)
        return True
    elif player.quest % 2 == 0:
        print(d)
        loc.pop[0].talk()
        print("1. Yes")
        print("2. No")
        val = input("'Well?' ")
        while val == "":
            val = input("'Well?'")
        while not val.isdigit():
            val = input("'Well?' ")
        val = int(val)
        if val == 1:
            print(c)
            hall_on = False
            quest_func(dungeon, player)
            return hall_on
        elif val == 2:
            print("Goodbye.")
            hall_on = False
            return hall_on
        else:
            int(input("'Well?' "))


shop_on = False
inn_on = False
house_on = False
battle_on = False
hall_on = False
questing = False


def compose(char):
    print("You pull out your parchment and quill and set about composing a spell for later.")
    c = 1
    for spell in char.magic:
        print("{}. {}".format(c, spell.name))
        c += 1
    val = input("Choose: ")
    while val == "":
        val = input("'Well?'")
    while not val.isdigit():
        val = input("'Well?' ")
    val = int(val) - 1
    p_spell = char.magic[val]
    if p_spell.cost > char.mp:
        print("You are too tired.")
    else:
        char.mp -= p_spell.cost
        print("You begin to draft your scroll.")
        scroll = generate_scroll(p_spell)
        temp_var = char.items["items"]
        temp_var.append(scroll)
        char.items["items"] = temp_var
        print("You have created a {}!".format(scroll.name))
        return char.items, char.mp


def run_village(player, town, shop, inn, house, hall, dungeon):
    global shop_on, inn_on, house_on, battle_on, hall_on, questing
    val = game_screen(town, player)
    print("\n")
    if val == 0:
        shop_on = True
    elif val == 1:
        inn_on = True
    elif val == 2:
        house_on = True
    elif val == 3:
        hall_on = True
    elif val == 4:
        print("You feel compelled to make a name for yourself...")
        bandit = random_bandit(player)
        p1_intro = ""
        battle_ground = Location("PATROL", "p1", p1_intro, [bandit], [])
        battle(battle_ground, player)
        return False
    elif val == 5:
        compose(player)
        return False
    elif val == 6:
        enchant_weapon(player)
    else:
        int(input("Choose one: "))
    while shop_on:
        shopping(shop, player)
    while inn_on:
        innkeeper(inn, player)
    while house_on:
        housing(house)
    while hall_on:
        _bool = mayor_hall(hall, player, dungeon)
        if _bool:
            return True


def town_game(player, town, shop, inn, house, hall, dungeon):
    _bool = run_village(player, town, shop, inn, house, hall, dungeon)
    if _bool:
        return True
    else:
        return False


def dungeon_lvl(player):
    if player.quest < 2:
        return 0
    elif player.quest < 4:
        return 1
    elif player.quest < 6:
        return 2
    elif player.quest < 8:
        return 3
    elif player.quest < 10:
        return 4
    elif player.quest < 12:
        return 5
    elif player.quest < 14:
        return 6
    elif player.quest < 16:
        return 7
    elif player.quest < 18:
        return 8
    elif player.quest < 20:
        return 9


def game_stage(player, towns, shops, inns, houses, halls, dungeons):
    lvl = dungeon_lvl(player)
    game_on = True
    towns[0].__str__()
    print("\n")
    while game_on:
        _bool = town_game(player, towns[0], shops[0], inns[0], houses[0], halls[0], dungeons[lvl])
        if _bool:
            return True
        else:
            return False
