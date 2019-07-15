#!/usr/bin/env python
# coding: utf-8

# # Black Jack. 

# 1. Bust when score is higher than 21. 
# 2. When dealer's value is more than 17, dealer stops hitting.
# 3. Higher score wins.

# In[5]:


import random


suits = ('Hearts','Diamonds','Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}




class Card:
    
    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
        
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"



class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:           
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_str = ''
        for card in self.deck:
            deck_str += '\n' + card.__str__()
        return f"The deck has: {deck_str}"
    
   
    def shuffle(self):
        random.shuffle(self.deck)
        
  
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        
        #card passed in from Deck.deal()        
        self.cards.append(card)
        self.value += values[card.rank]
        
        #To count how many Aces are in deck
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        while self.aces and self.value > 21 :
            self.value -= 10
            self.aces -= 1
            
            
            
            
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        
        #card passed in from Deck.deal()        
        self.cards.append(card)
        self.value += values[card.rank]
        
        #To count how many Aces are in deck
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        while self.aces and self.value > 21 :
            self.value -= 10
            self.aces -= 1
            
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
            
    
    def lose_bet(self):
        self.total-=self.bet
        
        
        
            
def take_bet(chips):
    
    while True:  
        try: 
            chips.bet = int(input("Please bet: "))
            
        except:
            if TypeError:
                print('Please type only numbers.')
            else:
                print('Error Occured Please Try Again')
            continue
            
        else:
            if chips.bet > chips.total:
                print("Sorry you do not have enough chips.")
                continue
            else:
                print('Thank you')  
                break
            
        finally:
            print(f"Chips Remained: {chips.total}\n")
            
            
            
            
            
            
def hit(deck,hand):
      
            single_card = deck.deal()
            hand.add_card(single_card)
            hand.adjust_for_ace()
            
           # print("Earend Points:", hand.value)
            

            
            
def hit_or_stand(deck,hand):
    
    global playing  # to control an upcoming while loop
        
    while True:
        question = input("Will you hit? (If yes, type: Y. If not, type: N) : ")
        
        if question == 'N':
            print("Hit unwanted.")
            playing = False  
            
        elif question == 'Y' :
            hit(deck,hand)

        else:
            print("please input Y or N.")
            continue
        break
        
        
        
        
        
        
def show_some(player,dealer):
    
    for card in player.cards:
        print("player's cards: ", card)
    for card in dealer.cards[1:]:
        print("dealer's cards:", card)
    
#   print(cards1,' ',cards2)   

def show_all(player,dealer):
    
    print("Player's score: ",player.value,"Dealer's score: ", dealer.value)
    
    for card in player.cards:
        print("player's card: ", card)
  
    for card in dealer.cards:
        print("dealer's cards: ", card)
        
        
        
        
        
def player_busts(player,dealer,chip):
        chip.lose_bet()
        print("Player Busted. Dealer Won")     

def player_wins(player,dealer,chip):
        chip.win_bet()
        print("Player Won")

def dealer_busts(player,dealer,chip):
        chip.win_bet()
        print("Dealer Busted. Player Won")
    
def dealer_wins(player,dealer,chip):
        chip.lose_bet()
        print("Dealer Won")
    
def push(player,dealer):
        print("Tie. Push.")
        
        
        
        
#**** The Game ********          

playing = True
while True:
    # Print an opening statement
    print("Welcome to Blackjack!")    
    # Create & shuffle the deck, deal two cards to each player
    deck=Deck()
    deck.shuffle()
    cards=deck.deal()
    
    player1=Hand()
    player2=Hand()

    player1.add_card(cards)
    player2.add_card(cards)
    player1.add_card(cards)
    player2.add_card(cards)
    
    # Set up the Player's chips
    chips=Chips()
    
    # Prompt the Player for their bet
    take_bet(chips)
    
    # Show cards (but keep one dealer card hidden)
    print("Cards obtained except for the first dealer's card: ")
    show_some(player1,player2)


    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player1)
            
        # Show cards (but keep one dealer card hidden)
        print("\n")
        show_some(player1,player2)
             
        # If player's hand exceeds 21, run player_busts() and break out of loop       
        if player1.value > 21:
            print("\n")
            player_busts(player1,player2,chips)
            break
            
        
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player1.value <= 21:
            while player2.value < 17:
                hit(deck,player2)
                hit_or_stand(deck,player1)  
                print("\n")
                show_some(player1,player2) 
                  
    
        # Run different winning scenarios

            if player2.value > 21:
                print("\n")
                dealer_busts(player1,player2,chips)
                playing = False
          
            elif player1.value > player2.value:
                print("\n")
                player_wins(player1,player2,chips)
                playing = False       
                
            elif player1.value < player2.value:
                print("\n")
                dealer_wins(player1,player2,chips)
                playing = False                  
        
            else:
                print("\n")
                push(player1,player2)
                playing = False 
                
    print("\nResults: ")
    show_all(player1,player2)
    print("\n")
            
    # Inform Player of their chips total 
    print("\n")
    print("Chips Remained:", chips.total)
    print("\n")
    
    # Ask to play again
    PlayAgain=input("Do you want to play again? Type 'Y' if yes.: ")
        
    if PlayAgain != 'Y':
        print("Game Over")
        break
        
    else:
        print("Game Restart")
        continue
        


# In[ ]:




