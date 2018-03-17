from Classes.character import Character
from Classes.magic import magic_missile, heal, heal2, heal3, firebolt, sleep, paralyze
from Classes.inventory import weapons, inn_items, scrolls, staffs, potions, elixirs
from random import randint, choice
from Classes.npc import NPC

# Generate the player character
player_magic = [magic_missile, heal, sleep, firebolt, heal2, paralyze, heal3]
player_items = {"weapon": weapons[0], "items": [potions[0], elixirs[0]]}
shop_items = weapons


def initial_player():
    player_name = str(input("What is you name, adventurer? "))
    return Character(player_name, 10, 10, 10, 10, 10, 10, player_magic, player_items, 100)


# Generate a random character
first_name = ["Arthur", "Baxter", "Clark", "Dane", "Eric", "Frank", "Gary", "Hort", "Inigo", "Jok", "Larry", "Martin",
              "Nick", "Ork", "Paul", "Que", "Randy", "Stephen", "Terry", "Uncle Bart", "Victor", "Walter",
              "Xerxes", "Yank", "Zebulon"]
last_name = ["Adams", "Brown", "Clark", "Davis", "Evans", "Fisher", "Green", "Harris", "Ingram", "Johnson",
             "Lewis", "Miller", "Nelson", "Owen", "Paulson", "Quakers", "Robinson", "Smith", "Taylor", "Utley",
             "Vincent", "Williams", "Xavier", "Young", "Zaragoza"]
shop_phrase = "'Hello, welcome to my shop!'"
mayor_phrase = "WOULD YOU LIKE TO CONTINUE YOUR QUEST?"
inn_phrase = "'Good day! Would you like a room? or perhaps just a strong drink?'"
npc_phrase = "'Hello.'"


def random_npc(prof="npc"):
    char_name = choice(first_name) + " " + choice(last_name)
    if prof == "shop":
        rand = NPC(name=char_name, items=shop_items, money=1000, phrase=shop_phrase)
        return rand
    elif prof == "mayor":
        rand = NPC(name=char_name, items=[], money=100, phrase=mayor_phrase)
        return rand
    elif prof == "inn":
        rand = NPC(name=char_name, items=inn_items, money=200, phrase=inn_phrase)
        return rand
    else:
        rand = NPC(name=char_name, items=[], money=5, phrase=npc_phrase)
        return rand


def random_char(gold, m, w, x, a=1, b=8, c=12):
    char_name = choice(first_name) + " " + choice(last_name)
    r_str = randint(b, c) + a
    r_int = randint(b, c) + a
    r_dex = randint(b, c) + a
    r_wis = randint(b, c) + a
    r_cha = randint(b, c) + a
    r_con = randint(b, c) + a
    rand_char = Character(char_name, r_str, r_int, r_dex, r_wis, r_cha, r_con, m, w, gold, lvl=a, _id=x)
    rand_char.get_xp(5 * a)
    return rand_char

# Generate a new Player Character with a Higher Level


def level_player(char):
    new_lvl = char.lvl + 1
    n_str = char.str + randint(0, 5) + 1
    n_int = char.int + randint(0, 5) + 1
    n_dex = char.dex + randint(0, 5) + 1
    n_wis = char.wis + randint(0, 5) + 1
    n_cha = char.cha + randint(0, 5) + 1
    n_con = char.con + randint(0, 5) + 1
    new = Character(char.name, n_str, n_int, n_dex, n_wis, n_cha, n_con, char.magic, char.items, money=char.money, lvl=new_lvl)
    new.quest = char.quest
    return new


def check_xp(char):
    lvl = char.lvl
    print("CURRENT XP: {}".format(char.xp))
    if char.xp < 10 * lvl:
        print("NO LEVEL GAINED")
        return char
    elif char.xp >= 10 * lvl:
        char.xp -= 10 * lvl
        print("NEW XP: {}".format(char.xp))
        new_char = level_player(char)
        new_char.xp = char.xp
        print("Your power has increased!")
        return new_char


def random_bandit(char):
    lvl = char.lvl
    gold = 10 * lvl
    band = random_char(gold, [], {"weapon":char.items["weapon"]}, a=lvl, x="bandit")
    return band
