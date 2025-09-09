import random
#initilizes user points
user_points = 500
print("DICE GAME")
#loop allows game to be replayed after losing and choosing to play again 
while True:
    #starts loop if user_points over 0 
    if user_points > 0:
        while user_points > 0:
            print(f"\nYou have {user_points} points.")
            #breaks loop and ends game if -1 entered using selection structure and break statement
            wager = int(input("Enter points to wager (-1 to QUIT): "))
            if wager == -1:
                print("\nThank you for playing! Goodbye!")
                user_points = -1
                break
            #asks to enter wager again if less than 1 using continue statement
            elif wager == 0:
                print(f"\nYou must wager at least one (1) point!")
                continue
            #asks to enter wager again if more than the amount of points user has
            elif wager > user_points:
                print(f"\nPlease enter a wager less than or equal to {user_points}!")
                continue
            
            #if wager entered follows all parameters, game begins 
            else:
                #loop used to continuosly enter wagers 
                while True:
                    #generates user dice 
                    user_dice_1 = random.randint(1, 6)
                    user_dice_2 = random.randint(1, 6)
                    #generates computer dice
                    computer_dice_1 = random.randint(1, 6)
                    computer_dice_2 = random.randint(1, 6)
                    #adds and displays computer and user dice totals
                    user = user_dice_1 + user_dice_2
                    computer = computer_dice_1 + computer_dice_2
                    print(f"\nYou rolled a [{user_dice_1}][{user_dice_2}]")
                    print(f"Computer rolled a [{computer_dice_1}][{computer_dice_2}]")
                    #checks if user wins or loses, and adds or subtracts wager points from user
                    if user > computer:
                        print(f"\nYou win {wager} points!")
                        user_points += wager
                        break
                    elif user < computer:
                        print(f"\nYou lose {wager} points!")
                        user_points -= wager
                        break
                    else:
                    #if tie, starts loop to ask user to roll again and continues asking if invalid input entered
                        print("\nIt's a tie!\n")
                        while True:
                            again = input("Enter 'R' to roll again: ")
                            if again == "r" or again == "R":
                                break
                            else:
                                print(f"\n{again} is an invalid input\n")
                                continue 
                continue
    #displays loss and asks user if they want to play again
    elif user_points == 0:
        print("GAME OVER! You have zero points left!\n")
        play_again = input("Would you like to play again (Y or N)? ")
        #if yes, adds 500 points to user again and restarts game
        if play_again == "Y" or play_again == "y":
            user_points += 500
            continue
        #if no, breaks loops and ends game
        elif play_again == "N" or play_again == "n":
            print("\nThank you for playing! Goodbye!")
            break
        #asks user again if invalid input
        else:
            print("Invalid input! Try again!\n")
            continue
    #breaks loop and ends game if -1 entered
    elif user_points == -1:
        break
