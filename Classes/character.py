from random import randint


def build_hp(char):
    return 10 + 10 * char.get_con()


def build_mp(char):
    return 10 + 10 * char.get_wis()


class Character:
    def __init__(self, name, _str, _int, dex, wis, cha, con, magic, items, money=0, lvl=1):
        self.name = name
        self.str = _str
        self.int = _int
        self.dex = dex
        self.wis = wis
        self.cha = cha
        self.con = con
        self.magic = magic
        self.items = items
        self.maxhp = build_hp(self)
        self.hp = self.maxhp
        self.maxmp = build_mp(self)
        self.mp = self.maxmp
        self.sleep = False
        self.fire = 0
        self.money = money
        self.quest = 0
        self.xp = 0
        self.lvl = 1

    def display_name(self):
        print("I am called ", self.name, "!")

    def get_str(self):
        return self.str - 10

    def get_int(self):
        return self.int - 10

    def get_dex(self):
        return self.dex - 10

    def get_wis(self):
        return self.wis - 10

    def get_cha(self):
        return self.cha - 10

    def get_con(self):
        return self.con - 10

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def attack(self):
        print("{} attacks!".format(self.name))
        return randint(1, 21) + self.get_str()

    def ac_rating(self):
        return randint(1, 21) + self.get_dex()

    def reflex(self):
        return randint(1, 21) + self.get_dex()

    def fortitude(self):
        return randint(1, 21) + self.get_con()

    def will(self):
        return randint(1, 21) + self.get_wis()

    def take_damage(self, val):
        self.hp -= val
        print("{} has taken {} points of damage.".format(self.name, val))
        return self.hp

    def take_mp(self, cost):
        self.mp -= cost
        return self.mp

    def heal(self, val):
        self.hp += val
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        print("{} has healed for {} HP.".format(self.name, val))
        return self.hp

    def rest(self, val):
        self.mp += val
        if self.mp > self.maxmp:
            self.mp = self.maxmp
        return self.mp

    def display_stats(self):
        print("Name: ", self.name, "\n", "HP: ", self.hp, "/", self.maxhp, "\n", "MP: ", self.mp, "/", self.maxmp, "\n"
              "Strength: ", self.str, "\n"
              "Intelligence: ", self.int, "\n"
              "Dexterity: ", self.dex, "\n"
              "Wisdom: ", self.wis, "\n"
              "Charisma: ", self.cha, "\n"
              "Constitution: ", self.con)

    def __del__(self):
        pass

    def death_check(self):
        if self.hp <= 0:
            return True
        else:
            pass

    def damage(self):
        val = randint(1, self.items["weapon"].item_value()) + self.get_str()
        if val < 0:
            return 0
        else:
            return val

    def reset(self):
        self.hp = self.maxhp
        self.mp = self.maxmp
        return self.hp, self.mp

    def win_gold(self, val):
        self.money += val
        print("You have won {}gp.".format(val))
        return self.money

    def spend_gold(self, val):
        self.money -= val
        print("You have lost {}gp.".format(val))
        return self.money

    def get_xp(self, val):
        self.xp += val
        return self.xp
