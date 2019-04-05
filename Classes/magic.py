

class Spell:
    def __init__(self, name, _type, val, cost, element=None):
        self.name = name
        self.type = _type
        self.val = val
        self.cost = cost
        self.elem = element

    def get_val(self):
        return self.val

    def get_cost(self):
        return self.cost

    def special(self):
        if self.elem is None:
            pass
        else:
            return self.elem


# Generate Spells

magic_missile = Spell("Magic Missile", "attack", 10, 10)
firebolt = Spell("Firebolt", "attack", 25, 50, element="Fire")
deathray = Spell("Death Ray", "attack", 15, 100, element="Death")

bark = Spell("Barkskin", "defense", 2, 10)
mage = Spell("Mage Armor", "defense", 4, 15)
iron = Spell("Ironskin", "defense", 6, 30)
shield = Spell("Shield", "defense", 8, 45)

heal = Spell("Cure Light Wounds", "heal", 10, 10)
heal2 = Spell("Cure Moderate Wounds", "heal", 25, 20)
heal3 = Spell("Cure Heavy Wounds", "heal", 50, 40)

sleep = Spell("Sleep", "alter", 5, 20)
paralyze = Spell("Sleep Paralysis", "alter", 10, 50)

spells = [magic_missile, firebolt, bark, mage, iron, shield, heal, heal2, heal3, deathray, sleep, paralyze]

sword_magic = [magic_missile, firebolt, mage, shield, heal, sleep]
ward_magic = [bark, iron, shield, heal, heal2, heal3]
sorce_magic = [magic_missile, firebolt, mage, heal, sleep, paralyze]