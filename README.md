<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/61b653a1-77d7-40c2-aa59-1383b3fd402f"
    alt="Last Hope Logo" 
    width="700"
  />
</p>

**Last Hope** is a terminal-based Python strategy game inspired by the classic **Battleships** board game, adapted into a science-fiction survival setting.

The player becomes the captain of humanity's last space fleet and must destroy hidden enemy alien ships by launching projectiles at coordinates on a 10x10 board.

> [!NOTE]
> This is a console-based Python game. It does not use external libraries, graphics engines, or a GUI.

---

## Overview

**Last Hope** is a turn-based coordinate attack game where the player must locate and destroy enemy ships hidden on a 10x10 grid.

The game includes:

- Arcade mode.
- Story mode.
- Multiple difficulty levels.
- Hidden enemy ships.
- Limited projectiles.
- Coordinate-based attacks.
- Hit and miss tracking.
- Developer options protected by password.
- Credits screen.
- ASCII title screens.
- Console-based story narration.

The gameplay is based on the logic of Battleships, but the setting has been changed into a space survival scenario where humanity fights against an alien threat.

> [!IMPORTANT]
> The project is written in Spanish and was created for educational purposes.

---

## Story

Humanity has abandoned Earth after it became uninhabitable due to a classified catastrophe.

During its journey through space, the last human fleet is attacked by an alien race. As the captain of the fleet, the player must defend humanity by destroying enemy ships before running out of projectiles.

As the story progresses, the fleet discovers that the alien race may come from a habitable planet. What begins as a battle for survival becomes a darker question about conquest, revenge, and whether humanity deserves a second chance.

> [!NOTE]
> The game uses a short narrative structure through captain log entries in **Story Mode**.

---

## Features

- Terminal-based gameplay.
- 10x10 game board.
- Random enemy ship placement.
- Ships with random size between 3 and 5 cells.
- Ships placed horizontally or vertically.
- Coordinate attack system.
- Hit and miss indicators.
- Limited projectile count.
- Win and lose conditions.
- Arcade mode with difficulty selection.
- Story mode with multiple scenes.
- Locked scene selection.
- Developer options menu.
- Password-protected settings.
- Option to show or hide enemy ships.
- Option to modify projectile count.
- ASCII title art.
- Credits and disclaimer screen.

---

## Project Structure

```text
LastHope/
│
├── LastHope.py
├── LICENSE
├── .gitignore
└── README.md
```

---

## File Description

| File | Description |
|---|---|
| `LastHope.py` | Main Python script containing the full game logic, menus, story, board generation, and gameplay loop. |
| `LICENSE` | Project license file. The current license is CC0 1.0 Universal. |
| `.gitignore` | Git ignore file for compiled files, build artifacts, and executables. |
| `README.md` | Project documentation. |

---

## Requirements

To run this project, you need:

- Python 3
- A terminal or command prompt

The project uses only Python standard libraries:

```text
random
os
time
sys
```

> [!TIP]
> No external packages need to be installed.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/LastHope.git
```

Enter the project folder:

```bash
cd LastHope
```

Run the game:

```bash
python LastHope.py
```

Or, depending on your system:

```bash
python3 LastHope.py
```

---

## How to Play

When the game starts, an ASCII title screen is displayed.

After that, the main menu appears:

```text
1. Modo Arcade.
2. Modo Historia (BETA).
3. Opciones.
4. Créditos.
0. Salir.
```

Select an option by typing its number.

---

## Game Board

The game uses a 10x10 board.

Rows are represented with letters:

```text
A B C D E F G H I J
```

Columns are represented with numbers:

```text
0 1 2 3 4 5 6 7 8 9
```

To shoot, enter a coordinate using a row letter and a column number.

Example:

```text
A3
```

> [!IMPORTANT]
> Coordinates must be written as one letter followed by one number, such as `A3`, `B7`, or `J9`.

---

## Board Symbols

| Symbol | Meaning |
|---|---|
| `*` | Unknown space that has not been attacked. |
| `O` | Hidden ship cell. Only visible when developer reveal mode is enabled. |
| `X` | Successful hit on a ship cell. |
| Empty space | Missed projectile. |
| `0` | Visible ship cell when reveal mode is enabled. |

---

## Game Objective

The objective is to destroy all enemy ships before running out of projectiles.

You win when all ship cells have been hit.

You lose when you run out of projectiles before destroying every enemy ship.

> [!WARNING]
> Projectiles are limited. Shooting the same coordinate twice is not allowed, but every valid shot still matters.

---

## Game Modes

## Arcade Mode

Arcade Mode allows the player to start a direct game with a selected difficulty.

The difficulty controls the number of enemy ships and available projectiles.

| Difficulty | Enemy Ships | Projectiles |
|---|---:|---:|
| Easy | `6` | `50` |
| Normal | `4` | `40` |
| Hard | `2` | `25` |

> [!NOTE]
> Fewer ships do not necessarily mean the game is easier, because harder modes also reduce the number of projectiles.

---

## Story Mode

Story Mode presents the game through a sequence of narrative scenes.

The story follows humanity's final fleet as it fights against an alien enemy and searches for a new home.

Story Mode includes:

- Scene-based narration.
- Different battles between scenes.
- Progression through story levels.
- A final ending scene.
- Unlockable scene selection after completing the story.

> [!IMPORTANT]
> Story Mode is marked as **BETA** in the game menu.

---

## Options Menu

The Options menu is protected by a password.

```text
AAJRR
```

The Options menu gives access to developer-style tools.

Available options include:

| Option | Description |
|---|---|
| Modify projectiles | Change the number of available projectiles. |
| Show ships | Reveal hidden enemy ship positions. |
| Hide ships | Hide enemy ship positions again. |
| Disable password | Remove password confirmation for settings. |
| Enable password | Restore password confirmation. |
| Unlock scene selection | Enable manual story scene selection. |
| Lock scene selection | Disable manual story scene selection. |
| Scene selector | Choose a specific story scene when available. |

> [!CAUTION]
> The Options menu can change the balance of the game. It is mainly useful for testing, debugging, or demonstration.

---

## Developer Password

The developer password is:

```text
AAJRR
```

It can be entered in two ways:

1. From the main menu by selecting **Opciones**.
2. During gameplay by typing `AAJRR` instead of a coordinate.

> [!TIP]
> Entering the password during gameplay opens the developer menu without leaving the current match.

---

## Gameplay Mechanics

## Ship Placement

Enemy ships are placed randomly on the board.

Ships can be placed in four directions:

- Left
- Right
- Up
- Down

Ships are not placed diagonally.

Each ship has a random size between:

```text
3 and 5 cells
```

The game checks that ships do not overlap before placing them on the board.

---

## Shooting System

The player attacks by entering coordinates.

Example:

```text
C5
```

The game checks whether the selected coordinate contains:

- Empty space
- A hidden enemy ship
- A previously attacked position

If the player hits a ship cell, the board marks it with:

```text
X
```

If the player misses, the board marks the position as an empty space.

---

## Ship Destruction

A ship is considered destroyed when all of its occupied cells have been hit.

The game tracks how many ships have been destroyed and how many remain.

The player wins when the number of destroyed ships equals the total number of enemy ships.

---

## Win Condition

The player wins when all enemy ships are destroyed.

When the player wins, the game displays a victory message and returns to the title/credits flow depending on the selected mode.

---

## Lose Condition

The player loses when there are no projectiles left.

When this happens:

- The full board is revealed.
- A defeat message is shown.
- The player is returned to the menu flow.

> [!WARNING]
> Running out of projectiles ends the game immediately.

---

## Controls

| Action | Input |
|---|---|
| Select menu option | Type a number and press `Enter` |
| Shoot projectile | Type a coordinate such as `A3` |
| Open developer menu during gameplay | Type `AAJRR` |
| Exit from main menu | Type `0` |

---

## Example Gameplay

Start the game:

```bash
python LastHope.py
```

Choose Arcade Mode:

```text
Selección: 1
```

Choose difficulty:

```text
1. Fácil.
2. Normal.
3. Difícil.

Selección: 1
```

Attack a coordinate:

```text
Introducir fila (A-J) y columna (0-9)
EJEMPLO(A3): B4
```

Possible result:

```text
¡¡Le diste!! Has dañado a una nave.
```

Or:

```text
Has fallado y no le has dado a ninguna nave...
```

---

## Educational Purpose

This project is useful for practicing:

- Python programming.
- Terminal-based applications.
- Game loops.
- Menus.
- Functions.
- Global variables.
- Conditional logic.
- Loops.
- Random generation.
- Matrix/list manipulation.
- Input validation.
- Coordinate systems.
- Basic game design.
- Turn-based mechanics.
- Story integration in a console game.

> [!NOTE]
> The project is especially useful as an introductory programming exercise because it combines logic, user interaction, and game rules in a single script.

---

## Code Structure

The main script includes functions for:

| Function Area | Description |
|---|---|
| Title screens | Displays ASCII art and section headers. |
| Credits | Shows the team members and educational disclaimer. |
| Developer options | Controls password-protected debugging options. |
| Board creation | Creates the 10x10 board. |
| Ship placement | Randomly places ships without overlapping. |
| Board printing | Displays the visible game board to the player. |
| Projectile validation | Checks whether user coordinates are valid. |
| Hit detection | Determines whether a shot hit or missed. |
| Ship destruction | Checks when a full ship has been destroyed. |
| Game over logic | Handles win and loss conditions. |
| Story mode | Displays story scenes and starts battles. |
| Main menu | Controls navigation between game modes. |

---

## Preview

### Screenshots

<img width="350" height="350" alt="Imagen pegada (3)" src="https://github.com/user-attachments/assets/1f96d422-5fa3-4d3e-b708-852ec13d686e" />

<img width="350" height="350" alt="Imagen pegada (2)" src="https://github.com/user-attachments/assets/a7b35ed2-dcb0-40ef-a142-c015bc36474c" />

<img width="350" height="350" alt="Imagen pegada (5)" src="https://github.com/user-attachments/assets/1ca8e740-4755-4383-9c75-805aa19ec243" />

<img width="350" height="350" alt="Imagen pegada" src="https://github.com/user-attachments/assets/b3d01cba-1728-4545-b0a3-acf71a4125bc" />

### Gameplay

<img width="1536" height="960" alt="Gameplay" src="https://github.com/user-attachments/assets/91a04a76-8db2-496b-a5ee-a398f6fab16e" />

---

## Credits

## Team

| Name | Student ID |
|---|---|
| Julio César Madrigal John | `A01737106` |
| Restituto Lara Larios | `A01737216` |
| Rodrigo López Guerra | `A01737437` |
| Alvaro Alberto Cruz Jiménez | `A01737453` |
| Alejandro Kong Montoya | `A0173427` |

---

## Inspiration

This game was inspired by the project and board game concept:

```text
Battleships
```

**Last Hope** recreates the base rules of Battleships and adapts them into a digital science-fiction environment.

> [!IMPORTANT]
> This project was created for educational purposes.

---

## Troubleshooting

## The screen does not clear correctly

The script uses:

```python
os.system('clear')
```

This works on Linux and macOS terminals.

On Windows, the equivalent command is:

```python
os.system('cls')
```

> [!TIP]
> If you are running the game on Windows and the screen does not clear, replace `clear` with `cls` in the script.

---

## Special characters do not display correctly

The story uses special Unicode characters and ANSI escape codes for bold text.

If the output looks strange:

- Use a modern terminal.
- Make sure your terminal supports UTF-8.
- Use a terminal that supports ANSI formatting.

---

## The game crashes after entering text in a numeric menu

Some menu inputs expect numbers.

If text is entered where the game expects a number, Python may raise an error.

> [!WARNING]
> Enter only numeric values in menus unless the game is asking for a coordinate or password.

---

## The developer password does not work

Make sure the password is entered exactly as:

```text
AAJRR
```

The program converts input to uppercase, so lowercase letters should also work.

---

## Possible Improvements

Future versions could include:

- Better input error handling for menu selections.
- Support for Windows screen clearing.
- Modular file structure instead of one long script.
- Separate files for story, board logic, and menus.
- Improved ship destruction detection.
- Cleaner board rendering.
- Save system for Story Mode.
- More story scenes.
- Better balancing for difficulty levels.
- Player statistics.
- Replay option after win or loss.
- Optional colorized board output.
- Multiplayer mode.
- Graphical version using Pygame.

> [!TIP]
> A strong next improvement would be replacing repeated `int(input(...))` calls with safer input validation to prevent crashes when the user types non-numeric text.

---

## License

This project is publicly available for educational and portfolio review purposes only.

The source code, visual assets, audio, videos, logos, screenshots, documentation, and other project materials may not be used, copied, modified, redistributed, sublicensed, or used commercially without explicit permission from the project authors.

All rights reserved unless otherwise stated.

> [!IMPORTANT]
> Some third-party assets, music, libraries, or references may be subject to their own licenses. Those materials remain owned by their original creators and are not covered by this project license. External concepts, names, or inspirations such as Battleships may have their own rights or trademarks. This project is presented as an educational adaptation.

---

## Disclaimer

**Last Hope** is an educational programming project.

It is inspired by the mechanics of Battleships and adapts them into a sci-fi terminal game.

> [!CAUTION]
> This project is not affiliated with any official Battleships brand, publisher, or rights holder.
