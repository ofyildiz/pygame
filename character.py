class AbilityScore:
    def __init__(self,
                 strength=0,
                 dexterity=0,
                 constitution=0,
                 intelligence=0,
                 wisdom=0,
                 charisma=0):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def __add__(self, other):
        strength = self.strength + other.strength
        dexterity = self.dexterity + other.dexterity
        constitution = self.constitution + other.constitution
        intelligence = self.intelligence + other.intelligence
        wisdom = self.wisdom + other.wisdom
        charisma = self.charisma + other.charisma
        abilityscore = AbilityScore(strength,
                                    dexterity,
                                    constitution,
                                    intelligence,
                                    wisdom,
                                    charisma)
        return abilityscore

    def return_modifier(self):
        mod = lambda score: score//2 - 5
        strength = mod(self.strength)
        dexterity = mod(self.dexterity)
        constitution = mod(self.constitution)
        intelligence = mod(self.intelligence)
        wisdom = mod(self.wisdom)
        charisma = mod(self.charisma)
        modifier = AbilityScore(strength,
                                dexterity,
                                constitution,
                                intelligence,
                                wisdom,
                                charisma)
        return modifier

class Race:
    def __init__(self,
                 race='Human'):
        self.race = race
        self.speed = 0
        self.abilityscore = AbilityScore()
        self.set_traits()

    def set_traits(self):
        if self.race == 'Human':
            self.abilityscore.strength += 1
            self.abilityscore.dexterity += 1
            self.abilityscore.constitution += 1
            self.abilityscore.intelligence += 1
            self.abilityscore.wisdom += 1
            self.abilityscore.charisma += 1
            self.speed += 30
        elif self.race == 'Elf':
            self.abilityscore.dexterity += 2
        elif self.race == 'Dwarf':
            self.abilityscore.constitution += 2
            self.speed += 25
            self.speed += 30
        elif self.race == 'Halfling':
            self.abilityscore.dexterity += 2
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
                 strength=10,
                 dexterity=10,
                 constitution=10,
                 intelligence=10,
                 wisdom=10,
                 charisma=10,
                 race='Human'):
        self.abilityscore_base = AbilityScore(strength,
                                              dexterity,
                                              constitution,
                                              intelligence,
                                              wisdom,
                                              charisma)
        self.race = Race(race)
        self.abilityscore = self.abilityscore_base + self.race.abilityscore
        self.abilitymodifier = self.abilityscore.return_modifier()
