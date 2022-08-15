import Combat.entity_type as entity_type
import Combat.abilities as abilities
import pickle

while True:
  x=input("What do you want to do (h) for help (q) for exit: ")
  if x=="h":
    print("list of commands:")
    print("'add' <name: str> <texture: str> <list of moves: [str]> <max_health: int> <max_mana: int> <default armor: int>")
    print("'list' listar skit")
    print("'stats' <entity name> list stats for entity")
    print("rm <entity name> removes entity")
    print("if you add to a name that already exist then you remove the pribious")
    print("you need to q to save your changes maybe \n")

  if x == "q":
    with open(entity_type.FILENAME, "wb") as f:
      pickle.dump(entity_type.entity_data, f)
    break
    
  if x == "list":
    for i in entity_type.entity_data:
      print(i)

  if x.startswith("add"):
    t = x.split(" ")
    if not len(t)==7:
      print("expected 6 args")
    else:
      moves = [abilities.string_to_move_class(i.replace("_", " ")) for i in t[3].split(",")] # wtf
      entity_type.entity_data[t[1]] = entity_type.Entity_type(t[2], moves, int(t[4]), int(t[5]), int(t[6]))
      
  if x.startswith("stats"):
    t = x.split(" ")
    if not len(t) == 2:
      print("expected 1 arg")
    else:
      if t[1] in entity_type.entity_data.keys():
        print(entity_type.entity_data[t[1]])
      else:
        print(f"name {t[1]} not found")

  if x.startswith("rm"):
    t = x.split(" ")
    if not len(t) == 2:
      print(f"expected 1 arg, {len(t)-1} were given")
    else:
      if t[1] in entity_type.entity_data.keys():
        r=entity_type.entity_data.pop(t[1])
        print(f"{r} removed")
      else:
        print(f"name {t[1]} not found")
    
          