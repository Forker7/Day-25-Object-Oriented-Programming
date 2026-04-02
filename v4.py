class blox:

    species = "race"

    def __init__(self,race1,race2):
        self.race = race1
        self.race2 = race2

player1 = blox("angel","cyborg")
player2 = blox("rabbit","human")

print("player1 is",format(player1.species))
print("player2 is",format(player2.species))

print(player1.race,player1.race2)
print(player2.race,player2.race2)


