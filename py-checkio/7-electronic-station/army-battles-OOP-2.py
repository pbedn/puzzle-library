# In the previous mission - Warriors - you've learned how to make a duel between 2 warriors happen. Great job! But let's move to something that feels a little more epic - the armies! In this mission your task is to add new classes and functions to the existing ones. The new class should be the Army and have the method add_units() - for adding the chosen amount of units to the army. Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
# The battles occur according to the following principles:
# at first, there is a duel between the first warrior of the first army and the first warrior of the second army. As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel, and the surviving warrior continues to fight with his current health. This continues until all the soldiers of one of the armies die. In this case, the battle() function should return True, if the first army won, or False, if the second one was stronger.
# Note that army 1 have the advantage to start every fight!
#
# Input: The warriors and armies.
#
# Output: The result of the battle (True or False).
#
# Precondition: 2 types of units

# Taken from mission The Warriors


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Army:
    def __init__(self):
        self.units = dict()

    def add_units(self, unit_type, number):
        self.units = [unit_type() for _ in range(number)]


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
        unit_2.health -= unit_1.attack
        if unit_1.health > 0 >= unit_2.health:
            unit_2.is_alive = False
            return True
        unit_1.health -= unit_2.attack
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

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is True
    assert battle.fight(army_3, army_4) is False
    print("Coding complete? Let's try tests!")
