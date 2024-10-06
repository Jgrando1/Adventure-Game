import random

class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name}] says: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you.")
        return True


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend" + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + "crushes you, puny adventurer")
            return False
        
    
    def steal(self):
        print(f"You attempt to pickpocket {self.name}!")

        # 70% chance to successfully steal from an enemy
        success_chance = random.random()  # Generates a number from 0.0 to 1.0
        if success_chance < 0.7:
            stolen_items = ["Cobweb", "Coins", "Dust", "Slimey Key", "Mould"]
            stolen_item = random.choice(stolen_items)
            
            print(f"You successfully stole some {stolen_item} from {self.name}")
            
            # Check if the stolen item is the key
            if stolen_item == "Slimey Key":
                return "key"  # Return "key" to indicate the player has stolen the key
            else:
                return True  # Generic success for other items
        else:
            print(f"{self.name} catches you trying to steal and prepares for attack!")
            return False
        
        
    
    def bribe(self, amount):
        print(f"You try to bribe {self.name} with {amount} coins.")
        if amount > 50:
            print(f"{self.name} accepts the bribe and lets you pass.")
            return True
        else:
            print(f"{self.name} laughs at the small bribe and attacks!")
            return False

    def sleep(self):
        print(f"You try to read a story to {self.name} to send them to sleep.")

        # 40% chance to succeed in putting the enemy to sleep
        success_chance = random.random()  
        if success_chance < 0.4:
            print(f"{self.name} falls asleep. You can sneak by now.")
            return True
        else:
            print(f"{self.name} is too strong to fall asleep from your story!")
            return False
        
# New friend class 
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.favorite_gift = None

    # Setter
    def set_favorite_gift(self, gift):
        self.favorite_gift = gift

    # Hug interaction
    def hug(self):
        print(f"You hug {self.name}. {self.name} seems pleased and smiles warmly at you.")

    # Offer gift interaction
    def offer_gift(self, gift):
        if gift == self.favorite_gift:
            print(f"{self.name} accepts the {gift} with joy and thanks you profusely!")
        else:
            print(f"{self.name} politely declines your {gift} but still appreciates the gesture.")

        
        
        
        
