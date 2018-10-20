turtles = [
    "Michelangelo",
    "Leonardo",
    "Raphael",
    "Donatello",
]

def shredder(names):
    if len(names) >= 1:
        names[0] = "Bebop"

shredder(turtles)

for turtle in turtles:
    print("* " + turtle)