def checkio(number):
    food_left = number
    number_of_pigeons, i = 0, 0
    while food_left > 0:
        i += 1
        number_of_pigeons += i

        for i in range(number_of_pigeons):
            food_eaten = 

    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"


'''
I start to feed one of the pigeons. A minute later two more fly by and a minute after that another 3. Then 4, and so on (Ex: 1+2+3+4+...). One portion of food lasts a pigeon for a minute, but in case there's not enough food for all the birds, the pigeons who arrived first ate first. Pigeons are hungry animals and eat without knowing when to stop. If I have N portions of bird feed, how many pigeons will be fed with at least one portion of wheat?

Input: A quantity of portions wheat as a positive integer.

Output: The number of fed pigeons as an integer.

Precondition: 0 < N < 105.
'''