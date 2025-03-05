# project.py
# A T-Rex game implementation using Turtle, inspired by Google Chrome's offline game.
# AI tools (e.g., ChatGPT) were used to assist in structuring and debugging this code.

import turtle
import random
import time
import sys

# Attempt to import pyvirtualdisplay for headless environments
try:
    from pyvirtualdisplay import Display
    HEADLESS_MODE = True  # Assume headless unless DISPLAY is set
    import os
    if 'DISPLAY' in os.environ:
        HEADLESS_MODE = False  # Use real display if available
except ImportError:
    HEADLESS_MODE = False  # Fallback to requiring a real display if pyvirtualdisplay isn’t installed

# Constants
TREX_WIDTH = 20
TREX_HEIGHT = 40
TREX_DUCK_HEIGHT = 20
CACTUS_WIDTH = 10
CACTUS_HEIGHT = 30
PTERODACTYL_WIDTH = 30
PTERODACTYL_HEIGHT = 20
PTERODACTYL_LOW_Y = 20
PTERODACTYL_HIGH_Y = 40
JUMP_VELOCITY = 200  # pixels per second
GRAVITY = 500  # pixels per second squared
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 200
GROUND_Y = -50
BASE_SPEED = 100  # pixels per second
SPEED_INCREASE_INTERVAL = 10  # seconds
SPEED_INCREMENT = 10  # pixels per second
MIN_OBSTACLE_TIME = 1.0  # seconds
MAX_OBSTACLE_TIME = 3.0  # seconds

# Game state
state = {
    'trex_y': 0,
    'jumping': False,
    'ducking': False,
    'velocity': 0,
    'obstacles': [],
    'total_time': 0,
    'next_obstacle_time': 0,
    'score': 0,
    'game_over': False
}

# Global variable for game over message
game_over_turtle = None

def start_jump():
    """Initiate a jump for the T-Rex if it is not already jumping."""
    if not state['jumping']:
        state['jumping'] = True
        state['velocity'] = JUMP_VELOCITY

def update_trex(delta_time):
    """
    Update the T-Rex's vertical position based on jump mechanics.
    
    Args:
        delta_time (float): Time elapsed since the last update in seconds.
    """
    if state['jumping']:
        state['trex_y'] += state['velocity'] * delta_time
        state['velocity'] -= GRAVITY * delta_time
        if state['trex_y'] <= 0:
            state['trex_y'] = 0
            state['jumping'] = False
            state['velocity'] = 0

def update_obstacles(delta_time):
    """
    Move obstacles leftward and generate new ones periodically.
    
    Args:
        delta_time (float): Time elapsed since the last update in seconds.
    """
    # Compute current speed based on time elapsed
    num_increases = int(state['total_time'] / SPEED_INCREASE_INTERVAL)
    current_speed = BASE_SPEED + SPEED_INCREMENT * num_increases
    
    # Move existing obstacles
    for obs in state['obstacles']:
        obs['x'] -= current_speed * delta_time
    
    # Remove obstacles that are off-screen
    state['obstacles'] = [obs for obs in state['obstacles'] if obs['x'] > -obs['width']]
    
    # Generate new obstacles based on time
    state['total_time'] += delta_time
    if state['total_time'] >= state['next_obstacle_time']:
        obstacle_type = random.choice(['cactus', 'pterodactyl'])
        if obstacle_type == 'cactus':
            new_obstacle = {
                'x': SCREEN_WIDTH,
                'y': 0,
                'type': 'cactus',
                'width': CACTUS_WIDTH,
                'height': CACTUS_HEIGHT
            }
        else:
            y = random.choice([PTERODACTYL_LOW_Y, PTERODACTYL_HIGH_Y])
            new_obstacle = {
                'x': SCREEN_WIDTH,
                'y': y,
                'type': 'pterodactyl',
                'width': PTERODACTYL_WIDTH,
                'height': PTERODACTYL_HEIGHT
            }
        state['obstacles'].append(new_obstacle)
        state['next_obstacle_time'] = state['total_time'] + random.uniform(MIN_OBSTACLE_TIME, MAX_OBSTACLE_TIME)

def detect_collision():
    """
    Check if the T-Rex collides with any obstacle.
    
    Returns:
        bool: True if a collision occurs, False otherwise.
    """
    trex_height = TREX_DUCK_HEIGHT if state['ducking'] else TREX_HEIGHT
    trex_left = 50 - TREX_WIDTH / 2
    trex_right = 50 + TREX_WIDTH / 2
    trex_bottom = state['trex_y']
    trex_top = state['trex_y'] + trex_height
    
    for obs in state['obstacles']:
        obs_left = obs['x'] - obs['width'] / 2
        obs_right = obs['x'] + obs['width'] / 2
        obs_bottom = obs['y']
        obs_top = obs['y'] + obs['height']
        
        if (trex_left < obs_right and obs_left < trex_right and
            trex_bottom < obs_top and obs_bottom < trex_top):
            return True
    return False

def start_duck():
    """Start ducking if not jumping."""
    if not state['jumping']:
        state['ducking'] = True

def stop_duck():
    """Stop ducking."""
    state['ducking'] = False

def reset_game():
    """Reset the game state to start a new game."""
    global game_over_turtle
    state['trex_y'] = 0
    state['jumping'] = False
    state['ducking'] = False
    state['velocity'] = 0
    state['obstacles'] = []
    state['total_time'] = 0
    state['next_obstacle_time'] = random.uniform(MIN_OBSTACLE_TIME, MAX_OBSTACLE_TIME)
    state['score'] = 0
    state['game_over'] = False
    if game_over_turtle is not None:
        game_over_turtle.clear()
        game_over_turtle.hideturtle()

def main():
    """Set up and run the T-Rex game."""
    global game_over_turtle

    # Start virtual display if in headless mode
    display = None
    if HEADLESS_MODE:
        try:
            display = Display(visible=0, size=(SCREEN_WIDTH, SCREEN_HEIGHT))
            display.start()
            print("Running in headless mode with virtual display.")
        except ImportError:
            print("Error: pyvirtualdisplay is required for headless environments.")
            print("Run 'pip install pyvirtualdisplay' and ensure Xvfb is installed.")
            sys.exit(1)
        except Exception as e:
            print(f"Failed to start virtual display: {e}")
            sys.exit(1)

    # Initialize screen
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.tracer(0)  # Manual updates for smoother rendering
    
    # Create T-Rex turtle
    trex = turtle.Turtle()
    trex.shape("square")
    trex.penup()
    
    # Create score turtle
    score_turtle = turtle.Turtle()
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.goto(0, SCREEN_HEIGHT / 2 - 20)
    
    # Create game over turtle
    game_over_turtle = turtle.Turtle()
    game_over_turtle.hideturtle()
    game_over_turtle.penup()
    game_over_turtle.goto(0, 0)
    
    # List to hold obstacle turtles
    obstacle_turtles = []
    
    # Bind keys
    screen.onkey(start_jump, "space")
    screen.onkeypress(start_duck, "Down")
    screen.onkeyrelease(stop_duck, "Down")
    screen.onkey(lambda: reset_game() if state['game_over'] else None, "r")
    screen.listen()
    
    # Draw ground
    ground = turtle.Turtle()
    ground.hideturtle()
    ground.penup()
    ground.goto(-SCREEN_WIDTH / 2, GROUND_Y)
    ground.pendown()
    ground.goto(SCREEN_WIDTH / 2, GROUND_Y)
    
    # Game loop function
    def update():
        if not state['game_over']:
            delta_time = 0.02  # Approximately 50 FPS
            update_trex(delta_time)
            update_obstacles(delta_time)
            state['score'] += int(delta_time * BASE_SPEED)  # Score based on survival time
            
            # Determine T-Rex height
            trex_height = TREX_DUCK_HEIGHT if state['ducking'] else TREX_HEIGHT
            # Update T-Rex position and shape
            trex.shapesize(trex_height / 20, TREX_WIDTH / 20)
            trex.goto(50, GROUND_Y + state['trex_y'] + trex_height / 2)
            
            # Manage obstacle turtles
            while len(obstacle_turtles) < len(state['obstacles']):
                obs_turtle = turtle.Turtle()
                obs_turtle.shape("square")
                obs_turtle.penup()
                obstacle_turtles.append(obs_turtle)
            for i, obs in enumerate(state['obstacles']):
                obs_turtle = obstacle_turtles[i]
                obs_turtle.shapesize(obs['height'] / 20, obs['width'] / 20)
                obs_turtle.goto(obs['x'], GROUND_Y + obs['y'] + obs['height'] / 2)
                obs_turtle.showturtle()
        for i in range(len(state['obstacles']), len(obstacle_turtles)):
                obstacle_turtles[i].hideturtle()
            
            # Update score display
            score_turtle.clear()
            score_turtle.write(f"Score: {state['score']}", align="center", font=("Arial", 16, "normal"))
            
            # Check for collision
            if detect_collision():
                state['game_over'] = True
                game_over_turtle.write(f"Game Over! Final Score: {state['score']}", align="center", font=("Arial", 24, "normal"))
        
        screen.update()
        screen.ontimer(update, 20)  # Schedule next update in 20ms
    
    # Start the game
    reset_game()
    update()
    screen.mainloop()
    
    # Clean up virtual display if used
    if display:
        display.stop()

if __name__ == "__main__":
    main()