from random import randint, choice
import string
from Classes.magic import spells


class Item:
    def __init__(self, name, val, cost, _type, amount=1, element="None", _id="None"):
        self.name = name
        self.val = val
        self.cost = cost
        self.type = _type
        self.amt = amount
        self.elem = element
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
elements = ["Fire", "Death", "Magic", "Alter", "Heal", "Defense"]

# Weapons type = type[0]
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

weapons = [short_sword, long_sword, bastard_sword, great_sword, great_axe]
fire_weapons = [short_sword_fire, long_sword_fire, bastard_sword_fire, great_sword_fire, great_axe_fire]
magic_weapons = [short_sword_magic, long_sword_magic, bastard_sword_magic, great_sword_magic, great_axe_magic]
death_weapons = [short_sword_death, long_sword_death, bastard_sword_death, great_sword_death, great_axe_death]

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
scr_bark = Item("Scroll of Barkskin", 2, 50, types[2], element="defense")
scr_mage = Item("Scroll of Mage Armor", 4, 50, types[2], element="defense")
scr_iron = Item("Scroll of Ironskin", 6, 50, types[2], element="defense")
scr_shield = Item("Scroll of Shield", 8, 50, types[2], element="defense")

scrolls = [scr_magic_missile, scr_firebolt, scr_heal, scr_heal2, scr_heal3, scr_deathray, scr_sleep, scr_paralyze,
           scr_bark, scr_mage, scr_iron, scr_shield]

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
padded = Item("Padded Armor", 0, 50, types[6])
leather = Item("Leather Armor", 1, 100, types[6])
studded = Item("Studded Leather Armor", 2, 150, types[6])
chainshirt = Item("Chain Shirt", 3, 250, types[6])
scale = Item("Scalemail", 4, 350, types[6])
half = Item("Half Plate Armor", 5, 550, types[6])
ring = Item("Ringmail", 6, 650, types[6])
chain = Item("Chainmail", 7, 850, types[6])
full = Item("Platemail", 8, 1150, types[6])

armors = [padded, leather, studded, chainshirt, scale, half, ring, chain, full]

# Starting Items by Character CLASS

spellsword_inv = {"weapon": weapons[1], "items": [potions[0], scrolls[0]], "armor": armors[0]}
warden_inv = {"weapon": weapons[1], "items": [potions[0]], "armor": armors[1]}
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
        s = Item("Scroll of Scroll of Barkskin", 2, 100, types[2], element="Heal", _id=randint(1,1000))
        return s
    elif index == 3:
        s = Item("Scroll of Mage Armor", 4, 200, types[2], element="Heal", _id=randint(1,1000))
        return s
    elif index == 4:
        s = Item("Scroll of Ironskin", 6, 500, types[2], element="Heal", _id=randint(1,1000))
        return s
    elif index == 5:
        s = Item("Scroll of Shield", 8, 100, types[2], element="Death", _id=randint(1,1000))
        return s
    elif index == 6:
        s = Item("Scroll of Scroll of Heal", 50, 100, types[2], element="Heal", _id=randint(1,1000))
        return s
    elif index == 7:
        s = Item("Scroll of Cure Moderate Wounds", 100, 200, types[2], element="Heal", _id=randint(1,1000))
        return s
    elif index == 8:
        s = Item("Scroll of Cure Heavy Wounds", 200, 500, types[2], element="Heal", _id=randint(1,1000))
        return s
    elif index == 9:
        s = Item("Scroll of Death", 15, 100, types[2], element="Death", _id=randint(1,1000))
        return s
    elif index == 10:
        s = Item("Scroll of Sleep", 10, 20, types[2], element="Alter", _id=randint(1,1000))
        return s
    elif index == 11:
        s = Item("Scroll of Sleep Paralysis", 20, 50, types[2], element="Alter", _id=randint(1,1000))
        return s


def enchantment_check(char):
    weapon = char.items["weapon"]
    try:
        weapons.index(weapon)
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
