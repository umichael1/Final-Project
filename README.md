🦖 T-Rex Runner Game

🎥 Video Demo: [https://drive.google.com/file/d/128uWwTI1p5D-5BNmALJGhm6lHRJRWYLa/view?usp=shari
ng]

📌 Description

This project implements a T-Rex Runner Game using Python and Pygame, inspired by the classic Chrome offline game.

The player controls a T-Rex that runs endlessly across the screen. The objective is simple: jump over obstacles and survive as long as possible. The game increases in difficulty as time progresses, making it a fun and engaging challenge.

This project is a faithful recreation of the Chrome Dino game with added features such as:
✅ Smooth Jumping Mechanics
✅ Collision Detection
✅ Scoring System
✅ Game Reset on Collision

🎮 How to Play
    •    Press Spacebar to make the T-Rex jump.
    •    Avoid obstacles (cacti).
    •    If the T-Rex collides with an obstacle, the game ends.
    •    Try to beat your high score by surviving as long as possible!

🛠️ Project Features

✔ Realistic Jump Animation – The T-Rex jumps smoothly and lands naturally.
✔ Obstacle Movement – Cacti move towards the player, requiring perfect timing.
✔ Collision Detection – The game accurately detects when the T-Rex hits an obstacle.
✔ Score System – The longer you survive, the higher your score!
✔ Game Restart – After a collision, the game can be restarted.

📂 Project Structure

t-rex-runner/
│── t_rex_runner/         # Main project folder
│   │── project.py        # Main game logic
│   │── test_project.py   # Unit tests
│   └── requirements.txt  # Dependencies list
│── README.md             # Documentation
└── .gitignore            # Ignore unnecessary files

⚙️ Installation & Setup

✅ Step 1: Clone the Repository

git clone https://github.com/YOUR-USERNAME/t-rex-runner.git
cd t-rex-runner

✅ Step 2: Install Dependencies

pip install -r requirements.txt

✅ Step 3: Run the Game

python t_rex_runner/project.py

✅ Step 4: Run Tests

pytest t_rex_runner/test_project.py

🏗️ Game Development Breakdown

🔹 1. Setting Up Pygame & Game Window
    •    The game window is created using pygame.display.set_mode().
    •    The T-Rex and obstacles are drawn as rectangles.

🔹 2. Handling Jumping & Gravity
    •    The jump is controlled using spacebar input.
    •    A gravity system brings the T-Rex back down smoothly.

🔹 3. Moving Obstacles
    •    Obstacles move from right to left to create a scrolling effect.
    •    New obstacles spawn when old ones move off-screen.

🔹 4. Collision Detection
    •    The T-Rex’s colliderect() function detects crashes with obstacles.
    •    If a collision is detected, the game ends immediately.

🔹 5. Scoring System
    •    The player gains points each time an obstacle is avoided.
    •    The score is displayed on the game screen.

🔹 6. Restarting the Game
    •    After a game over, the player can restart by pressing a key.

🧪 Unit Testing with Pytest

We wrote three test functions to ensure the game runs correctly.

🔹 test_project.py

import pygame
from t_rex_runner.project import check_collision, reset_game, update_score

def test_check_collision():
    dino = pygame.Rect(50, 200, 40, 40)
    obstacle = pygame.Rect(50, 200, 20, 40)
    assert check_collision(dino, obstacle) == True  # ✅ Expect collision

    dino = pygame.Rect(50, 200, 40, 40)
    obstacle = pygame.Rect(200, 200, 20, 40)
    assert check_collision(dino, obstacle) == False  # ✅ No collision expected

def test_reset_game():
    reset_game()
    from t_rex_runner.project import dino, obstacle, score  # Re-import after reset
    assert dino.x == 50 and dino.y == 200  # ✅ Dino should reset
    assert obstacle.x == 800  # ✅ Obstacle should reset
    assert score == 0  # ✅ Score should reset

def test_update_score():
    from t_rex_runner.project import score
    initial_score = score
    update_score()
    assert score == initial_score + 1  # ✅ Score should increase by 1

🎨 Game Screenshots

Chrome Offline Game Version

Different T-Rex Runner Forks

🌍 Interesting Forks & Custom Versions

Many developers have modified the T-Rex game with unique themes! Here are some cool versions:

🎭 Kumamon Runner

🐻 Kumamon Runner – A cute bear-themed version!

🎼 Hello KuGou

🎵 Hello KuGou – A music-inspired take on T-Rex Runner.

🎮 T-Rex Runner Bot

🤖 T-Rex Runner Bot – An AI bot that plays the game!

🏎 Corona Runner

🦠 Corona Runner – A pandemic-themed version.

💡 Why This Project is Great for Learning

This T-Rex Runner game is more than just fun—it’s a great way to learn:
✅ Python basics – Loops, functions, conditionals
✅ Pygame fundamentals – Rendering, events, and animations
✅ Collision detection – How objects interact
✅ Game physics – Gravity and jumping mechanics

🎬 Next Steps

If you’d like to expand this game, here are some feature ideas:
    •    🎵 Add sound effects for jumping and collisions
    •    🌎 Make an online leaderboard
    •    🏆 Add power-ups (speed boost, double jump)

🚀 Have fun coding! Want to contribute? Fork this repo and start building! 🎮🔥

🔗 Useful Links
    •    Original Chrome Dino Game Source
    •    Play Online Version

🎯 Final Thoughts

This T-Rex Runner Game is a fun, easy-to-play, and highly addictive Python project. With smooth controls, an engaging challenge, and endless customization options, it’s a great introduction to game development! 🚀🔥

🎉 Now go and enjoy the game! 🎮
