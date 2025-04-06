"""
Python Farm Game - A simple grid-based game built with Pygame.
This module contains the main game logic, broken into functions for maintainability.
"""

# Base Imports
import sys

# Third Party Imports
import pygame


def init_constants():
    """Initialize and return game constants."""
    constants = {
        # Screen dimensions
        "SCREEN_WIDTH": 640,
        "SCREEN_HEIGHT": 480,
        "TILE_SIZE": 32,
        
        # Colors
        "WHITE": (255, 255, 255),
        "BLACK": (0, 0, 0),
        "GREEN": (0, 255, 0),
        "BROWN": (139, 69, 19),
        "BLUE": (0, 0, 255),
        "DARK_BROWN": (90, 50, 10),
        
        # Frame rate
        "FPS": 60,
        
        # Tile types
        "GRASS": 0,
        "TILLED_SOIL": 1
    }
    
    # Derived constants
    constants["GRID_WIDTH"] = constants["SCREEN_WIDTH"] // constants["TILE_SIZE"]
    constants["GRID_HEIGHT"] = constants["SCREEN_HEIGHT"] // constants["TILE_SIZE"]
    
    return constants


def init_game(constants):
    """Initialize game state and return required objects."""
    # Initialize pygame
    pygame.init()
    
    # Create the screen
    screen = pygame.display.set_mode((constants["SCREEN_WIDTH"], constants["SCREEN_HEIGHT"]))
    pygame.display.set_caption("Python Farm Game")
    
    # Clock for controlling frame rate
    clock = pygame.time.Clock()
    
    # Create a simple map (0 = grass, 1 = tilled soil)
    game_map = [[constants["GRASS"] for _ in range(constants["GRID_WIDTH"])] for _ in range(constants["GRID_HEIGHT"])]
    
    # Player settings
    player = {
        "pos": [constants["GRID_WIDTH"] // 2, constants["GRID_HEIGHT"] // 2],
        "color": constants["BLUE"],
        "speed": 5  # For smooth movement
    }
    
    return screen, clock, game_map, player


def handle_events(player, constants, game_map):
    """Handle game events and return whether the game should continue running."""
    for event in pygame.event.get():
        # Handle quitting the game
        if event.type == pygame.QUIT:
            return False
            
        # Handle key presses
        elif event.type == pygame.KEYDOWN:
            # Player movement
            handle_player_movement(event.key, player, constants)
            
            # Till soil with spacebar
            if event.key == pygame.K_SPACE:
                till_soil(player, game_map, constants)
            
    return True


def till_soil(player, game_map, constants):
    """Till the soil at the player's current position."""
    x, y = player["pos"]
    
    # Only till if the tile is grass (not already tilled)
    if game_map[y][x] == constants["GRASS"]:
        game_map[y][x] = constants["TILLED_SOIL"]
        print(f"Tilled soil at position: {player['pos']}")


def handle_player_movement(key, player, constants):
    """Handle player movement based on key press."""
    if key == pygame.K_UP and player["pos"][1] > 0:
        player["pos"][1] -= 1
    elif key == pygame.K_DOWN and player["pos"][1] < constants["GRID_HEIGHT"] - 1:
        player["pos"][1] += 1
    elif key == pygame.K_LEFT and player["pos"][0] > 0:
        player["pos"][0] -= 1
    elif key == pygame.K_RIGHT and player["pos"][0] < constants["GRID_WIDTH"] - 1:
        player["pos"][0] += 1
    
    # Print player position for debugging
    print(f"Player position: {player['pos']}")


def draw_map(screen, game_map, constants):
    """Draw the game map/grid."""
    for y in range(constants["GRID_HEIGHT"]):
        for x in range(constants["GRID_WIDTH"]):
            # Create a rectangle for the tile
            rect = pygame.Rect(
                x * constants["TILE_SIZE"],
                y * constants["TILE_SIZE"],
                constants["TILE_SIZE"], 
                constants["TILE_SIZE"]
            )
            
            # Draw the tile based on its type
            if game_map[y][x] == constants["GRASS"]:  # Grass
                pygame.draw.rect(screen, constants["GREEN"], rect)
            elif game_map[y][x] == constants["TILLED_SOIL"]:  # Tilled soil
                pygame.draw.rect(screen, constants["DARK_BROWN"], rect)
                
            # Draw grid lines
            pygame.draw.rect(screen, constants["BLACK"], rect, 1)


def draw_player(screen, player, constants):
    """Draw the player on the screen."""
    player_rect = pygame.Rect(
        player["pos"][0] * constants["TILE_SIZE"], 
        player["pos"][1] * constants["TILE_SIZE"], 
        constants["TILE_SIZE"],
        constants["TILE_SIZE"]
    )
    pygame.draw.rect(screen, player["color"], player_rect)


def render(screen, game_map, player, constants):
    """Render the game state to the screen."""
    # Clear the screen
    screen.fill(constants["BLACK"])
    
    # Draw the map and player
    draw_map(screen, game_map, constants)
    draw_player(screen, player, constants)
    
    # Update the display
    pygame.display.flip()


def game_loop(screen, clock, game_map, player, constants):
    """Main game loop."""
    game_running = True
    
    while game_running:
        # Handle events
        game_running = handle_events(player, constants, game_map)
        
        # Render the game
        render(screen, game_map, player, constants)
        
        # Control the frame rate
        clock.tick(constants["FPS"])


def main():
    """Entry point for the game."""
    # Initialize constants and game state
    constants = init_constants()
    screen, clock, game_map, player = init_game(constants)
    
    # Run the game
    game_loop(screen, clock, game_map, player, constants)
    
    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main() 