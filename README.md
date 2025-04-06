# Python Farm Game

A simple FarmVille-style game built with Pygame. This project is designed as a step-by-step learning tool for game development concepts.

## Current Features

- Grid-based map system (20x15 tiles at 32x32 pixels each)
- Player movement using arrow keys
- Simple tile rendering (grass and tilled soil)
- Farm tile system (tilling soil)
- Basic game loop

## How to Run

1. Make sure you have Python installed (Python 3.6+)
2. Install Pygame: `pip install pygame`
3. Run the game: `python main.py`

## Controls

- Arrow keys: Move player character
- Spacebar: Till soil at the player's current position

## Project Structure

- `main.py`: The main game file containing the game loop and basic functionality

## Development Roadmap

- [x] Basic grid and player movement
- [x] Farm tile system (tilling)
- [ ] Planting and growing crops
- [ ] Watering system
- [ ] Harvesting
- [ ] Day/night cycle
- [ ] Inventory system
- [ ] Shop and economy

## Code Organization Concepts

The game uses these key concepts:

- **Game Loop**: The central while loop that handles input, updates game state, and renders
- **Grid System**: Using a 2D array to track the state of each tile
- **Event Handling**: Capturing and responding to user input
- **Rendering**: Drawing game objects to the screen in the correct order
- **Tile System**: Different types of tiles (grass, tilled soil) with different visual appearances and functionality

Future improvements will add proper sprite handling and more sophisticated game state management.


# Vibe Coding Strategy
- Voice to code many new features
- Over time... it will get messy and bloated
- Force Cursor/chat to stay organized and also document everythin
- Eventually, AI won't figure it out and you'll need to manually fix