import getpass

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")
position = getpass.getpass(f"Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

guess = input("Guess the position of treasure: ")

if guess == position:
    print("Correct!")
else:
    print(f"Incorrect! Treasure was on {position}")    
print(f"{row1}\n{row2}\n{row3}\n")
