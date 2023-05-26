# Taken from mission The Defenders

# Taken from mission Army Battles
# Taken from mission The Warriors


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True
        self.defense = 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, number):
        self.units += [unit_type() for _ in range(number)]


class Battle:
    def fight(self, first_army, second_army):
        first_army_itr = iter(first_army.units)
        second_army_itr = iter(second_army.units)
        first_army_unit = next(first_army_itr)
        second_army_unit = next(second_army_itr)
        while True:
            if fight(first_army_unit, second_army_unit):
                try:
                    second_army_unit = next(second_army_itr)
                except StopIteration:
                    return True
            else:
                try:
                    first_army_unit = next(first_army_itr)
                except StopIteration:
                    return False


def fight(unit_1, unit_2):
    while True:
        if unit_2.defense < unit_1.attack:
            unit_2.health -= unit_1.attack - unit_2.defense
            if getattr(unit_1, "vampirism", False):
                unit_1.health += (unit_1.attack - unit_2.defense) * unit_1.vampirism
        if unit_1.health > 0 >= unit_2.health:
            unit_2.is_alive = False
            return True

        if unit_1.defense < unit_2.attack:
            unit_1.health -= unit_2.attack - unit_1.defense
            if getattr(unit_2, "vampirism", False):
                unit_2.health += (unit_2.attack - unit_1.defense) * unit_2.vampirism
        if unit_2.health > 0 >= unit_1.health:
            unit_1.is_alive = False
            return False


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False, "0"
    assert battle.fight(army_3, army_4) == True, "1"
    print("Coding complete? Let's try tests!")

    ## BATTLE 2
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Defender, 5)
    army_1.add_units(Vampire, 6)
    army_1.add_units(Warrior, 7)
    army_2.add_units(Warrior, 6)
    army_2.add_units(Defender, 6)
    army_2.add_units(Vampire, 6)
    battle = Battle()
    assert battle.fight(army_1, army_2) is False, "2"

    ## BATTLE 3
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Defender, 11)
    army_1.add_units(Vampire, 3)
    army_1.add_units(Warrior, 4)
    army_2.add_units(Warrior, 4)
    army_2.add_units(Defender, 4)
    army_2.add_units(Vampire, 13)
    battle = Battle()
    assert battle.fight(army_1, army_2) is True, "3"


"""
So we have 3 types of units: the Warrior, Knight and Defender. Let's make the battles even more epic and add another type - the Vampire!
Vampire should be the subclass of the Warrior class and have the additional vampirism parameter, which helps him to heal himself. When the Vampire hits the other unit, he restores his health by +50% of the dealt damage (enemy defense makes the dealt damage value lower).
The basic parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%
Input: The warriors and armies.

Output: The result of the battle (True or False).

Precondition: 4 types of units
"""
