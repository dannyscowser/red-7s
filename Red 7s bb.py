# Red 7s card counting code

import random
import sys

# Define game objects
class Player:
    def __init__(self, money):
        self.money = money
        self.hand = []


class Dealer:
    def __init__(self):
        self.hand = []


# Define card objects
SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]
VALUES = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


# create card_count
card_count = -2

# Create Deck of Cards
deck = []
for suit in SUITS:
    for value in VALUES:
        deck.append(Card(suit, value))

random.shuffle(deck)

# Define the card images
card_images = {
    ("Hearts", "A"): "cards/ace_of_hearts.png",
    ("Hearts", 2): "cards/2_of_hearts.png",
    ("Hearts", 3): "cards/3_of_hearts.png",
    ("Hearts", 4): "cards/4_of_hearts.png",
    ("Hearts", 5): "cards/5_of_hearts.png",
    ("Hearts", 6): "cards/6_of_hearts.png",
    ("Hearts", 7): "cards/7_of_hearts.png",
    ("Hearts", 8): "cards/8_of_hearts.png",
    ("Hearts", 9): "cards/9_of_hearts.png",
    ("Hearts", 10): "cards/10_of_hearts.png",
    ("Hearts", "J"): "cards/jack_of_hearts.png",
    ("Hearts", "Q"): "cards/queen_of_hearts.png",
    ("Hearts", "K"): "cards/king_of_hearts.png",
    ("Diamonds", "A"): "cards/ace_of_diamonds.png",
    ("Diamonds", 2): "cards/2_of_diamonds.png",
    ("Diamonds", 3): "cards/3_of_diamonds.png",
    ("Diamonds", 4): "cards/4_of_diamonds.png",
    ("Diamonds", 5): "cards/5_of_diamonds.png",
    ("Diamonds", 6): "cards/6_of_diamonds.png",
    ("Diamonds", 7): "cards/7_of_diamonds.png",
    ("Diamonds", 8): "cards/8_of_diamonds.png",
    ("Diamonds", 9): "cards/9_of_diamonds.png",
    ("Diamonds", 10): "cards/10_of_diamonds.png",
    ("Diamonds", "J"): "cards/jack_of_diamonds.png",
    ("Diamonds", "Q"): "cards/queen_of_diamonds.png",
    ("Diamonds", "K"): "cards/king_of_diamonds.png",
    ("Clubs", "A"): "cards/ace_of_clubs.png",
    ("Clubs", 2): "cards/2_of_clubs.png",
    ("Clubs", 3): "cards/3_of_clubs.png",
    ("Clubs", 4): "cards/4_of_clubs.png",
    ("Clubs", 5): "cards/5_of_clubs.png",
    ("Clubs", 6): "cards/6_of_clubs.png",
    ("Clubs", 7): "cards/7_of_clubs.png",
    ("Clubs", 8): "cards/8_of_clubs.png",
    ("Clubs", 9): "cards/9_of_clubs.png",
    ("Clubs", 10): "cards/10_of_clubs.png",
    ("Clubs", "J"): "cards/jack_of_clubs.png",
    ("Clubs", "Q"): "cards/queen_of_clubs.png",
    ("Clubs", "K"): "cards/king_of_clubs.png",
    ("Spades", "A"): "cards/ace_of_spades.png",
    ("Spades", 2): "cards/2_of_spades.png",
    ("Spades", 3): "cards/3_of_spades.png",
    ("Spades", 4): "cards/4_of_spades.png",
    ("Spades", 5): "cards/5_of_spades.png",
    ("Spades", 6): "cards/6_of_spades.png",
    ("Spades", 7): "cards/7_of_spades.png",
    ("Spades", 8): "cards/8_of_spades.png",
    ("Spades", 9): "cards/9_of_spades.png",
    ("Spades", 10): "cards/10_of_spades.png",
    ("Spades", "J"): "cards/jack_of_spades.png",
    ("Spades", "Q"): "cards/queen_of_spades.png",
    ("Spades", "K"): "cards/king_of_spades.png"
}

# Create deal function
def deal():
    global card_count
    global deck

    # Check if the deck has less than 15 cards and shuffle if necessary
    if len(deck) < 15:
        for suit in SUITS:
            for value in VALUES:
                deck.append(Card(suit, value))
        random.shuffle(deck)
        card_count = -2

    player.hand.append(deck.pop())
    dealer.hand.append(deck.pop())
    player.hand.append(deck.pop())
    dealer.hand.append(deck.pop())


# Should figure out a way to decide when to shuffle

# Calculate Hand Value
def hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card.value == "A":
            aces += 1
        elif card.value == "J" or card.value == "Q" or card.value == "K":
            value += 10
        else:
            value += card.value
    if aces > 0:
        if value + 11 + (aces - 1) > 21:
            value += aces
        else:
            value += 11 + (aces - 1)
    return value


def count_Cards(hand):
    temp_count = 0
    for card in hand:
        if card.value in range(2, 7) or (card.value == 7 and card.suit == 'Hearts') or (
                card.value == 7 and card.suit == 'Diamonds'):
            temp_count += 1
        elif card.value in [8, 9] or (card.value == 7 and card.suit == 'Spades') or (
                card.value == 7 and card.suit == 'Clubs'):
            temp_count += 0
        elif card.value in ["A", "K", "Q", "J", 1, 10, 11]:
            temp_count -= 1
    return temp_count


# Calculate Winner
def calculate_winner():
    p_value = hand_value(player.hand)
    d_value = hand_value(dealer.hand)
    # Check for Blackjack First
    if len(player.hand) == 2 and p_value == 21:
        print("You have Blackjack, you win!")
        player.money += int(bet * 2.5)
    elif len(dealer.hand) == 2 and d_value == 21:
        print("Dealer has Blackjack, dealer wins!")
    elif (len(player.hand) == 2 and p_value == 21) and (len(dealer.hand) == 2 and d_value == 21):
        print("You both have Blackjack, you take even money!")
        player.money += int(bet * 2)
    # Bust
    elif p_value > 21 >= d_value:
        print("You bust, dealer wins!")
    elif p_value <= 21 < d_value:
        print("Dealer busts, you win!")
        player.money += int(bet * 2)
    # Regular Play
    elif p_value > d_value:
        print("McTominay! You win!")
        player.money += int(bet * 2)
    elif p_value == d_value and p_value <= 21 and d_value <= 21:
        print("A push is a win!")
        player.money += bet
    else:
        print("Dealer wins!")


# Player Actions
def player_actions():
    global bet
    while True:
        action = input("Hit (h), Hold (o), Double Down (d), or Split (s)? ")
        if action == "h":
            player.hand.append(deck.pop())
            print("You hit")
            print(f"Your new card is: {player.hand[-1]}, your total is {hand_value(player.hand)}")
            if hand_value(player.hand) > 21:
                print("You bust!")
                break
            else:
                continue
        elif action == "o":
            print("You hold")
            print("Your total:", hand_value(player.hand))
            break
        elif action == "d":
            if hand_value(player.hand) in [8, 9, 10, 11]:
                player.hand.append(deck.pop())
                player.money -= bet
                bet *= 2
                print("You doubled down")
                print(f"Your new card is: {player.hand[-1]}")
                break
            else:
                print("Can't double down")
                continue
        elif action == "s":
            if player.hand[0].value == player.hand[1].value:
                #player.hand.append(deck.pop())
                print("You could normally split here, but I haven't figured out how to do it yet.")
                continue
            else:
                print("Can't split")
                continue
        else:
            print("Invalid input")
            continue


def dealer_actions():
    while True:
        print("Dealer's next card:", dealer.hand[-1])
        while hand_value(dealer.hand) < 17:
            dealer.hand.append(deck.pop())
            print("Dealer's next card:", dealer.hand[-1])
        if hand_value(dealer.hand) > 21:
            print("Dealer busted!")
            break
        else:
            print("Dealer stays:", hand_value(dealer.hand))
            break


# Start Game
def start_game():
    global card_count
    global bet
    bet = 0
    deal()
    print(f"Your stack of cash: ${player.money}")
    while bet == 0:
        try:
            bet = int(input(f"You have ${player.money}. How much do you want to bet?"))
            if bet < 1 or bet > player.money:
                print(f"Hmm... You ain't that strapped. Bet must be between $1 and ${player.money}")
                bet = 0
                continue
            else:
                player.money -= bet
        except ValueError:
            print("Come on bro... Try again")
            continue
    print(f"Your hand: {player.hand[0]} and {player.hand[1]}. Your total is {hand_value(player.hand)}")
    print(f"Dealer's hand: {dealer.hand[0]}.")
    player_actions()
    dealer_actions()
    print(f'Your hand:', *player.hand, f"Your total is {hand_value(player.hand)}", sep=", ")
    #print(f"Your total: ", hand_value(player.hand))
    print(f"Dealer's hand:", *dealer.hand, f"Dealer's total is {hand_value(dealer.hand)}", sep=", ")
    #print(f"Dealer's total: ", hand_value(dealer.hand))
    player.count = count_Cards(player.hand)
    dealer.count = count_Cards(dealer.hand)
    final_count = player.count + dealer.count + card_count
    card_count = final_count
    while True:
        try:
            guess = int(input("Guess the count: "))
            if guess == final_count:
                print("Correct!")
                break
            else:
                print(f"Incorrect, count is {final_count}")
                break
        except ValueError:
            print("Sorry, that was not a valid integer. Please try again.")
    calculate_winner()
    if len(deck) < 15:
        print("New deck, the dealer shuffled the cards")
    player.hand = []
    dealer.hand = []


# Play Again
def play_again():
    global double
    while True:
        again = input("Play again (y/n)? ")
        if again == "y":
            double = 1
            if player.money < 1:
                print("You don't have enough money to play")
                sys.exit()
            else:
                start_game()
                play_again()
        elif again == "n":
            sys.exit()
        else:
            print("Please type y or n")
            continue


# Create Player
player = Player(337)
# Create Dealer
dealer = Dealer()

# Start Game
start_game()
play_again()