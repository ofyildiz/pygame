class AbilityScore:
    def __init__(self,
                 strength, dexterity, constitution,
                 intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

class AbilityModifier:
    def __init__(self,
                 strength, dexterity, constitution,
                 intelligence, wisdom, charisma):
        self.strength = self.get_modifier(strength)
        self.dexterity = self.get_modifier(dexterity)
        self.constitution = self.get_modifier(constitution)
        self.intelligence = self.get_modifier(intelligence)
        self.wisdom = self.get_modifier(wisdom)
        self.charisma = self.get_modifier(charisma)

    def get_modifier(self, score):
        modifier = score//2 - 5
        return modifier

class Character():
    def __init__(self,
                 strength, dexterity, constitution,
                 intelligence, wisdom, charisma,
                 race):
        self.abilityscore = AbilityScore(strength, dexterity, constitution,
                                    intelligence, wisdom, charisma)
        self.abilitymodifier = None
        self.speed = None
        self.race = race
        self.set_traits()

    def set_traits(self):
        if self.race == 'Dwarf':
            self.abilityscore.constitution += 2
            self.speed = 25
        elif self.race == 'Elf':
            self.abilityscore.dexterity += 2
            self.speed = 30
        elif self.race == 'Halfling':
            self.abilityscore.dexterity += 2
            self.speed = 25
        elif self.race == 'Human':
            self.abilityscore.strength += 1
            self.abilityscore.dexterity += 1
            self.abilityscore.constitution += 1
            self.abilityscore.intelligence += 1
            self.abilityscore.wisdom += 1
            self.abilityscore.charisma += 1
            self.speed = 30
            self.abilitymodifier = AbilityModifier(self.abilityscore.strength,
                                                   self.abilityscore.dexterity,
                                                   self.abilityscore.constitution,
                                                   self.abilityscore.intelligence,
                                                   self.abilityscore.wisdom,
                                                   self.abilityscore.charisma)
