# One-Dimensional Game of Life

The One-Dimensional Game of Life is a simple simulation that follows a set of rules to determine the birth, survival, or death of cells in a linear world. This C++ program offers an interactive way to explore the dynamics of cellular automata in a one-dimensional universe.

## Features

- **Customizable World Size**: Users can define the length of the one-dimensional world.
- **Generation Control**: Users can specify the number of generations to simulate.
- **Manual or Random Initial State**: Choose between manually inputting the initial state of the world or generating it randomly.
- **Visualization**: The program visually represents the state of the world for each generation.
- **Delay Between Generations**: Adds a 0.5-second delay between generations to better observe the simulation.
- **Replayability**: After a simulation ends, users can start a new one without restarting the program.

## Rules

- A cell dies if it has two neighbors or no neighbors.
- A cell survives if it has exactly one neighbor.
- An empty cell becomes alive if it has exactly one neighbor.

## How to Compile and Run

To compile the program, use a C++ compiler such as `g++`. Navigate to the directory containing the program and run the following command:

```bash
g++ -o GameOfLife GameOfLife.cpp
```

This command compiles the `GameOfLife.cpp` file and creates an executable named `GameOfLife`. To start the program, use:

```bash
./GameOfLife
```

## Usage Instructions

1. **Length of the World**: Input the desired size of the one-dimensional world.
2. **Number of Generations**: Specify how many generations you want to simulate.
3. **Initial State**: Choose between entering the initial state manually (`y`) or generating it randomly (`n`). If manually entering, input the positions of live cells one by one, followed by `-1` to finish.
4. **Observation**: Watch as the program simulates each generation, displaying the state of the world.
5. **Restart**: After the simulation ends, you can start a new one by responding `y` when prompted.

## Input Validation

The program includes comprehensive input validation to ensure a smooth user experience:

- Prompts for valid integers where required.
- Checks for logical input (`y` or `n`) for binary choices.
- Allows re-entry of inputs upon validation failure.

Enjoy exploring the fascinating dynamics of the One-Dimensional Game of Life!
