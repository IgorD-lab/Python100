# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
import pypokedex

pokemons = {}

# Improvement - request pokemons by name or search for them by number or display list of pokemons or numbers 50-100 example
# Also display all info about a pokemon
# Maybe turn into a full game
for i in range(1, 50):
    p = pypokedex.get(dex=i)
    
    pokemons[p.name] = p.types
    
table = PrettyTable()    

table.add_column("Pokemon Name", list(pokemons.keys()))
table.add_column("Type", [', '.join(types) for types in pokemons.values()])

table.align = "l"

print(table)