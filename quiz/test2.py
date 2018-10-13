def likely_reference(skit):
    if skit == "Dead Parrot":
        print("stiff")
    elif skit == "Hungarian Phrasebook":
        print("eels")
    elif skit == "Lumberjack":
        if len(skit) < 3:
            print("sleeps all day")
        else:
            print("i'm okay")
    else:
        print("ni" * len(skit))
        
likely_reference("Lumberjack")
####

options = [
    "rock",
    "paper",
    "scissors",
    "flamethrower",
]

del options[3]
print("There are {} options".format(len(options)))


####
elements = [
    "Hydrogen",
    "Helium",
    "Lithium",
    "Symposium",
    "Beryllium",
    "Boron",
    "Carbon",
]

incorrect = elements.pop(3)
print("{} is not an element".format(incorrect))