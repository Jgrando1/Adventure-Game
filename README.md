# Text-Based Adventure Game

## Overview
This is a Python-based text adventure game where players navigate through various rooms, interact with characters (both friendly and enemies), and use items to solve puzzles. The game includes a simple combat system, interactions with non-playable characters (NPCs), and the ability to collect and use items.

## Features
- **Room Navigation**: Explore different rooms and discover hidden secrets.
- **Character Interactions**: Talk to friendly characters, pickpocket enemies, and engage in combat.
- **Inventory System**: Collect items, such as keys, to unlock doors and progress in the game.
- **Combat Mechanics**: Fight enemies using items and strategies to defeat them.
- **Dynamic World**: Rooms are linked in multiple directions, creating a navigable game world.

## How to Play
1. **Navigate Rooms**: Use commands like `north`, `south`, `east`, and `west` to move between rooms.
2. **Interact with Characters**: 
    - Use `talk` to converse with characters.
    - Use `steal` to pickpocket enemies.
    - Use `fight` to engage in combat with enemies.
3. **Collect Items**: Pick up items to solve puzzles, such as using a key to unlock a door.
4. **Solve Puzzles**: Use the items you collect to progress further in the game.

### Example Commands:
- `north`, `south`, `east`, `west`: Move between rooms.
- `talk`: Speak to characters in the room.
- `steal`: Attempt to pickpocket enemies.
- `fight`: Fight an enemy using an item.
- `use key`: Use a key to unlock a door.

## Game Flow
- You start in a room and can navigate using the cardinal directions.
- As you explore, you'll encounter both friendly characters and enemies.
- Some rooms are locked and require specific items (such as a key) to access.
- Interact with characters to learn more about the environment and progress through the game.
- Be prepared to fight or evade enemies as you explore deeper into the game world.

## Installation & Setup
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/text-based-adventure-game.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd text-based-adventure-game
    ```
3. **Run the game**:
    ```bash
    python main.py
    ```

## Requirements
- Python 3.x

## Project Structure
```bash
├── character.py   # Contains the Character, Enemy, and Friend classes
├── room.py        # Contains the Room class
├── item.py        # Contains the Item class
├── main.py        # The main game loop
└── README.md      # This file
