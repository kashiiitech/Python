while True:    
    player1name = input("what's your name :")    #here we give input name for player 1
    player2name = input("and what's your name :")   # here we give name of player 2
    print("Select: Rock,Paper,Scissors")    # here just two player select rock,paper or scissors on which decided the winner
    
    player1 = input("do you want to choose rock,paper or scissors :")    #here player one select rock,paper or scissors
    player2 = input("do you want to choose rock,paper or scissors :")    # here player two select rock paper or scissors
    
    if player1 == player2:   #this condition shows sometime the selection of player one and player two will become same
        print("it's a tie!")    # if the selection of player one and player two will same it simply print this condition
        
    elif (player1=="rock"and player2=="scissors") or (player1=="scissors" and player2=="paper") or (player1=="paper" and player2 == "rock"):     #if the selsection of player one and player two is not same than if the conditions of this line will be true than simply playerone is winner if these conditions is false playertwo is winner
        print(player1name,"congratulations you won !")
    else:    #if above condition becomes false than this will become true
        print(player2name,"congratulations you win !")   # if the selection is not from the elif statement than this will be printed because game rules are define in elif statement but the selection is not from elif statement simply else statement will be printes
    repeat_again = input("do you want to try again [y/n] :")  # here this will simply shows play agian if use select y means yes than the if condition is true and loop will continue but if use select n means no then if condition will be false and else it will simply break the loop and game will be end!
    if repeat_again == "y":  # if user select y from the above options the loop will repeat itself
        continue   # and continue the loop
    else:   # if user select yes than if is true but if user select n means no or anyother word or character except y than the game will stopped
        break   #this will simply break the function when user does not select y
