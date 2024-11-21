from resources.art import logoTreasure

print(logoTreasure)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# https://ascii.co.uk/art
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

while True:
    choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

    if choice1 == "left":
        choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
        if choice2 == "wait":
            choice3 = input("You arrive at the island unharmed. There is house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
            if choice3 == "red":
                print("It's a room fool of fire. Game Over")
            elif choice3 == "yellow":
                print("You found the treasure! You Win!")
            elif choice3 == "blue":
                print("You enter a room of beasts. Game Over.")
            else:
                print("You choose the door that doesn't exist. You fell into a void. Game Over")  
        else:
            print("You got attacked by an angry trout. Game Over.")
    else:
        print("You fell into a hole. Game Over.")

    continue_game = input('New Game? Yes/No\n').lower()

    if continue_game == "yes":
        pass
    else:
        break



