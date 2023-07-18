######################################################################### MACHINE SLOT ######################################################################################
import random
MAX_LINES = 3 #Number of lines a user can bet on
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values): #to check on the lines they bet on
    winnings = 0
    winnings_lines = []
    for line in range(lines): #for every line in lines
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check: #if symbol is not = to previous symbol
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines



def get_slot_machine_spin(rows, cols,symbols): #getting the slots to spin
    all_symbols = []
    for symbol,symbol_count in symbols.items():#iterating through the lists according to the number assigned to the symbol
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(rows):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows): #loop through the number of values we are to generat
            value = random.choice(all_symbols)#this picks a random value from this list
            current_symbols.remove(value)# we dont get to pick the value again
            column.append(value)# we then add the value to our column

        columns.append(column)
    return columns



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1: #if i = index
                print (column[row],  end=" | ") #print the pipe "|"
            else:
                print(column[row], end ="")#don't print the pipe

        print()


def deposit():
    while True: 
        amount = input("What would you like to deposit? $:") #user enters amount they want to deposit
        if amount.isdigit():#check to see if what the user has entered qualifies to be an integer or not
            amount = int(amount)
            if amount > 0:
                break
            else: #if user enters non-value number
                print("Amount must be greater than 0.")
        else:
            print("Please enter amount")

    return amount



def get_number_of_lines(): #user gets to determine from here the number of lines he wants to bet on
        while True: 
            lines = input("Enter the number of lines you wish to bet on(1-" + str(MAX_LINES)+ ")? $:") #user enters amount they want to deposit
            if lines.isdigit():#check to see if what the user has entered qualifies to be an integer or not
                lines = int(lines)
                if 1 <= lines <= MAX_LINES :
                    break
                else: #if user enters non-value number
                        print("Enter a valid number of lines")
            else:
                print("Please enter a number")

        return lines



def get_bet():
        while True: 
            amount = input("What would you like to bet on each line? $: ") #user enters bet choice
            if amount.isdigit():#check to see if what the user has entered qualifies to be an integer or not
                amount = int(amount)
                if MIN_BET <= amount <= MAX_BET:
                    break
                else: #if user enters non-value number
                    print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
            else:
                print("Please enter amount")

        return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()   
        total_bet = (bet * lines)

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")

        else:
            break 

    print(f"You are betting ${bet} on {lines} lines. Total bet amounts to: ${total_bet} ")

    print("Profile: "+ str(balance), lines)

    slots = get_slot_machine_spin(ROWS,COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main(): #we get to call the main function if the user wants to play again
    balance =  deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play(q to quit).")

        if answer == "q":
            break
        balance += spin(balance)
    print(f"You are left with ${balance}")
    
main()
 