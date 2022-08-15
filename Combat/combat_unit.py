import Combat.abilities as abilities
import Combat.entity_type as entity_type

class Entity:
    def __init__(self, texture, moves, max_health, max_mana,
                 default_armor):
        self.texture=texture
        self.moves = moves
        self.health = max_health
        self.mana = max_mana
        self.armor = default_armor
        self.max_health = max_health
        self.max_mana = max_mana
        self.default_armor = default_armor 

    @classmethod
    def from_type(cls, type: entity_type.Entity_type):
        return cls(type.texture, type.moves, type.max_health, type.max_mana, type.default_armor)

    def take_damage(self, damage):
        self.health -= damage * (1 - self.armor) #change #why not change it? -chim. #no because like i need stregth and armor should bot be a number between 0 and 1 althou like -pav
        if self.health < 1:
            return 1
        return 0

    