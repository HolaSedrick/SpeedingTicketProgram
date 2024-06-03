# Python Project 01 - Speeding Ticket Calculator
#
# Sedrick Neighbors
# CIS-155-60 Intro To Programming
# Date: 4/17/23
#
# Program Description
# This program calculates speeding tickets for the Podunk Police Department.
# The fee structure is as follows:
#    $50 plus $5 for every mph over the speed limit
#    $200 fee for any speed over 90 mph
#    Fines are doubled if in a construction zone
#
# Pseudocode:
# def program():
#    input for speedlimit ("Speed limit: ")
#    input for clockedspeed ("Clocked Speed: ")
#    input for constructionzone ("Construction Zone? Y/N ")
#    constructionfee = constructionzone (for correct input string)
#    fine = 0 (fine is set to a default of 0)
#    if clockedspeed > speedlimit:
#        fine = (clockedspeed - speedlimit) * 5 + 50
#        if clockedspeed > 90:
#            fine += 200
#    if constructionfee == 'Y' or constructionfee == 'y':
#        fine = (fine * 2)
#        print fine message (constructionzone)
#    elif constructionfee == 'N' or constructionfee == 'n':
#        print fine message (no constructionzone)
#    else
#        print invalid input
# run program()
#
#
# Test Set and Results (speedlimit, clockedspeed, constructionzone):
#
# (50, 45, 'Y') ---- $0 No Fine
# (50, 50, 'Y') ---- $0 No Fine
# (50, 40, 'N') ---- $0 No Fine
# (40, 40, 'N') ---- $0 No Fine
# (70, 80, 'y') ---- $200 fine
# (75, 94, 'Y') ---- $690 fine
# (65, 98, 'n') ---- $415 fine
# (70, 82, 'N') ---- $110 fine
# (65, 85, 'B') ---- Invalid input
# (60, 95, 'c') ---- Invalid input
# (70, 45,  4 ) ---- Invalid input
#
#
def program():
    speedlimit = int(input("Speed Limit: "))
    clockedspeed = int(input("Clocked Speed: "))
    constructionzone = (input("Construction Zone? Y/N "))
    constructionfee = constructionzone
    fine = 0
    # if statements to compute the speeding fine if speed is over the limit 
    if clockedspeed > speedlimit:
        fine = (clockedspeed - speedlimit) * 5 + 50
        if clockedspeed > 90:
            fine += 200
    # if statement to check if user input 'Y' or 'y' to verify if speeding occured in a construction zone
    # if so, apply the appropiate fine calculation
    if constructionfee == 'Y' or constructionfee == 'y':
        fine = (fine * 2)
        print(f"The fine for driving", clockedspeed, "mph in a", speedlimit, "mph zone, while under construction is:", '${}'.format(fine))
    # elif statement to check if user input 'N' or 'n' to verify if speeding did not occur in a construction zone
    elif constructionfee == 'N' or constructionfee == 'n':
        print(f"The fine for driving", clockedspeed, "mph in a", speedlimit, "mph zone is:", '${}'.format(fine))
    # else statement to return 'invalid input' if user input anything
    else:
        print('Invalid input')
program()


