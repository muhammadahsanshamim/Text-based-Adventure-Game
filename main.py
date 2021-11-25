# Period: 3
# Date Created: Septemer 20th, 2021
# Name: Ahsan Shamim
# Description: Menu for Text-Based Adventure Game



# prints the introduction of the game
print("""
You are an archaeologist who travels around the world.
searching for mysteries and myths.
One day, you hear about reported sightings of a long-lost anciet City filled with gold.
you leave for the Amazonian rainforest to find the City.
You have arrived.
While you are on the way towards the City, you are met by The Themyscrian warriors.
The Themyscrian wariors are an ancient group of warriors who guard the city. 
Presumed dead and extinct.
They live in hiding and protect the city and its treasure.
You are warned against entering the city and from taking its treasure.
Weary of ther warning, You find the city and enter it.
You find the gold, but suddenly, the Themyscrian warriors find you and chase you.
Your task is to take the gold and escape the city without getting caught.
You need to get out of the city, find the hidden escape tunnel and escape using the river.
You are in a mirage. You need to find your way out of the city.
You can go four directions: forward, backward, right, left
You also have an option to quit the game,
which is accessible from the menu
""")


# a list of all the valid actions in the menu


valid_actions = ["forward", "backward", "left", "right", "quit"]


def menu():
        """ Prints out the menu for all the possible actions
        taken by the user """
        print("""Choose an action:
    """)
        for action in valid_actions:
            print(f"* {action}")

# This defines the first action of the game


def action_1():
        """ Prints out the menu for input action to move in the map
        at Level 1 """
        print("""
      LEVEL 1
      """)
        menu()
        action_input = input("Action: ")
        if action_input.lower() in valid_actions[0]:
            print(f" Danger ")
            action_1()
        if action_input.lower() in valid_actions[1]:
            print(f" Wrong way! ")
            action_1()
        if action_input.lower() in valid_actions[2]:
            print(f" You are turning to the left side of the temple")
            action_2()
        if action_input.lower() in valid_actions[3]:
            print(f" danger ")
            action_1()
        if action_input.lower() in valid_actions[4]:
            print(" You have quit the game ")
            quit()
        elif action_input.lower not in valid_actions:
            print("Invalid direction!")
            action_1()

# This defines the second action by the user


def action_2():
        """ Prints out the menu for input action to move in the map
        at Level 2 """
        print("""
        LEVEL 2
        """)
        menu()
        action_input = input("Action: ")
        if action_input.lower() in valid_actions[0]:
            print(f" Keep walking ahead ")
            action_3()
        if action_input.lower() in valid_actions[1]:
            print(f" Wrong way! ")
            action_2()
        if action_input.lower() in valid_actions[2]:
            print(f" warriors ahead")
            action_2()
        if action_input.lower() in valid_actions[3]:
            print(f" warriors ahead ")
            action_2()
        if action_input.lower() in valid_actions[4]:
            print(" You have quit the game ")
            quit()
        elif action_input.lower not in valid_actions:
            print("Invalid direction!")
            action_2()

# This defines the third action by the user


def action_3():
        """ Prints out the menu for input action to move in the map
        at Level 3 """
        print("""
        LEVEL 3
        """)
        menu()
        action_input = input("Action: ")
        if action_input.lower() in valid_actions[0]:
            print(f" Keep walking ahead")
            action_4()
        if action_input.lower() in valid_actions[1]:
            print(f" Wrong way! ")
            action_3()
        if action_input.lower() in valid_actions[2]:
            print(f" Deadend")
            action_3()
        if action_input.lower() in valid_actions[3]:
            print(f" Deadend ")
            action_3()
        if action_input.lower() in valid_actions[4]:
            print(" You have quit the game ")
            quit()
        elif action_input.lower not in valid_actions:
            print("Invalid direction!")
            action_3()

# This defines the fourth action by the user


def action_4():
        """ Prints out the menu for input action to move in the map
        at Level 4 """
        print("""
        LEVEL 4
        """)
        menu()
        action_input = input("Action: ")
        if action_input.lower() in valid_actions[0]:
            print(f" Dead end ")
            action_4()
        if action_input.lower() in valid_actions[1]:
            print(f" Wrong way! ")
            action_4()
        if action_input.lower() in valid_actions[2]:
            print(f" Go a different direction")
            action_4()
        if action_input.lower() in valid_actions[3]:
            print(f" Turn right to walk towards the exit ")
            action_5()
        if action_input.lower() in valid_actions[4]:
            print(" You have quit the game ")
            quit()
        elif action_input.lower not in valid_actions:
            print("Invalid direction!")
            action_4()

# This defines the fifth action by the user


def action_5():
        """ Prints out the menu for input action to move in the map
        at Level 5 """
        print("""
        LEVEL 5
        """)
        menu()
        action_input = input("Action: ")
        if action_input.lower() in valid_actions[0]:
            print(f" Keep walking")
            action_6()
        if action_input.lower() in valid_actions[1]:
            print(f" Wrong way! ")
            action_5()
        if action_input.lower() in valid_actions[2]:
            print(f" Path blocked")
            action_5()
        if action_input.lower() in valid_actions[3]:
            print(f" Path blocked ")
            action_5()
        if action_input.lower() in valid_actions[4]:
            print(" You have quit the game ")
            quit()
        elif action_input.lower not in valid_actions:
            print("Invalid direction!")
            action_5()

# This defines the sixth action by the user


def action_6():
        """ Prints out the menu for input action to move in the map
        at Level 6 """
        print("""
        LEVEL 6
        """)
        menu()
        action_input = input("Action: ")
        if action_input.lower() in valid_actions[0]:
            print(f" Keep walking")
            action_7()
        if action_input.lower() in valid_actions[1]:
            print(f" Wrong way! ")
            action_6()
        if action_input.lower() in valid_actions[2]:
            print(f" Warriors ahead")
            action_6()
        if action_input.lower() in valid_actions[3]:
            print(f" Warriors ahead")
            action_6()
        if action_input.lower() in valid_actions[4]:
            print(" You have quit the game ")
            quit()
        elif action_input.lower not in valid_actions:
            print("Invalid direction!")
            action_6()

# This defines the seventh action by the user


def action_7():
        """ Prints out the menu for input action to move in the map
        at Level 7 """
        print("""
        LEVEL 7
        """)
        menu()
        action_input = input("Action: ")
        if action_input.lower() in valid_actions[0]:
            print(f" wall ahead ")
            action_7()
        if action_input.lower() in valid_actions[1]:
            print(f" Wrong way! ")
            action_7()
        if action_input.lower() in valid_actions[2]:
            print(f" Wall ahead")
            action_7()
        if action_input.lower() in valid_actions[3]:
            print(f" turn right towards the exit ")
            action_8()
        if action_input.lower() in valid_actions[4]:
            print(" You have quit the game ")
            quit()
        elif action_input.lower not in valid_actions:
            print("Invalid direction!")
            action_7()

# This defines the eighth action by the user


def action_8():
        """ Prints out the menu for input action to move in the map
        at Level 8 """
        print("""
        LEVEL 8
        """)
        menu()
        action_input = input("Action: ")
        if action_input.lower() in valid_actions[0]:
            print(f" Booby traps")
            action_8()
        if action_input.lower() in valid_actions[1]:
            print(f" Wrong way! ")
            action_8()
        if action_input.lower() in valid_actions[2]:
            print(f" Turn left. You are getting closer!")
            action_9()
        if action_input.lower() in valid_actions[3]:
            print(f" Booby traps ")
            action_8()
        if action_input.lower() in valid_actions[4]:
            print(" You have quit the game ")
            quit()
        elif action_input.lower not in valid_actions:
            print("Invalid direction!")
            action_8()

# This defines the ninth action by the user


def action_9():
        """ Prints out the menu for input action to move in the map
        at Level 9 """
        print("""
        LEVEL 9
        """)
        menu()
        action_input = input("Action: ")
        if action_input.lower() in valid_actions[0]:
            print(f""" You found the exit! """)
            end_script()
            quit()
        if action_input.lower() in valid_actions[1]:
            print(f" Wrong way! ")
            action_9()
        if action_input.lower() in valid_actions[2]:
            print(f" Run away")
            action_9()
        if action_input.lower() in valid_actions[3]:
            print(f" Run away ")
            action_9()
        if action_input.lower() in valid_actions[4]:
            print(" You have quit the game ")
            quit()
        elif action_input.lower not in valid_actions:
            print("Invalid direction!")
            action_9()


def end_script():
    """ This function prints out the ending message of the game """
    print("""
    You have successfully escaped out of the temple and
    you have completed the game.
    """)

while True:
    action_1()
    action_2()
    action_3()
    action_4()
    action_5()
    action_6()
    action_7()
    action_8()
    action_9()