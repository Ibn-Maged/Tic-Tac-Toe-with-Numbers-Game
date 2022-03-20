# Tic Tac Toe with Numbers game version 3.0
# Author: Mohamed Maged 
# Date: 2/3/2022

#Defining the Board and the Valid Number Choices for the two Players
 
player1_nums = [1 , 3 , 5 , 7 , 9 ]                                 #Player 1's Valid Numbers
player2_nums = [0 , 2 , 4 , 6 , 8 ]                                 #Player 2's Valid Numbers
board = [[" "," "," "] , [" ", " ", " "] , [" ", " ", " "]]
step_count = 1

#Creating a Function to display the Board 
def display_board():
    for i in board:
        print(*i , sep="__|__")                                     #to print the elements seperated with __|__
    
       
# Geting 2 User Inputs for x and y Axises


def get_row():
    while True:                                      #infinite loop to take valid input 
        try:
            x = int(input("Enter the Row: "))
            x -= 1                                   #to match it with list indexing
            if x >= 0 and x <= 2:
                break
            else:
                print("Invalid Number! , Please Choose a Number Between 1 and 3")
        except ValueError:
            print("You Can Enter only Numbers!")                #Creating ValueError Exception to Force the User to Enter only Numbers 
    return x

def get_col():
    while True:                                   #infinite loop to take valid input 
        try:
            y = int(input("Enter the Column: "))
            y -= 1                                   #to match it with list indexing
            if y >= 0 and y <= 2:
                break
            else:
                print("Invalid Number! , Please Choose a Number Between 1 and 3")
        except ValueError:
            print("You Can Enter only Numbers!")              #Creating ValueError Exception to Force the User to Enter only Numbers
    return y



#function to update the board 

def state_update(x , y):
    if step_count % 2 != 0:                                  #odd step count -->  player 1
        print("Available Numbers: ", player1_nums)
        num = int(input("Please Choose a Number to Play: "))
        
        while True:                                    #infinite loop to check if the chosen number is still in the remaining choices 
            if num in player1_nums:
                board[x][y] = num                      #reassign the board with chosen number in the chosen position
                player1_nums.remove(num)               #remove the chosen number from player 1's list
                break
            elif num not in player1_nums:
                print("Invalid Number!")
                num = int(input("Please Choose a Valid Number to Play: "))

    else:                                                   #even step count --> player 2      
        print("Available Numbers: ", player2_nums)
        num = int(input("Please Choose a Number to Play: ")) 
        
        while True:                                   #infinite loop to check if the chosen number is still in the remaining choices
            if num in player2_nums:
                board[x][y] = num                     #reassign the board with chosen number in the chosen position 
                player2_nums.remove(num)              #remove the chosen number from player 2's list
                break
            else:
                print("Invalid Number!")
                num = int(input("Please Choose a Valid Number to Play: "))  
                

# Checking for Win Functions 

def check_horizontal(x):   
   try:
        if x == 0:
            if ( board[0][0] + board[0][1] +  board[0][2] ) == 15:
                return True         
        elif x == 1:
            if (board[1][0] + board[1][1] + board[1][2]) == 15:
                return True
        elif x == 2:
            if (board[2][0] + board[2][1] + board[2][2]) == 15:
                return True
   except TypeError:                            #Creating TypeError exception because the initial value of the board is string 
        print("" ,end="")                       #and the input is int to be able to add int to string without getting errors



def check_vertical(y):
    try:
        if y == 0:
            if (board[0][0] + board[1][0] + board[2][0]) == 15:
                return True         
        elif y == 1:
            if (board[0][1] + board[1][1] + board[2][1]) == 15:
                return True
        elif y == 2:
            if (board[0][2] + board[1][2] + board[2][2]) == 15:
                return True
    except TypeError:                         #Creating TypeError exception because the initial value of the board is string
        print("" ,end="")                     #and the input is int to be able to add int to string without getting errors

def check_diagonal():
    try:
        if board[1][1] != " " :              #" " is the initial value of the board elements
            if (board[0][0] + board[1][1] + board[2][2]) == 15:
                return True
            elif (board[2][0] + board[1][1] + board[0][2]) == 15:
                return True
    except TypeError:
        print("" , end="")               

def check_win(x,y):
    return check_horizontal(x) or check_vertical(y) or check_diagonal()

#Game Loop
    
while True:
    if step_count % 2 != 0:
        print("Player 1's Turn")
    else:
        print("Player 2's Turn")    
   
    display_board()

    while True:                        #Check if the location is empty
        x = get_row()
        y = get_col()
        if board[x][y] == " ":
            break    
        else:
            print("Location Occupied, Please Choose Another Location")
    
    state_update(x , y)
    
    if check_win(x,y):
        if step_count %2 != 0:
            print("Player 1 Won!")
            display_board()
            break
        else:
            print("Player 2 Won!")
            display_board()
            break
    elif step_count == 9 and not check_win(x,y):
        print("It is a Draw!")
        break
    print("\n")
    step_count += 1

    