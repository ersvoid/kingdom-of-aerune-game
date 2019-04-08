from random import randint, choice
import string
from Classes.magic import spells


class Item:
    def __init__(self, name, val, cost, _type, amount=1, element="None", material="None", _id="None"):
        self.name = name
        self.val = val
        self.cost = cost
        self.type = _type
        self.amt = amount
        self.elem = element
        self.mat = material
        self.id = _id

    def item_value(self):
        return self.val

    def get_type(self):
        return self.type

    def __del__(self):
        return

    def check_item(self):
        if self.amt == 0:
            return False
        else:
            return True

    def use_item(self):
        self.amt -= 1
        return self.amt

    def special(self):
        if self.elem is None:
            pass
        else:
            return self.elem


# Generate items
types = ["weapon", "potion", "scroll", "elixir", "staff", "quest", "armor"]
elements = ["Fire", "Death", "Magic", "Alter", "Heal"]
materials = ["Robe", "Leather", "Metal", "Metal Plate"]

# Weapons type = type[0]
staff = Item("Quarterstaff", 6, 10, types[4])
short_sword = Item("Short Sword", 6, 10, types[0])
long_sword = Item("Long Sword", 8, 100, types[0])
bastard_sword = Item("Bastard Sword", 10, 200, types[0])
great_sword = Item("Greatsword", 12, 500, types[0])
great_axe = Item("Greataxe", 16, 1000, types[0])
short_sword_fire = Item("Short Sword of Fire", 6, 10, types[0], element="Fire")
long_sword_fire = Item("Long Sword of Fire", 8, 100, types[0], element="Fire")
bastard_sword_fire = Item("Bastard Sword of Fire", 10, 200, types[0], element="Fire")
great_sword_fire = Item("Greatsword of Fire", 12, 500, types[0], element="Fire")
great_axe_fire = Item("Greataxe of Fire", 16, 1000, types[0], element="Fire")
short_sword_magic = Item("Short Sword of Magic", 6, 10, types[0], element="Magic")
long_sword_magic = Item("Long Sword of Magic", 8, 100, types[0], element="Magic")
bastard_sword_magic = Item("Bastard Sword of Magic", 10, 200, types[0], element="Magic")
great_sword_magic = Item("Greatsword of Magic", 12, 500, types[0], element="Magic")
great_axe_magic = Item("Greataxe of Magic", 16, 1000, types[0], element="Magic")
short_sword_death = Item("Short Sword of Death", 6, 10, types[0], element="Death")
long_sword_death = Item("Long Sword of Death", 8, 100, types[0], element="Death")
bastard_sword_death = Item("Bastard Sword of Death", 10, 200, types[0], element="Death")
great_sword_death = Item("Greatsword of Death", 12, 500, types[0], element="Death")
great_axe_death = Item("Greataxe of Death", 16, 1000, types[0], element="Death")

weapons = [staff, short_sword, long_sword, bastard_sword, great_sword, great_axe]
fire_weapons = [staff, short_sword_fire, long_sword_fire, bastard_sword_fire, great_sword_fire, great_axe_fire]
magic_weapons = [staff, short_sword_magic, long_sword_magic, bastard_sword_magic, great_sword_magic, great_axe_magic]
death_weapons = [staff, short_sword_death, long_sword_death, bastard_sword_death, great_sword_death, great_axe_death]

# Potions type = type[1]

pot_light1 = Item("Potion of Light Wounds", 50, 50, types[1])
pot_light2 = Item("Potion of Light Wounds", 50, 50, types[1])
pot_light3 = Item("Potion of Light Wounds", 50, 50, types[1])
pot_light4 = Item("Potion of Light Wounds", 50, 50, types[1])
pot_light5 = Item("Potion of Light Wounds", 50, 50, types[1])
pot_med1 = Item("Potion of Moderate Wounds", 100, 100, types[1])
pot_med2 = Item("Potion of Moderate Wounds", 100, 100, types[1])
pot_med3 = Item("Potion of Moderate Wounds", 100, 100, types[1])
pot_med4 = Item("Potion of Moderate Wounds", 100, 100, types[1])
pot_med5 = Item("Potion of Moderate Wounds", 100, 100, types[1])
pot_heav1 = Item("Potion of Heavy Wounds", 200, 200, types[1])
pot_heav2 = Item("Potion of Heavy Wounds", 200, 200, types[1])
pot_heav3 = Item("Potion of Heavy Wounds", 200, 200, types[1])
pot_heav4 = Item("Potion of Heavy Wounds", 200, 200, types[1])
pot_heav5 = Item("Potion of Heavy Wounds", 200, 200, types[1])

potions = [pot_light1, pot_light2, pot_light3, pot_light4, pot_light5, pot_med1, pot_med2, pot_med3, pot_med4, pot_med5,
           pot_heav1, pot_heav2, pot_heav3, pot_heav4, pot_heav5]

# Scroll type = type[2]
scr_magic_missile = Item("Scroll of Magic Missile", 10, 100, types[2], element="Magic")
scr_firebolt = Item("Scroll of Firebolt", 25, 100, types[2], element="Fire")
scr_heal = Item("Scroll of Mend Light Wounds", 50, 100, types[2], element="Heal")
scr_heal2 = Item("Scroll of Mend Wounds", 100, 200, types[2], element="Heal")
scr_heal3 = Item("Scroll of Mend Heavy Wounds", 200, 500, types[2], element="Heal")
scr_deathray = Item("Scroll of Death", 15, 100, types[2], element="Death")
scr_sleep = Item("Scroll of Sleep", 10, 20, types[2], element="Alter")
scr_paralyze = Item("Scroll of Sleep Paralysis", 20, 50, types[2], element="Alter")

scrolls = [scr_magic_missile, scr_firebolt, scr_heal, scr_heal2, scr_heal3, scr_deathray, scr_sleep, scr_paralyze]

# Elixir type = type[3]
elix_light1 = Item("Weak Elixir", 25, 50, types[3])
elix_med1 = Item("Elixir", 25, 50, types[3])
elix_heav1 = Item("Strong Elixir", 25, 50, types[3])
elix_light2 = Item("Weak Elixir", 25, 50, types[3])
elix_med2 = Item("Elixir", 25, 50, types[3])
elix_heav2 = Item("Strong Elixir", 25, 50, types[3])
elix_light3 = Item("Weak Elixir", 25, 50, types[3])
elix_med3 = Item("Elixir", 25, 50, types[3])
elix_heav3 = Item("Strong Elixir", 25, 50, types[3])
elix_light4 = Item("Weak Elixir", 25, 50, types[3])
elix_med4 = Item("Elixir", 25, 50, types[3])
elix_heav4 = Item("Strong Elixir", 25, 50, types[3])
elix_light5 = Item("Weak Elixir", 25, 50, types[3])
elix_med5 = Item("Elixir", 25, 50, types[3])
elix_heav5 = Item("Strong Elixir", 25, 50, types[3])

elixirs = [elix_light1, elix_light2, elix_light3, elix_light4, elix_light5, elix_med1, elix_med2, elix_med3, elix_med4,
           elix_med5, elix_heav1, elix_heav2, elix_heav3, elix_heav4, elix_heav5]

# Staff type = type[4]
magic_staff = Item("Staff of Magic", 8, 1000, types[4], element="Magic")
fire_staff = Item("Staff of Fire", 8, 2000, types[4], element="Fire")
death_staff = Item("Staff of Death", 8, 5000, types[4], element="Death")
sleep_staff = Item("Staff of Sleep", 8, 3500, types[4], element="Alter")

staffs = [magic_staff, fire_staff, death_staff, sleep_staff]

# Quest Items = type[5]
test_quest_item = Item("Quest Item", 0, 0, types[5])

# Armor Items = type[6]
robe = Item("Robe", 0, 50, types[6], element="None", material="Robe")
robe_white = Item("White Robe", 10, 50, types[6], element="White", material="Robe")
robe_red = Item("Red Robe", 5, 50, types[6], element="Red", material="Robe")
robe_gold = Item("Gold Robe", 5, 50, types[6], element="Gold", material="Robe")
robe_blue = Item("Blue Robe", 5, 50, types[6], element="Blue", material="Robe")
leather = Item("Leather Armor", 1, 100, types[6], element="None", material="Leather")
studded = Item("Studded Leather Armor", 2, 150, types[6], element="None", material="Leather")
leather_white = Item("White Leather Armor", 11, 100, types[6], element="White", material="Leather")
studded_white = Item("White Studded Leather Armor", 12, 150, types[6], element="White", material="Leather")
leather_red = Item("Red Leather Armor", 6, 100, types[6], element="Red", material="Leather")
studded_red = Item("Red Studded Leather Armor", 7, 150, types[6], element="Red", material="Leather")
chainshirt = Item("Chain Shirt", 3, 250, types[6], element="None", material="Metal")
scale = Item("Scalemail", 4, 350, types[6], element="None", material="Metal")
chainshirt_white = Item("White Chain Shirt", 13, 250, types[6], element="White", material="Metal")
scale_white = Item("White Scalemail", 14, 350, types[6], element="White", material="Metal")
half = Item("Half Plate Armor", 5, 550, types[6], element="None", material="Metal Plate")
half_white = Item("White Half Plate Armor", 15, 550, types[6], element="White", material="Metal Plate")
half_gold = Item("Gold Half Plate Armor", 10, 550, types[6], element="Gold", material="Metal Plate")
ring = Item("Ringmail", 6, 650, types[6], element="None", material="Metal")
chain = Item("Chainmail", 7, 850, types[6], element="None", material="Metal")
ring_white = Item("White Ringmail", 16, 650, types[6], element="White", material="Metal")
chain_white = Item("White Chainmail", 17, 850, types[6], element="White", material="Metal")
full = Item("Platemail", 8, 1150, types[6], element="None", material="Metal Plate")
full_white = Item("White Platemail", 18, 1150, types[6], element="White", material="Metal Plate")
full_gold = Item("Gold Platemail", 13, 1150, types[6], element="Gold", material="Metal Plate")

armors = [robe, leather, studded, chainshirt, scale, half, ring, chain, full]
white_armors = [robe_white, leather_white, studded_white, chainshirt_white, scale_white, half_white, ring_white,
                chain_white, full_white]
red_armors = [robe_red, leather_red, studded_red]
gold_armors = [robe_gold, half_gold, full_gold]
blue_armors = [robe_blue]

# Starting Items by Character CLASS

spellsword_inv = {"weapon": weapons[1], "items": [potions[0], scrolls[0]], "armor": armors[1]}
warden_inv = {"weapon": weapons[2], "items": [potions[0]], "armor": armors[1]}
sorceror_inv = {"weapon": weapons[0], "items": [potions[0], elixirs[0], scrolls[0]], "armor": armors[0]}


inn_items = []

# IDs
id_list = []
for a in string.ascii_letters:
    id_list.append(a)

number = len(id_list)
id_numbers = []
for n in range(0, 10):
    id_numbers.append(n)
ids = []


def generate_ids():
    for a in id_list:
        for n in id_numbers:
            ids.append(a + str(n))


generate_ids()

id_val = 0

# list of item classes
p_lst = []
e_lst = []
# shop function that displays item types
item_labels = ["Weak Potion", "Potion", "Strong Potion", "Weak Elixir", "Elixir", "Strong Elixir"]


def display_shop_menu():
    c = 1
    for item in item_labels:
        print("{}. {}".format(c, item))
        c += 1


def player_choice():
    choice = input("What would ya like? ")
    id_count = 0
    while choice == "":
        choice = input("'Well?'")
    while not choice.isdigit():
        choice = input("'Well?' ")
    choice = int(choice)
    if choice == 1:
        i = Item("Potion of Light Wounds", 50, 50, types[1], _id=ids[id_count])
        id_count += 1
        return i
    elif choice == 2:
        i = Item("Potion of Moderate Wounds", 100, 100, types[1], _id=ids[id_count])
        id_count += 1
        return i
    elif choice == 3:
        i = Item("Potion of Heavy Wounds", 200, 200, types[1], _id=ids[id_count])
        id_count += 1
        return i
    elif choice == 4:
        i = Item("Weak Elixir", 50, 50, types[3], _id=ids[id_count])
        id_count += 1
        return i
    elif choice == 5:
        i = Item("Elixir", 100, 100, types[3], _id=ids[id_count])
        id_count += 1
        return i
    elif choice == 6:
        i = Item("Strong Elixir", 200, 200, types[3], _id=ids[id_count])
        id_count += 1
        return i


def generate_scroll(spell):
    index = spells.index(spell)
    if index == 0:
        s = Item("Scroll of Magic Missile", 10, 100, types[2], element="Magic", _id=randint(1,1000))
        return s
    elif index == 1:
        s = Item("Scroll of Firebolt", 25, 100, types[2], element="Fire", _id=randint(1,1000))
        return s
    elif index == 2:
        s = Item("Scroll of Scroll of Heal", 50, 100, types[2], element="Heal", _id=randint(1,1000))
        return s
    elif index == 3:
        s = Item("Scroll of Cure Moderate Wounds", 100, 200, types[2], element="Heal", _id=randint(1,1000))
        return s
    elif index == 4:
        s = Item("Scroll of Cure Heavy Wounds", 200, 500, types[2], element="Heal", _id=randint(1,1000))
        return s
    elif index == 5:
        s = Item("Scroll of Death", 15, 100, types[2], element="Death", _id=randint(1,1000))
        return s
    elif index == 6:
        s = Item("Scroll of Sleep", 10, 20, types[2], element="Alter", _id=randint(1,1000))
        return s
    elif index == 7:
        s = Item("Scroll of Sleep Paralysis", 20, 50, types[2], element="Alter", _id=randint(1,1000))
        return s


def enchantment_check(char):
    weapon = char.items["weapon"]
    try:
        weapons.index(weapon)
        return True
    except ValueError:
        return False


def enchantment_check_armor(char):
    armor = char.items["armor"]
    try:
        armors.index(armor)
        return True
    except ValueError:
        return False


def enchant_weapon(char):
    weapon = char.items["weapon"]
    _bool = enchantment_check(char)
    if _bool:
        lst = ["White", "Red", "Black"]
        c = 1
        for l in lst:
            print("{}. {}".format(c, l))
            c += 1
        print("{}. Never you mind.".format(c))
        choice = input("Please select an enchantment: ")
        while choice == "":
            choice = input("'Well?'")
        while not choice.isdigit():
            choice = input("'Well?' ")
        choice = int(choice)
        if choice == 1:
            index = weapons.index(weapon)
            weapon = magic_weapons[index]
            char.items["weapon"] = weapon
            print("{}".format(char.items["weapon"].name))
        elif choice == 2:
            index = weapons.index(weapon)
            weapon = fire_weapons[index]
            char.items["weapon"] = weapon
            print("{}".format(char.items["weapon"].name))
        elif choice == 3:
            index = weapons.index(weapon)
            weapon = death_weapons[index]
            char.items["weapon"] = weapon
            print("{}".format(char.items["weapon"].name))
        elif choice == 4:
            return
        else:
            return


def enchant_armor(char):
    armor = char.items["armor"]
    _bool = enchantment_check_armor(char)
    if _bool:
        if armor.mat == "Robe":
            lst = ["White", "Red", "Gold", "Blue"]
            c = 1
            for l in lst:
                print("{}. {}".format(c, l))
                c += 1
            print("{}. Never you mind.".format(c))
            choice = input("Please select an enchantment: ")
            while choice == "":
                choice = input("'Well?'")
            while not choice.isdigit():
                choice = input("'Well?' ")
            choice = int(choice)
            if choice == 1:
                index = armors.index(armor)
                armor = white_armors[index]
                char.items["armor"] = armor
                print("{}".format(char.items["armor"].name))
            elif choice == 2:
                #index = armors.index(armor)
                armor = red_armors[0]
                char.items["armor"] = armor
                print("{}".format(char.items["armor"].name))
            elif choice == 3:
                #index = armor.index(armor)
                armor = gold_armors[0]
                char.items["armor"] = armor
                print("{}".format(char.items["armor"].name))
            elif choice == 4:
                #index = armor.index(armor)
                armor = blue_armors[0]
                char.items["armor"] = armor
                print("{}".format(char.items["armor"].name))
            elif choice == 5:
                return
            else:
                return
        elif armor.mat == "Leather":
            lst = ["White", "Red"]
            c = 1
            for l in lst:
                print("{}. {}".format(c, l))
                c += 1
            print("{}. Never you mind.".format(c))
            choice = input("Please select an enchantment: ")
            while choice == "":
                choice = input("'Well?'")
            while not choice.isdigit():
                choice = input("'Well?' ")
            choice = int(choice)
            if choice == 1:
                index = armors.index(armor)
                armor = white_armors[index]
                char.items["armor"] = armor
                print("{}".format(char.items["armor"].name))
            elif choice == 2:
                index = armors.index(armor)

                armor = red_armors[index]
                char.items["armor"] = armor
                print("{}".format(char.items["armor"].name))
            elif choice == 3:
                return
            else:
                return
        elif armor.mat == "Metal":
            lst = ["White"]
            c = 1
            for l in lst:
                print("{}. {}".format(c, l))
                c += 1
            print("{}. Never you mind.".format(c))
            choice = input("Please select an enchantment: ")
            while choice == "":
                choice = input("'Well?'")
            while not choice.isdigit():
                choice = input("'Well?' ")
            choice = int(choice)
            if choice == 1:
                index = armors.index(armor)
                armor = white_armors[index]
                char.items["armor"] = armor
                print("{}".format(char.items["armor"].name))
            elif choice == 2:
                return
            else:
                return
        elif armor.mat == "Metal Plate":
            lst = ["White", "Gold"]
            c = 1
            for l in lst:
                print("{}. {}".format(c, l))
                c += 1
            print("{}. Never you mind.".format(c))
            choice = input("Please select an enchantment: ")
            while choice == "":
                choice = input("'Well?'")
            while not choice.isdigit():
                choice = input("'Well?' ")
            choice = int(choice)
            if choice == 1:
                index = armors.index(armor)
                armor = white_armors[index]
                char.items["armor"] = armor
                print("{}".format(char.items["armor"].name))
            elif choice == 2:
                index = armors.index(armor)
                if index == 5:
                    armor = gold_armors[1]
                elif index == 8:
                    armor = gold_armors[2]
                char.items["armor"] = armor
                print("{}".format(char.items["armor"].name))
            elif choice == 3:
                return
            else:
                return


def enchant_staff(char):
    staff = char.items["weapon"]
    _bool = enchantment_check(char)
    if _bool:
        lst = ["White", "Red", "Black", "Green"]
        c = 1
        for l in lst:
            print("{}. {}".format(c, l))
            c += 1
        print("{}. Never you mind.".format(c))
        choice = input("Please select an enchantment: ")
        while choice == "":
            choice = input("'Well?'")
        while not choice.isdigit():
            choice = input("'Well?' ")
        choice = int(choice)
        if choice == 1:
            weapon = staffs[0]
            char.items["weapon"] = weapon
            print("{}".format(char.items["weapon"].name))
        elif choice == 2:
            weapon = staffs[1]
            char.items["weapon"] = weapon
            print("{}".format(char.items["weapon"].name))
        elif choice == 3:
            weapon = staffs[2]
            char.items["weapon"] = weapon
            print("{}".format(char.items["weapon"].name))
        elif choice == 4:
            weapon = staffs[3]
            char.items["weapon"] = weapon
            print("{}".format(char.items["weapon"].name))
        elif choice == 4:
            return
        else:
            return