from Classes.character import Character
from Classes.magic import magic_missile, heal, heal2, heal3, firebolt, sleep, paralyze
from Classes.inventory import weapons, inn_items, scrolls, staffs, potions, elixirs, armors
from random import randint, choice
from Classes.npc import NPC

# Generate the player character
player_magic = [magic_missile, heal, sleep, firebolt, heal2, paralyze, heal3]
player_items = {"weapon": weapons[0], "items": [potions[0], elixirs[0], scrolls[0]], "armor": armors[0]}
shop_items = weapons
profs = ["Spellsword", "Warden", "Sorceror"]


def initial_player():
    player_first = str(input("What is your first name, adventurer? "))
    player_last = str(input("What is your last name, adventurer? "))
    player_name = player_first + " " + player_last
    char = Character(player_name, 10, 10, 10, 10, 10, 10, player_magic, player_items, money=100)
    c = 1
    for i in profs:
        print("{}. {}".format(c, i))
        c += 1
    val = input("What is your profession, {}?".format(player_name))
    while val == "":
        val = input("'Well?'")
    while not val.isdigit():
        val = input("'Well?' ")
    while int(val) < 1:
        val = input("'Well?' ")
    while int(val) > 3:
        val = input("Well? ")
    val = int(val) - 1
    char.profession(val)
    return char


# Generate a random character
first_name = ["Arthur", "Brock", "Connor", "Dane", "Eric", "Frank", "Gary", "Harry", "Ivan", "Jack", "Larry", "Martin",
              "Nick", "Owen", "Paul", "Quinn", "Randy", "Stephen", "Terry", "Ulysses", "Victor", "Walter",
              "Xerxes", "Youngblood", "Zebulon"]
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
    elif prof == "arm":
        rand = NPC(name=char_name, items=armors, money = 200, phrase=shop_phrase)
        return rand
    else:
        rand = NPC(name=char_name, items=[], money=5, phrase=npc_phrase)
        return rand


def random_char(gold, m, w, x, a=1, b=8, c=12):
    char_name = choice(first_name) + " " + choice(last_name)
    r_str = randint(b, c)
    r_int = randint(b, c)
    r_dex = randint(b, c)
    r_wis = randint(b, c)
    r_cha = randint(b, c)
    r_con = randint(b, c)
    rand_char = Character(char_name, r_str, r_int, r_dex, r_wis, r_cha, r_con, m, w, money=gold, lvl=a, _id=x)
    rand_char.get_xp(5 * a)
    return rand_char

# Generate a new Player Character with a Higher Level


def level_player(char):
    new_lvl = char.lvl + 1
    if char.prof == "Spellsword":
        n_str = char.str + 0.25
        n_int = char.int + 0
        n_dex = char.dex + 1
        n_wis = char.wis + 0.5
        n_cha = char.cha + 0
        n_con = char.con + 0.25
        new = Character(char.name, n_str, n_int, n_dex, n_wis, n_cha, n_con, char.magic, char.items,
                        money=char.money,
                        lvl=new_lvl, prof="Spellsword")
        new.quest = char.quest
        return new
    elif char.prof == "Warden":
        n_str = char.str + 0.5
        n_int = char.int + 0
        n_dex = char.dex + 0.25
        n_wis = char.wis + 0.25
        n_cha = char.cha + 0
        n_con = char.con + 1
        new = Character(char.name, n_str, n_int, n_dex, n_wis, n_cha, n_con, char.magic, char.items,
                        money=char.money,
                        lvl=new_lvl, prof="Warden")
        new.quest = char.quest
        return new
    elif char.prof == "Sorceror":
        n_str = char.str + 0.25
        n_int = char.int + 0
        n_dex = char.dex + 0.25
        n_wis = char.wis + 1
        n_cha = char.cha + 0
        n_con = char.con + 0.5
        new = Character(char.name, n_str, n_int, n_dex, n_wis, n_cha, n_con, char.magic, char.items,
                        money=char.money,
                        lvl=new_lvl, prof="Sorceror")
        new.quest = char.quest
        return new


def check_xp(char):
    lvl = char.lvl
    print("CURRENT XP: {}".format(char.xp))
    if char.xp < 10 * lvl:
        print("You will need to keep training to gain a level.")
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
    band = random_char(gold, [], {"weapon":weapons[1], "armor":armors[0], "items": potions[0]}, a=lvl, x="bandit")
    return band
