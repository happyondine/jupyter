#!/usr/bin/env python
# coding: utf-8

# # Tic Tac Toe

# In[ ]:





# In[3]:


from IPython.display import clear_output
import random

def display_board(board):
    
    board='{0}|{1}|{2}\n- - -\n{3}|{4}|{5}\n- - -\n{6}|{7}|{8}'
    
    print(board.format(real_board[0],real_board[1],real_board[2],real_board[3],real_board[4],real_board[5],real_board[6],real_board[7],real_board[8]))

    
    
    
def player_input():  
        player1=''             
        while True:
            player1 = input("Please pick 'X' : \n ")          
            if player1=='x' or player1=='X':
                break   
                
                
def player_input2():  
        player2=''             
        while True:
            player2 = input("Please pick 'O' : \n ")          
            if player2=='O' or player2=='o':
                break                
            else:
                continue
                
                
                
def place_marker(test_board, marker, position):
    
    test_board[position-1]=marker
    return test_board





def win_check(board, mark):
    
    if (board[0]==board[1]==board[2]==mark) or (board[3]==board[4]==board[5]==mark) or (board[6]==board[7]==board[8]==mark) or (board[0]==board[3]==board[6]==mark) or (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[0]==board[4]==board[8]==mark) or (board[2]==board[4]== board[6]==mark):
         return True
  



def choose_first():
    
    x=random.randint(1,2) 
    #print('player%s'%x)
    
    
    player='player{}'.format(x)
    print(player)
    return player





def space_check(test_board, position):
    
    if test_board[position-1]==" ":
        return True
    else:
        return False
        
        
        
        
        
        
def full_board_check(board):
     
    y=True   
    for x in board:
        if x==' ':
            y=False

    return y         
       
     
        
        
        
def player_choice(test_board):
    
    position = 1
    
    while True:
        position = int(input('Please enter a number:\n'))
        
        space=space_check(test_board, position)
        if space==True:
            return position
            break
        

        
        
def replay():
    
            player=input("do you want to play again? press 't' if yes. ")
            if player=="t":
                print('game will restart')
                return True
            else:
                print('no replay')
            
            
            
            
#****** THE GAME ****



clear_output()

answer='t'
while(answer=='t'): 
        clear_output()
        print('Welcome to Tic Tac Toe!')
        real_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']        
        display_board(real_board)    
    
    
        #first player random selection
        
        #Player 1 turn: choose the input mark 'x'
        first=choose_first()
        
        if first=='player1':           
            print('you are player 1 ')
            mark='x'
            player_input()
            
        # Player2's turn: choose the input  mark 'o'
        else:           
            print('you are player 2')
            mark='o'
            player_input2()
            
        #choose the position
        pos= player_choice(real_board)            
        pos_int=int(pos)
        
        first_board=place_marker(real_board,mark,pos_int)
       
        display_board(first_board)
        
        
        #after first selection, next person plays
        
        print('next person play\n')
        
        while(answer=='t'): #while game_on:                
        
            #Player 1 Turn
            if first=='player1':           
                print('you are player 2 put O')
                mark='o'
                player_input2()
                first='player2'
                
            # Player2's turn.
            elif first=='player2':           
                mark='x'
                print('you are player 1 put X')
                player_input()
                first='player1'
                
            #choose the position   
            pos= player_choice(real_board)
            pos_int=int(pos)
            
            new_board=place_marker(real_board,mark,pos_int)           
            display_board(new_board)
            
            #win check
            win=win_check(new_board, mark)
            if win==True:
                print('{} Win'.format(mark))
                
                if not replay():
                    answer=''                   
                break
                
            #full check             
            full=full_board_check(new_board)
            if full==True:
                print("full board")
                
                if not replay():
                    answer=''
                break
            
            
print('game over!!!!!!!!')       
         


# In[ ]:




