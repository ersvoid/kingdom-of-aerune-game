

class Item:
    def __init__(self, name, val, cost, _type, amount=1, element="None"):
        self.name = name
        self.val = val
        self.cost = cost
        self.type = _type
        self.amt = amount
        self.elem = element

    def item_value(self):
        return self.val

    def get_type(self):
        return self.type

    def __del__(self):
        pass

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
types = ["weapon", "potion", "scroll", "elixir", "staff", "quest"]
elements = ["Fire", "Death", "Magic", "Alter", "Heal"]

# Weapons type = type[0]
short_sword = Item("Short Sword", 4, 10, types[0])
long_sword = Item("Long Sword", 8, 100, types[0])
bastard_sword = Item("Bastard Sword", 200, 50, types[0])
great_sword = Item("Greatsword", 32, 500, types[0])
great_axe = Item("Greataxe", 50, 1000, types[0])
short_sword_fire = Item("Short Sword of Fire", 4, 10, types[0], element="Fire")
long_sword_fire = Item("Long Sword of Fire", 8, 100, types[0], element="Fire")
bastard_sword_fire = Item("Bastard Sword of Fire", 200, 50, types[0], element="Fire")
great_sword_fire = Item("Greatsword of Fire", 32, 500, types[0], element="Fire")
great_axe_fire = Item("Greataxe of Fire", 50, 1000, types[0], element="Fire")
short_sword_magic = Item("Short Sword of Magic", 4, 10, types[0], element="Magic")
long_sword_magic = Item("Long Sword of Magic", 8, 100, types[0], element="Magic")
bastard_sword_magic = Item("Bastard Sword of Magic", 200, 50, types[0], element="Magic")
great_sword_magic = Item("Greatsword of Magic", 32, 500, types[0], element="Magic")
great_axe_magic = Item("Greataxe of Magic", 50, 1000, types[0], element="Magic")
short_sword_death = Item("Short Sword of Death", 4, 10, types[0], element="Death")
long_sword_death = Item("Long Sword of Death", 8, 100, types[0], element="Death")
bastard_sword_death = Item("Bastard Sword of Death", 200, 50, types[0], element="Death")
great_sword_death = Item("Greatsword of Death", 32, 500, types[0], element="Death")
great_axe_death = Item("Greataxe of Death", 50, 1000, types[0], element="Death")

weapons = [short_sword, long_sword, bastard_sword, great_sword, great_axe]
fire_weapons = [short_sword_fire, long_sword_fire, bastard_sword_fire, great_sword_fire, great_axe_fire]
magic_weapons = [short_sword_magic, long_sword_magic, bastard_sword_magic, great_sword_magic, great_axe_magic]
death_weapons = [short_sword_death, long_sword_death, bastard_sword_death, great_sword_death, great_axe_death]

# Potions type = type[1]
pot_light = Item("Potion of Light Wounds", 50, 50, types[1])
pot_med = Item("Potion of Moderate Wounds", 100, 100, types[1])
pot_heav = Item("Potion of Heavy Wounds", 200, 200, types[1])

potions = [pot_light, pot_med, pot_heav]

# Scroll type = type[2]
scr_magic_missile = Item("Scroll of Magic Missile", 10, 100, types[2], element="Magic")
scr_firebolt = Item("Scroll of Firebolt", 25, 100, types[2], element="Fire")
scr_heal = Item("Scroll of Scroll of Heal", 50, 100, types[2], element="Heal")
scr_heal2 = Item("Scroll of Cure Moderate Wounds", 100, 200, types[2], element="Heal")
scr_heal3 = Item("Scroll of Cure Heavy Wounds", 200, 500, types[2], element="Heal")
scr_deathray = Item("Scroll of Death", 15, 100, types[2], element="Death")
scr_sleep = Item("Scroll of Sleep", 10, 20, types[2], element="Alter")
scr_paralyze = Item("Scroll of Sleep Paralysis", 20, 50, types[2], element="Alter")

scrolls = [scr_magic_missile, scr_firebolt, scr_heal, scr_heal2, scr_heal3, scr_deathray, scr_sleep, scr_paralyze]

# Elixir type = type[3]
elix_light = Item("Weak Elixir", 25, 50, types[3])
elix_med = Item("Elixir", 25, 50, types[3])
elix_heav = Item("Strong Elixir", 25, 50, types[3])

elixirs = [elix_light, elix_med, elix_heav]

# Staff type = type[4]
magic_staff = Item("Staff of Magic", 8, 500, types[4], element="Magic")
fire_staff = Item("Staff of Fire", 8, 500, types[4], element="Fire")
death_staff = Item("Staff of Death", 8, 500, types[4], element="Death")
sleep_staff = Item("Staff of Sleep", 8, 500, types[4], element="Alter")

staffs = [magic_staff, fire_staff, death_staff, sleep_staff]

# Quest Items = type[5]
test_quest_item = Item("Quest Item", 0, 0, types[5])


inn_items = [pot_light, pot_med, pot_heav, elix_light, elix_med, elix_heav]