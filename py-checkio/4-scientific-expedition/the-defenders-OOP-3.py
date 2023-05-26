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
        if unit_1.health > 0 >= unit_2.health:
            unit_2.is_alive = False
            return True
        if unit_1.defense < unit_2.attack:
            unit_1.health -= unit_2.attack - unit_1.defense
        if unit_2.health > 0 >= unit_1.health:
            unit_1.is_alive = False
            return False


if __name__ == "__main__":
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

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False
    assert fight(bob, mike) is False
    assert fight(lancelot, rog) is True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is False
    assert battle.fight(army_3, army_4) is True
    print("Coding complete? Let's try tests!")
