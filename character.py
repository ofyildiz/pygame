class Ability:
    def __init__(self, base=0):
        self.base = base
        self.temp, self.mod, self.score = 0, 0, 0
        self.update()

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

    def __add__(self, other):
        str = self.str + other.str
        dex = self.dex + other.dex
        con = self.con + other.con
        int = self.int + other.int
        wis = self.wis + other.wis
        cha = self.cha + other.cha
        abilityscore = Stats(str,
                                    dex,
                                    con,
                                    int,
                                    wis,
                                    cha)
        return abilityscore

    def return_modifier(self):
        mod = lambda score: score//2 - 5
        str = mod(self.str)
        dex = mod(self.dex)
        con = mod(self.con)
        int = mod(self.int)
        wis = mod(self.wis)
        cha = mod(self.cha)
        modifier = Stats(str,
                                dex,
                                con,
                                int,
                                wis,
                                cha)
        return modifier

class Race:
    def __init__(self,
                 race='Human'):
        self.race = race
        self.speed = 0
        self.abilityscore = Stats()
        self.set_traits()

    def set_traits(self):
        if self.race == 'Human':
            self.abilityscore.str += 1
            self.abilityscore.dex += 1
            self.abilityscore.con += 1
            self.abilityscore.int += 1
            self.abilityscore.wis += 1
            self.abilityscore.cha += 1
            self.speed += 30
        elif self.race == 'Elf':
            self.abilityscore.dex += 2
        elif self.race == 'Dwarf':
            self.abilityscore.con += 2
            self.speed += 25
            self.speed += 30
        elif self.race == 'Halfling':
            self.abilityscore.dex += 2
            self.speed += 25

class Class:
    def __init__(self,
                 title='Barbarian'):
        self.title = title
        self.hit_dice = 0
        self.set_features()

    def set_features(self):
        if self.title == 'Barbarian':
            self.hit_dice += 12
        elif title == 'Bard':
            self.hit_dice += 8

class Character():
    def __init__(self,
                 str=10,
                 dex=10,
                 con=10,
                 int=10,
                 wis=10,
                 cha=10,
                 race='Human',
                 Class_='Barbarian'):
        self.abilityscore_base = Stats(str,
                                              dex,
                                              con,
                                              int,
                                              wis,
                                              cha)
        self.race = Race(race)
        self.Class = Class(Class_)
        self.abilityscore = self.abilityscore_base + self.race.abilityscore
        self.abilitymodifier = self.abilityscore.return_modifier()
