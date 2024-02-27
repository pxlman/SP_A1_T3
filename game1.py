# File: CS112_A1_T2_1_20230005.py
# Purpose: Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.
# Author: Ahmed Ashraf Lotfy
# ID: 20230005

print("""
#####################################################################################
#####################################################################################

       There is a bottle and each player add from 1 to 10 drops of water.
          The player who fills the bottles with 100 drops first wins.

#####################################################################################
#####################################################################################
      """)

sum = 0
# Function to return True if the inserted number is valid ( Integer and 1<n<10 )
def validNumber(n):
    if n.isnumeric():
        n = int(n)
        if n < 1 or n > 10:
            return False
        return True
    return False
# The while True of the program
while True:
    n1 = ""
    # Taking input till the number is valid
    while not validNumber(n1):
        n1 = input("Player 1 must enter a valid number between 1 & 10:  ")
    # Adding the number to the sum
    sum+=int(n1)
    print(f"The sum is {sum}")
    if sum >= 100:
        print("Player 1 wins")
        break
    n2 = ""
    # Taking input till the number is valid
    while not validNumber(n2):
        n2 = input("Player 2 must enter a valid number between 1 & 10:  ")
    # Adding the number to the sum
    sum+=int(n2)
    print(f"The sum is {sum}")
    if sum >= 100:
        print("Player 2 wins")
        break