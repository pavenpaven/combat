import enum

class Move_type(enum.Enum):
  ATTACK = enum.auto()
  BUFF = enum.auto()

class Default_move:
  MANA_COST=0
  NAME="default move"
  TYPE=Move_type.ATTACK
  def function(self):
    return 10

class Heal_move(Default_move):
  MANA_COST=15
  NAME="heal move"
  TYPE=Move_type.BUFF
  def function(self, player):
    self.mana-=15
    player.health = min(player.health+5, player.max_health)

class Kick_move(Default_move):
  MANA_COST=10
  NAME="kick move"
  def function(self):
    self.mana-=10
    return 8*(1.8-(0.8*self.health/self.max_health))
  
LIST_OF_MOVES = [Default_move, Heal_move, Kick_move]

def string_to_move_class(str, move_class_list=LIST_OF_MOVES):
  for i in move_class_list:
    if i.NAME == str:
      return i
  raise Exception(f"Im afirad you can't do {str}, Dave.")