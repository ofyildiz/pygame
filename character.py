class Ability:
    def __init__(self,
                 strength, dexterity, constitution,
                 intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

class Modifier:
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
        if score > 10:
            return 1
        else:
            return -1

class Char(Modifier, Ability):
    def __init__(self,
                 strength, dexterity, constitution,
                 intelligence, wisdom, charisma):
        self.AbilitieScore = Ability(strength, dexterity, constitution,
                                     intelligence, wisdom, charisma)
        self.AbilityModifier = Ability(strength, dexterity, constitution,
                                       intelligence, wisdom, charisma)
