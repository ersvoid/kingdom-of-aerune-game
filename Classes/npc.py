

class NPC:
    def __init__(self, name, items, money, phrase):
        self.name = name
        self.items = items
        self.money = money
        self.phrase = phrase

    def talk(self):
        print(self.phrase)

    def sell(self, char):
        c = 1
        for i in self.items:
            print(str(c) + ". " + i.name + ": " + str(i.cost))
            c += 1
        print("or 0 to quit")
        choice = input("Choose an item to buy: ")
        while choice == "":
            choice = input("Choose: ")
        while not choice.isdigit():
            choice = input("Choose a number: ")
        choice = int(choice) - 1
        if choice == -1:
            return
        item = self.items[choice]
        if char.money >= item.cost:
            if item.type == "weapon":
                print("You can only have one weapon at a time.")
                print("Do you want to trade weapons?")
                print("1. Yes")
                print("2. No")
                val = str(input("Well? "))
                if val == "1":
                    char.money += char.items["weapon"].cost
                    char.money -= item.cost
                    self.money += item.cost
                    char.items["weapon"] = item
                    print("You have bought the {}!".format(item.name))
                    return self.money, self.items, char.items, char.money
                elif val == "2":
                    print("Okay, that's fine.")
                else:
                    return
            else:
                temp_var = char.items["items"]
                temp_var.append(item)
                char.items["items"] = temp_var
                char.money -= item.cost
                self.money += item.cost
                print("You have bought a {}!".format(item.name))
                return self.money, self.items, char.items, char.money
        else:
            print("You don't have enough gold!")
            int(input("Choose an item to buy: ")) - 1

    def buy(self, char):
        c = 1
        for i in char.items["items"]:
            print(str(c) + ". " + i.name + ": " + str(i.cost))
            c += 1
        print("or 0 to quit")
        choice = input("Choose an item to sell: ")
        while choice == "":
            choice = input("Choose: ")
        while not choice.isdigit():
            choice = input("Choose a number: ")
        choice = int(choice) - 1
        if choice == -1:
            return
        item = char.items["items"][choice]
        char.money += item.cost
        self.money -= item.cost
        del char.items["items"][choice]
        return self.money, self.items, char.items, char.money

    def sell_drink(self, char, drink):
        temp_var = char.items["items"]
        temp_var.append(drink)
        char.items["items"] = temp_var
        char.money -= drink.cost
        self.money += drink.cost
        print("You have bought a {}!".format(drink.name))
        return self.money, self.items, char.items, char.money
