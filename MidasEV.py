import math
import matplotlib.pyplot as plt

MidasGold = 160
MidasXpMulti = 2.1

#This Value is For EV calculation
#XP EV = XP/xpPerGold
#If this value is 1 the EV of XP will be 1:1
#
#Level 1 Tome = 9.3 XP per gold
#Level 2 Tome = 11.1
#Level 3 Tome = 14.7
#Level 4 Tome = 16.5
#Level 5 Tome = 18.3
#
xpPerGold = 9.3

#Lane creep bounties increase based on game time
minutes = 10

class creep:
    def __init__(self, name, xp, gold) -> None:
        self.name = name
        self.xp = xp
        self.gold = gold

Creeps = list()

#Gold Bounties in Dota 2 have a RNG Range so im averaging them for this

#Lane Creeps
Creeps.append(creep("Melee Creep", 57, (34+39+(math.floor(minutes/7.5)*2))/2))
Creeps.append(creep("Ranged Creep", 77, (43+52+(math.floor(minutes/7.5)*6*2))/2))
Creeps.append(creep("Siege Creep", 88, (59+72)/2))

#Kobold Camp
Creeps.append(creep("Kobold Foreman", 31, (20+25)/2))
Creeps.append(creep("Kobold Soldier", 19, (14+18)/2))
Creeps.append(creep("Kobold", 19, (6+8)/2))

#Hill Troll Camp
Creeps.append(creep("Hill Troll Preist", 29, (19+22)/2))
Creeps.append(creep("Hill Troll Berserker", 31, (20+23)/2))

#Vhoul Camp
Creeps.append(creep("Vhoul Assassin", 31, (20+24)/2))

#Ghost Camp
Creeps.append(creep("Ghost", 47, (28+34)/2))
Creeps.append(creep("Fell Spirit", 31, (17+20)/2))

#Harpy Camp
Creeps.append(creep("Harpy Stormcrafter", 47, (29+33)/2))
Creeps.append(creep("Harpy Scout", 31, (21+24)/2))

#Centaur Camp
Creeps.append(creep("Centaur Conqueror", 90, (53+62)/2))
Creeps.append(creep("Centaur Courser", 31, (16+19)/2))

#Wolf Camp
Creeps.append(creep("Alpha Wolf", 66, (30+36)/2))
Creeps.append(creep("Giant Wolf", 47, (18+21)/2))

#Satyr Camp
Creeps.append(creep("Satyr Mindstealer", 47, (22+26)/2))
Creeps.append(creep("Satyr Banisher", 31, (12+14)/2))
Creeps.append(creep("Stayr Tormenter", 90, (62+73)/2))

#Ogre Camp
Creeps.append(creep("Ogre Frostmage", 47, (28+36)/2))
Creeps.append(creep("Ogre Bruiser", 31, (18+38)/2))

#Golem Camp
Creeps.append(creep("Mud Golem", 32, (24+27)/2))
Creeps.append(creep("Shard Golem", 17, (8+13)/2))

#Hellbear Camp
Creeps.append(creep("Hellbear Smasher", 90, (61+79)/2))
Creeps.append(creep("Hellbear", 66, (36+44)/2))

#Wildwing Camp
Creeps.append(creep("Wildwing Ripper", 90, (54+70)/2))
Creeps.append(creep("Wildwing", 19, (12+16)/2))

#Troll Camp
Creeps.append(creep("Dark Troll Summoner", 90, (43+50)/2))
Creeps.append(creep("Hill Troll", 47, (21+26)/2))

results = dict()

for X in Creeps:
    gold = MidasGold - X.gold
    xp = X.xp * MidasXpMulti
    ev = gold + (xp/xpPerGold)

    results[X.name] = ev

#results sorted based on EV
sortedRes = sorted(results.items(), key=lambda x: x[1])

graphResX = list()
graphResY = list()

for X in sortedRes:
    graphResX.append(X[0])
    graphResY.append(X[1])

plt.bar(graphResX, graphResY)

plt.xticks(fontsize=8, rotation=75)

plt.xlabel("Creep")
plt.ylabel("EV")

plt.show()
