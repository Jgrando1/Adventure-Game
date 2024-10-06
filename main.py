from room import Room
from character import Friend
from character import Enemy
from item import Item


# Populate the map with some rooms. 

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
library = Room("Library")  
armory = Room("Armory")


# Set room descriptions
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate decorations")
library.set_description("Rows of dusty books line the walls, and the air smells of old parchment. A flickering candle casts eerie shadows.")  # Corrected
armory.set_description("Weapons and armor from a forgotten era line the walls, many covered in rust. A few glimmering pieces stand out.")


# Link the rooms correctly in both directions
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")

dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

ballroom.link_room(library, "west")
library.link_room(ballroom, "east")

kitchen.link_room(armory, "west")
armory.link_room(kitchen, "east")

# Create a friendly character
brown_fingers = Friend("Brown Fingers", "A friendly but cautious butler")
brown_fingers.set_conversation("Good day to you! There's a zombie roaming around here somewhere, He stays away from the kitchen for some reason...be careful!")
brown_fingers.set_favorite_gift("Soap")
kitchen.set_character(brown_fingers)

# Create an Enemy called dave; set a weakness + linked to a room
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

inventory = []
key = Item("Slimey Key", "A slimey key that opens the armory door..")
locked_door = True


# Starting room
current_room = kitchen


# Main loop for program 
while True:
    print("\n")
    current_room.get_details()
    
    # Checks whether there is a inhabitant in the room. 
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    
    # Checks the players command
    command = input("> ")
    
    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
        
    # Check for the talk command     
    elif command == "talk":
        if inhabitant is not None:
             inhabitant.talk()
        else:
            print("You are alone in this room..")  
    
     # New 'hug' command for the Friend class
    elif command == "hug":
        if isinstance(inhabitant, Friend):
            inhabitant.hug()
        else:
            print("This person doesn't want a hug.")
    
    # New 'offer gift' command for the Friend class
    elif command == "gift":
        if isinstance(inhabitant, Friend):
            print("What gift would you like to offer?")
            gift = input("> ")
            inhabitant.offer_gift(gift)
        else:
            print("You can't offer a gift to this person.")
          
    # Check for the fight command 
    elif command == "fight":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy): # check if the inhabitant is of enemy 
                print("What do you want to fight with?")
                fight_item = input(">")
                if inhabitant.fight(fight_item):
                    print(f"You defeated {inhabitant.name}!")
                    current_room.set_character(None) # remove enemy from the room if killed. 
                else:
                    print(f"{inhabitant.name} has defeated you adventurer! Game over.")
                    break # end if we die!
            else:
                print(f"{inhabitant.name} doesn't seem interested in fighting you.")
        else:
            print("There is no one here to fight.")
            
   # pickpocket command
    elif command == "steal":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            stolen_item = inhabitant.steal()
            if stolen_item == "key":
                print("You found a Slimey Key!")
                inventory.append(key)  # Add the key to the player's inventory
            elif stolen_item:
                print(f"You successfully stole from {inhabitant.name}!")
            else:
                print(f"{inhabitant.name} attacks you for stealing!")
                break
        else:
            print("There's no one here to steal from.")

    # bribery
    elif command == "bribe":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("How many coins will you offer?")
            bribe_amount = int(input("> "))
            if inhabitant.bribe(bribe_amount):
                current_room.set_character(None)  # Enemy lets you pass
            else:
                print(f"{inhabitant.name} attacks you!")
                break
        else:
            print("There's no one here to bribe.")

    # put the enemy to sleep
    elif command == "sleep":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            if inhabitant.sleep():
                print(f"{inhabitant.name} is asleep. You can sneak by.")
            else:
                print(f"{inhabitant.name} is too strong to fall asleep!")
        else:
            print("There's no one here to put to sleep.")
            
     # Use the key to open the locked door in the Armory
    elif command == "use key":
        if key in inventory and current_room == armory and locked_door:
            print("You use the key to unlock the door.")
            locked_door = False
        elif not locked_door:
            print("The door is already unlocked.")
        else:
            print("You don't have a key or you're not at the right door.")

    # Handle invalid commands
    else:
        print("Incorrect command, please try again.")
            
