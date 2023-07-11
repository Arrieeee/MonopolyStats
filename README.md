Monopoly Card Landing Probability Simulation

This Python code simulates a game of Monopoly and calculates the chance of landing on each card when starting from the "Go" space. It also provides a visualization of the statistics to help understand the probabilities involved.

How to Use:

1. Clone the repository or download the monopoly_simulation.py file.
2. Make sure you have Python 3 installed on your system.
3. Install the required dependencies. You can do this by running the following command:
pip install matplotlib
4. Open a terminal or command prompt and navigate to the directory where the monopoly_simulation.py file is located.
5. Run the code by executing the following command:
python monopoly_simulation.py
6. Follow the on-screen instructions to enter the number of rounds to simulate.
   
Functionality:
The code consists of the following classes:

1. Cards: Represents the different cards in the Monopoly game. Each card has a name and a counter to track the number of times it has been encountered.
2. Player: Represents a player in the game. It tracks the player's position, the number of times they go to jail, and the number of single and double rolls.
3. Dice: Represents the dice used in the game. It tracks the count of each dice side.
4. Functions: Contains utility functions for formatting numbers with commas and plotting the statistics.

Upon running the code, you will be prompted to enter the number of rounds to simulate. The program will simulate the game for the specified number of rounds. After the simulation, it will display a bar graph. Showing the chance of landing on each card when starting from the "Go" space. The graph also includes statistics on the dice rolls, including single rolls, double rolls, and instances of being sent to jail.

Contribution:
Contributions to the code are welcome. If you have any suggestions, bug fixes, or improvements, please feel free to open an issue or submit a pull request.

License:
Feel free to use and modify the code for your own purposes.
