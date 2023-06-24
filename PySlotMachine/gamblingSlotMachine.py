#Text Based Slot Machine

#Global constant
#So we can use them anywhere in the scope of program

import random

MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        #I'm doing a for else statement here
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    #Below .items() is method that returns key value pair
    for symbol, symbol_count in symbols.items():
        # _ means, unanonymous var in python, if you dont care count use it
        for _ in range(symbol_count):
            all_symbols.append(symbol)

#This explanation is for columns = []
#[ [], [], [] ]  
#It's gonna be something like this so,
#So we randomly pick the value from list that we got earlier and gets appended to this
    columns = []    
    for _ in range(cols): # No need of i cause im not gonna use it
        column = []
        # [:] Doing that make sures its a copy list
        # And make sures we dont do any changes to the orginal list
        current_symbols = all_symbols[:]
        for _ in range(rows): # Same case why we use " _ "
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns 

def print_slot_machines(columns):
    for row in range(len(columns[0])):
        #Enumerate function basically stores the indexs i
        #Which i need here specifically
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
         #isdigit is a function that i can call on strings
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount should be greater than 0! ")
        else:
            print("Please Enter a number")   
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on(1-"+str(MAX_LINES)+')? ')
        if lines.isdigit():
            lines = int(lines)
            if lines>=1 and lines<=MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True: # Be very carefull while using using "while loop with True", cause if you dont have break statement that is going to run forever
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET: #Another way to compare  Normally we would have done #if bet<=MAX_BET and bet>=MIN_BET:
                break
            else:
                print(f"Amount must be in range ${MIN_BET} - ${MAX_BET}")  #Available for python >= 3.6 and easy way to do the formatting in py under print statements
        else:
            print("Please Enter a number")

    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have sufficent balance to bet that amount, your current balance is: {balance}")
        else:
            break
    print(f"You are betting on ${bet} on {lines} lines. Total bet is equal to: S{total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machines(slots)
    winnings,winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winnings_lines) #Splat operator / Unpact operator *
    return winnings - total_bet

    
def main():
    balance = deposit()
    #We put this inside the main function because,
    #If i want to play again
    #I can just call the main function,Then
    #It will be able to call my deposit function
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Press Enter to play (q to quit).")
        if answer == 'q':
            break
        balance += spin(balance)

    print(f"You are left with ${balance}")


main()





             
