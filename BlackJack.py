import random
from replit import clear
from art import logo

#function to generate a random card from the infinite deck of cards lists cards[]
def deal_card(list_of_cards):
    """Takes a list of cards and generates a random card"""
    randomItem = list_of_cards[random.randint(0,12)]
    return randomItem
    
#Function to return score
def calculate_score(list):
    score = sum(list)
    if score == 21 and len(list) == 2:
        return 0                #Blackjack:
    if 11 in list and score>21: #If the score is already over 21, remove the 11 and replace it with a 1
        list.remove(11)
        list.append(1)
    return score

#Compare scores and returns result according to condition
def compare(userScore, dealerScore):
    if userScore == dealerScore:
        return "Draw"
    elif dealerScore == 0:
        return "Lose! Opponent has a blackjack"
    elif userScore == 0:    
        return "You win with a Blackjack"
    elif userScore > 21:
        return "You went over! You lose"
    elif dealerScore > 21:
        return "Opponent went over. You win"
    elif userScore > dealerScore:
        return "You have higher score.. You Win"
    else:
        return "Opponent has higher score.. You Lose"


def play_Game(): #Recursion Function to run game in loop as long as player wants
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    dealer_cards = []
    gameover = False
    #loop to generate the first twwo cards for the user and the dealer
    for i in range (0,2):
        user_cards.append(deal_card(list_of_cards = cards))
        dealer_cards.append(deal_card(list_of_cards = cards))


    #Total of the first two cards in the list of cards
    while not gameover:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, Your score {user_score} ")
        print(f"Dealer's first card: [{dealer_cards[0]}]")

        if user_score == 0 or dealer_score == 0 or user_score>21:
                gameover = True
        else:
            user_next_deal = input("Type 'y' to add another card or 'n' to pass: ")
            if user_next_deal == "y":
                user_cards.append(deal_card(list_of_cards = cards))
                # print("cards-",user_cards, "score-" ,user_score)
            else:
                gameover = True

    #Computer deals 
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card(list_of_cards = cards))
        #Update comp score
        dealer_score = calculate_score(dealer_cards)

    print(f"\n Your final hand: {user_cards}, and your score is {user_score}")
    print(f"\n Opponent hand: {dealer_cards}, and his score is {dealer_score} \n")
    print(f"Result: {compare(userScore= user_score, dealerScore= dealer_score)} \n")

    restart = input("Do you want to restart the game? y/n  \n")
    if restart == "y":
        clear()
        play_Game()
play_Game()