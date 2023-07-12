'''
-time: 2023/07/12 15:09
-author: https://github.com/Arrieeee
'''


import random
import matplotlib.pyplot as plt
from tqdm import tqdm
from art import *

class Cards:
    def __init__(self, card_name):
        """
        Initialize a Card object with a given card name.
        
        Args:
        - card_name: A string representing the name of the card.
        """
        self.card_name = card_name 
        self.count = 0  # Counter to keep track of the number of times the card has been encountered

    @staticmethod
    def init_cards():
        """
        Create and initialize a list of Cards objects representing the Monopoly game cards.
        
        Returns:
        - A list of Cards objects.
        """
        cards = []
        # Create Cards objects for each card and append them to the list
        cards.append(Cards('GO/START'))
        cards.append(Cards('Mediterranean Avenue'))
        cards.append(Cards('Community Chest'))
        cards.append(Cards('Baltic Avenue'))
        cards.append(Cards('Income Tax'))
        cards.append(Cards('Reading Railroad'))
        cards.append(Cards('Oriental Avenue'))
        cards.append(Cards('Chance'))
        cards.append(Cards('Vermont Avenue'))
        cards.append(Cards('Connecticut Avenue'))
        cards.append(Cards('Jail'))
        cards.append(Cards('St. Charles Place'))
        cards.append(Cards('Electric Company'))
        cards.append(Cards('States Avenue'))
        cards.append(Cards('Virginia Avenue'))
        cards.append(Cards('Pennsylvania Railroads'))
        cards.append(Cards('St. James Place'))
        cards.append(Cards('Community Chest'))       
        cards.append(Cards('Tennessee Avenue'))
        cards.append(Cards('New York Avenue'))
        cards.append(Cards('Free Parking'))
        cards.append(Cards('Kentucky Avenue'))
        cards.append(Cards('Chance'))
        cards.append(Cards('Indiana Avenue'))
        cards.append(Cards('Illinois Avenue'))
        cards.append(Cards('B&O Railroads'))
        cards.append(Cards('Atlantic Avenue'))
        cards.append(Cards('Ventnor Avenue'))
        cards.append(Cards('Water Works'))
        cards.append(Cards('Marvin Gardens'))
        cards.append(Cards('Go To Jail'))
        cards.append(Cards('Pacific Avenue'))
        cards.append(Cards('North Carolina Avenue'))
        cards.append(Cards('Community Chest'))
        cards.append(Cards('Pennsylvania Avenue'))
        cards.append(Cards('Short Line'))
        cards.append(Cards('Chance'))
        cards.append(Cards('Park Place'))
        cards.append(Cards('Luxury Tax'))
        cards.append(Cards('Boardwalk'))
        return cards
    
    def name(self):
        return self.card_name
    

class Player:
    def __init__(self, cards):
        """
        Initialize a Player object with a list of cards and initialize counters for various statistics.
        
        Args:
        - cards: A list of Cards objects representing the game cards.
        """
        self.cards = cards

        self.player_index = 0  # Index representing the player's position on the game board
        self.single_roll = 0  # Counter for the number of times the player rolls the dice once
        self.double_roll = 0  # Counter for the number of times the player rolls the dice twice
        self.triple_roll = 0 # Counter for the number of times the player rolls the dice thirce
        self.send_to_jail = 0  # Counter for the number of times the player goes to jail

    def roll(self):
        """
        Simulate a dice roll and calculate the total move based on the dice values.
        
        Returns:
        - The total move value after rolling the dice.
        """
        total1 = total2 = 0

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        total1 = dice1 + dice2

        if dice1 == dice2:
            self.double_roll += 1
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            total2 = dice1 + dice2

            if dice1 == dice2:
                self.send_to_jail += 1
            else:
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)

                total3 = dice1 + dice2

                self.triple_roll += 1
                return total1 + total2 + total3
        else:
            self.single_roll += 1

        return total1

    def update_player_index(self, move_total):
        """
        Update the player's index based on the move total.
        
        Args:
        - move_total: The total move value after rolling the dice.
        """
        self.player_index += int(move_total)

    def reset_player_index(self):
        """
        Reset the player's index to zero.
        """
        self.player_index = 0

    def get_player_index(self):
        """
        Get the player's current index.
        
        Returns:
        - The player's current index as an integer.
        """
        return self.player_index

    def get_card_index(self, card_name):
        """
        Get the index of a card in the list of cards based on its name.
        
        Args:
        - card_name: The name of the card as a string.
        
        Returns:
        - The index of the card in the list of cards, or -1 if not found.
        """
        for index, card_obj in enumerate(self.cards):
            if card_obj.name() == card_name:
                return index
        return -1
          
    def update_card_stats(self, card_index):
        """
        Update the statistics of a card based on its index.
        
        Args:
        - card_index: The index of the card in the list of cards.
        """
        self.cards[card_index].count += 1


class Dice:
    def __init__(self, dice_side):
        """
        Initialize a Dice object with a specified dice side and set the count to zero.
        
        Args:
        - dice_side: A string representing the side of the dice.
        """
        self.side = dice_side
        self.count = 0  # Counter for the number of times this dice side appears

    @staticmethod
    def init_dice():
        """
        Initialize a list of Dice objects representing all possible dice sides.
        
        Returns:
        - A list of Dice objects.
        """
        dices = []
        dices.append(Dice('2'))
        dices.append(Dice('3'))
        dices.append(Dice('4'))
        dices.append(Dice('5'))
        dices.append(Dice('6'))
        dices.append(Dice('7'))
        dices.append(Dice('8'))
        dices.append(Dice('9'))
        dices.append(Dice('10'))
        dices.append(Dice('11'))
        dices.append(Dice('12'))
        return dices

    @staticmethod
    def update_dice_stats(dices, dice_side):
        """
        Update the statistics of a specific dice side in the list of Dice objects.
        
        Args:
        - dices: A list of Dice objects.
        - dice_side: The dice side to update the count for.
        """
        for dice in dices:
            if dice.side == dice_side:
                dice.count += 1
    

class Functions:
    def add_commas(number):
        """
        Add commas to a given number for improved readability.
        
        Args:
        - number: The number to add commas to.
        
        Returns:
        - A string representation of the number with commas added.
        """
        # Convert the number to a string
        number_str = str(number)
        result = []

        # Iterate through the characters in reverse order
        for i, char in enumerate(number_str[::-1]):
            # Add a comma after every third character
            if i != 0 and i % 3 == 0:
                result.append(', ')

            # Add the character to the result
            result.append(char)

        # Reverse the result and join the characters
        return ''.join(result[::-1])
    
    def plot_stats(cards, dices, total_rounds, single_roll, double_roll, triple_roll, send_to_jail):
        """
        Plot the statistics of card and dice occurrences in the game simulation.
        
        Args:
        - cards: A list of Card objects.
        - dices: A list of Dice objects.
        - total_rounds: The total number of rounds simulated.
        - single_roll: The count of single rolls.
        - double_roll: The count of double rolls.
        - triple_roll: The count of triple rolls.
        - send_to_jail: The count of times sent to jail.
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

        card_names = [card.card_name for card in cards]
        card_counts = [card.count for card in cards]
        card_percentages = [(count / total_rounds) * 100 for count in card_counts]

        bar_width = 0.4
        card_bars = ax1.bar(card_names, card_percentages, width=bar_width, label='Card')

        ax1.set_ylabel('Percentage')
        ax1.set_title(f'Chance of landing on certain cards when starting from Go (Rounds Simulated: {Functions.add_commas(total_rounds)})')
        ax1.tick_params(axis='x', rotation=90) 

        total_rolls = single_roll + double_roll + + triple_roll + send_to_jail

        single_roll_percentage = (single_roll / total_rolls) * 100
        double_roll_percentage = (double_roll / total_rolls) * 100
        triple_roll_percentage = (triple_roll / total_rolls) * 100
        send_to_jail_percentage = (send_to_jail / total_rolls) * 100

        roll_names = ['Once', 'Twice', 'Trice', 'Trice (Send To Jail)']
        roll_counts = [single_roll, double_roll, triple_roll, send_to_jail]
        roll_percentages = [single_roll_percentage, double_roll_percentage, triple_roll_percentage, send_to_jail_percentage]

        roll_colors = ['blue', 'green', 'yellow', 'red']  

        roll_bars = ax2.bar(roll_names, roll_percentages, width=bar_width, label='Roll', color=roll_colors)

        ax2.set_xlabel('Dice Numbers')
        ax2.set_ylabel('Percentage')
        ax2.set_title('Dice Statistics')

        dice_sides = [dice.side for dice in dices]
        dice_counts = [dice.count for dice in dices]
        dice_percentages = [(count / total_rounds) * 100 for count in dice_counts]

        dice_colors = ['orange']  

        ax2.bar(dice_sides, dice_percentages, width=bar_width, label='Dice', color=dice_colors)

        legend_labels = ['Chance To Roll (Once, Twice, Thrice)', 'Dice Number Chance']
        ax2.legend(legend_labels)  
        ax2.set_xticks(roll_names + dice_sides)  

        plt.tight_layout()  
        plt.show()

    def main():
        """
        Main game simulation logic.
        Simulates player rolls, updates card and dice statistics, and resets the player index.
        """
        move_total = player.roll()
        player.update_player_index(move_total)

        card_name = cards[player.get_player_index()].name()
        card_index = player.get_card_index(card_name)

        if card_index != -1:
            player.update_card_stats(card_index)
            Dice.update_dice_stats(dices, str(move_total))
            player.reset_player_index()

    def simulate_game(total_rounds):
        # Simulate the game for the specified number of rounds
        for _ in tqdm(range(total_rounds), desc='Processing...', unit='round'):
            Functions.main()
        # Plot the statistics of card and dice occurrences
        Functions.plot_stats(cards, dices, total_rounds, player.single_roll, player.double_roll, player.triple_roll, player.send_to_jail)

    def banner():
        title1 = text2art("MONOPOLY")
        title2 = text2art("SIMULATION")
        print(title1, title2)
        print('WARNING')
        print('BE CAUTIOUS NOT TO INPUT AN EXCESSIVELY LARGE NUMBER! Try 10000, and slowly go up.')

    
if __name__ == '__main__':
    # Initialize the cards, player, and dices
    cards = Cards.init_cards()
    player = Player(cards)
    dices = Dice.init_dice()

    # Get the total number of rounds to simulate from the user
    try:
        Functions.banner()
        total_rounds = int(input('Enter the number of rounds to simulate: '))
    except ValueError:
        print('Please enter a valid number.')
        exit()

    Functions.simulate_game(total_rounds)        
