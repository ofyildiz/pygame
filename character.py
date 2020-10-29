import random as rd

class Ability:
    def __init__(self, base=0, temp=0):
        self.base, self.temp, self.score, self.mod = 0, 0, 0, 0

    def update(self, temp=0):
        self.temp = temp
        self.score = self.base + self.temp
        self.mod = (self.score)//2 - 5

class Stats:
    def __init__(self, str=0, dex=0, con=0, int=0, wis=0, cha=0):
        self.str = Ability(str)
        self.dex = Ability(dex)
        self.con = Ability(con)
        self.int = Ability(int)
        self.wis = Ability(wis)
        self.cha = Ability(cha)
        self.list = [self.str, self.dex, self.con, self.int, self.wis, self.cha]

    def update(self, list):
        for key, temp in enumerate(list):
            self.list[key].update(temp)

class Race:
    def __init__(self, race='Human'):
        self.race = race
        if self.race == 'Human':
            self.statboni = [1, 1, 1, 1, 1, 1]
            self.speed = 30
        elif self.race == 'Elf':
            self.statboni = [0, 2, 0, 0, 0, 0]
            self.speed = 30
        elif self.race == 'Dwarf':
            self.statboni = [0, 0, 2, 0, 0, 0]
            self.speed = 25
        elif self.race == 'Halfling':
            self.statboni = [0, 2, 0, 0, 0, 0]
            self.speed = 25
        else:
            self.statboni = [0, 0, 0, 0, 0, 0]
            self.speed = 25

class Dice:
    def __init__(self, typ=20):
        self.typ = typ
        self.result = typ

    def roll(self):
        self.result = rd.randint(1, self.typ)

class Job:
    def __init__(self, job='Barbarian'):
        self.job = job
        if self.job == 'Barbarian':
            self.hitdie = [Dice(12)]
        elif job == 'Bard':
            self.hitdie = [Dice(8)]

    def levelup(self):
        self.hitdie.append(Dice([self.hitdie[0].typ]))

class Character():
    def __init__(self, str=10, dex=10, con=10, int=10, wis=10, cha=10,
                 race='Human', job='Barbarian'):
        self.stats = Stats(str, dex, con, int, wis, cha)
        self.race = Race(race)
        self.stats.update([self.race.statboni])
        self.job = Job(job)
        self.level = 1
        self.exp = 0
        self.hitpoints = self.job.hitdie[0].typ + self.stats.con.mod

    def levelup(self):
        self.level += 1
        self.job.levelup()
        self.job.hitdie[-1].roll
        self.hitpoints += self.job.hitdie[-1].result + self.stats.con.mod
