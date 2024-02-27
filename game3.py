# File: CS112_A1_T2_Game3_20230557.py
# Purpose: Subtract a square game
# Author: Marwan
# ID: 20230557

print("""
#############################################################################

          This game starts with a custom number of coins,
    each player can take a non-zero square number of coins per turn,
                    last player take coins wins.

#############################################################################
""")
coins = "j"
while True:
    coins = input("Number of coins to start playing with (Normal is 13)")
    if coins.isnumeric():
        if int(coins) > 1:
            break
coins = int(coins)

def validNumber(n,total):
    # Must be numeric before compare it with total
    if n.isnumeric():
        n = int(n)
        # Must be less than total and not 0
        if n <= total and n > 0:
            # From 1 to the half of the number and used +2 because the case of 1
            for i in range(1,int(n/2)+2):
                # Square of i equal n
                if i*i == n:
                    return True
    # If non of these just return False
    return False
while True:
    n1 = "0"
    # Waits a valid input from the player 1
    while True:
        n1 = input("\nPlayer 1 inserts a valid non-zero square: ")
        # Base case when it's valid input break the loop
        if validNumber(n1,coins):
            break
    # Convert n1 from str to int
    n1 = int(n1)
    # Take the player's from the coins
    coins -= n1
    print(f"\nCoins now are {coins}")
    # Win case
    if coins == 0:
        print("\n** Player 1 wins $u$ **\n")
        break
    #
    #
    # Player 2
    n2 = "0"
    # Waits a valid input from the player 2
    while True:
        n2 = input("\nPlayer 2 inserts a valid non-zero square: ")
        # Base case when it's valid input break the loop
        if validNumber(n2,coins):
            break
    # Convert n2 from str to int
    n2 = int(n2)
    # Take the player's from the coins
    coins -= n2
    print(f"\nCoins now are {coins}")
    # Win case
    if coins == 0:
        print("\n** Player 2 wins $u$ **\n")
        break
