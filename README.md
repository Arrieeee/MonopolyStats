# Monopoly Card Landing Probability Simulation
This Python code simulates a game of Monopoly and calculates the chance of landing on each card when starting from the "Go" space. It also provides a visualization of the statistics to help understand the probabilities involved.

![example](https://github.com/Arrieeee/MonopolyStats/assets/94126075/93f71300-2fd5-4b10-af9c-3a753245a517)


# How to Use:
1. Clone the repository or download the monopoly_simulation.py file.
2. Make sure you have Python 3 installed on your system.
3. Install the required dependencies. You can do this by running the following command:
```bash
pip install matplotlib
pip install art
pip install tqdm
```
4. Open a terminal or command prompt and navigate to the directory where the monopoly_simulation.py file is located.
5. Run the code by executing the following command:
```bash
python monopoly_simulation.py
```
7. Follow the on-screen instructions to enter the number of rounds to simulate.

## Warning: Potential Performance Impact
- When entering the number of rounds to simulate, please be cautious not to input an excessively large number. Keep in mind that very large numbers can significantly impact the performance of your computer and       result in a long execution time for the simulation.
- For most practical purposes, a number like 100,000 is more than sufficient to obtain reliable results without putting undue strain on your system. It allows for a reasonably accurate representation of the          probabilities involved in the game.
- Please consider this warning and select an appropriate number of rounds, such as 100,000 or a similar magnitude, to strike a balance between accuracy and computational efficiency during the simulation.

## Functionality:
The code consists of the following classes:

- Cards: Represents the different cards in the Monopoly game. Each card has a name and a counter to track the number of times it has been encountered.
- Player: Represents a player in the game. It tracks the player's position, the number of times they go to jail, and the number of single and double rolls.
- Dice: Represents the dice used in the game. It tracks the count of each dice side.
- Functions: Contains utility functions for formatting numbers with commas and plotting the statistics.

Upon running the code, you will be prompted to enter the number of rounds to simulate. The program will simulate the game for the specified number of rounds. After the simulation, it will display a bar graph. Showing the chance of landing on each card when starting from the "Go" space. The graph also includes statistics on the dice rolls, including single rolls, double rolls, and instances of being sent to jail.

# Contribution:
Contributions to the code are welcome. If you have any suggestions, bug fixes, or improvements, please feel free to open an issue or submit a pull request.

# License:
Feel free to use and modify the code for your own purposes.
