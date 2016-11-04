# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise


class Pirate():

    number_of_rums = 0

    def __init__(self):
        print("Hi, Im' a pirate, I drink rum!")

    def drink_rum(self):
        self.number_of_rums += 1
        print("I drinked", self.number_of_rums, "rum.")
        self.hows_goin_mate()

    def hows_goin_mate(self):
        if self.number_of_rums >= 5:
            return "Arrrr!"
        else:
            return "Nothin!"


John_Silver = Pirate()
John_Silver.drink_rum()
print(John_Silver.hows_goin_mate())
John_Silver.drink_rum()
print(John_Silver.hows_goin_mate())
John_Silver.drink_rum()
print(John_Silver.hows_goin_mate())
John_Silver.drink_rum()
print(John_Silver.hows_goin_mate())
John_Silver.drink_rum()
print(John_Silver.hows_goin_mate())
John_Silver.drink_rum()
print(John_Silver.hows_goin_mate())
