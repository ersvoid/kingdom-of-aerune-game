from Classes.character import Character
from Classes.magic import magic_missile, heal
from Classes.inventory import weapons, potions, elixirs, scrolls, staffs
from random import randint, choice
from Classes.npc import NPC

# Generate the player character
player_magic = [magic_missile, heal]
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
mayor_phrase = "'Hello, I am the leader of this town.'"
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
        rand = NPC(name=char_name, items=[potions, elixirs], money=200, phrase=inn_phrase)
        return rand
    else:
        rand = NPC(name=char_name, items=[], money=5, phrase=npc_phrase)
        return rand


def random_char(gold, m, w, a=1, b=5, c=12):
    char_name = choice(first_name) + " " + choice(last_name)
    r_str = randint(b, c) + a
    r_int = randint(b, c) + a
    r_dex = randint(b, c) + a
    r_wis = randint(b, c) + a
    r_cha = randint(b, c) + a
    r_con = randint(b, c) + a
    rand_char = Character(char_name, r_str, r_int, r_dex, r_wis, r_cha, r_con, m, w, gold, lvl=a)
    rand_char.get_xp(10 * a)
    return rand_char

# Generate a new Player Character with a Higher Level


def level_player(char):
    char.lvl += 1
    n_str = char.str + randint(0, 5) + 1
    n_int = char.int + randint(0, 5) + 1
    n_dex = char.dex + randint(0, 5) + 1
    n_wis = char.wis + randint(0, 5) + 1
    n_cha = char.cha + randint(0, 5) + 1
    n_con = char.con + randint(0, 5) + 5
    new = Character(char.name, n_str, n_int, n_dex, n_wis, n_cha, n_con, char.magic, char.items, char.money)
    new.quest = char.quest
    new.lvl = char.lvl
    return new


def check_xp(char):
    lvl = char.lvl
    if char.xp < 10 * lvl:
        return char
    elif char.xp >= 10 * lvl:
        char = level_player(char)
        print("Your power has increased!")
        char.xp = 0
        return char
