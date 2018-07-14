# usable variables (by players)
yes = 0
global yes
while (yes < 1):
    # squares
    chooseMove = 0
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"
    nine = "9"
    playerTurn = "x"
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    global ten
    global top_left
    global top_middle
    global top_right
    global mid
    global mid_right
    global mid_left
    global bot_left
    global bot
    global bot_right
    top_left = 0
    top_middle = 0
    top_right = 0
    mid_left = 0
    mid = 0
    mid_right = 0
    bot_left = 0
    bot = 0
    bot_right = 0

    def update():
        # Tic Tac Toe board
        global one
        global two
        global three
        global four
        global five
        global six
        global seven
        global eight
        global nine
        global ten
        global playerTurn
        global top_left
        global top_middle
        global top_right
        global mid
        global mid_right
        global mid_left
        global bot_left
        global bot
        global bot_right
        global top_leftx
        global top_middlex
        global top_rightx
        global midx
        global mid_rightx
        global mid_leftx
        global bot_leftx
        global botx
        global bot_rightx
        print("------------------")
        print("Tic Tac Toe!")
        print(
                "    " + one + " | " + two + " | " + three + "\n   ___|___|___\n    " + four + " | " + five + " | " + six + "\n   ___|___|___\n    " + seven + " | " + eight + " | " + nine + "\n      |   |")
        print("It is " + playerTurn + "'s turn")
        print("------------------")

        # Player chooses move

        chooseMove = int((input("Press the number\n that is your move\n   player " + playerTurn + ")\n>")))

        # Tests move and sets it

        if (chooseMove == 1 and playerTurn == "x"):
            one = "x"
            playerTurn = "o"
            top_leftx = 1
            return playerTurn
        if (chooseMove == 1 and playerTurn == "o"):
            one = "o"
            playerTurn = "x"
            top_left = 1
            return playerTurn
        if (chooseMove == 2 and playerTurn == "x"):
            two = "x"
            playerTurn = "o"
            top_middlex = 1
            return playerTurn
        if (chooseMove == 2 and playerTurn == "o"):
            two = "o"
            playerTurn = "x"
            top_middle = 1
            return playerTurn
        if (chooseMove == 3 and playerTurn == "x"):
            three = "x"
            playerTurn = "o"
            top_rightx = 1
            return playerTurn
        if (chooseMove == 3 and playerTurn == "o"):
            three = "o"
            playerTurn = "x"
            top_right = 1
            return playerTurn
        if (chooseMove == 4 and playerTurn == "x"):
            four = "x"
            playerTurn = "o"
            mid_leftx = 1
            return playerTurn
        if (chooseMove == 4 and playerTurn == "o"):
            four = "o"
            playerTurn = "x"
            mid_left = 1
            return playerTurn
        if (chooseMove == 5 and playerTurn == "x"):
            five = "x"
            playerTurn = "o"
            middlex = 1
            return playerTurn
        if (chooseMove == 5 and playerTurn == "o"):
            five = "o"
            playerTurn = "x"
            middle = 1
            return playerTurn
        if (chooseMove == 6 and playerTurn == "x"):
            six = "x"
            playerTurn = "o"
            mid_rightx = 1
            return playerTurn
        if (chooseMove == 6 and playerTurn == "o"):
            six = "o"
            playerTurn = "x"
            mid_right = 1
            return playerTurn
        if (chooseMove == 7 and playerTurn == "x"):
            seven = "x"
            playerTurn = "o"
            bot_leftx = 1
            return playerTurn
        if (chooseMove == 7 and playerTurn == "o"):
            seven = "o"
            playerTurn = "x"
            bot_left = 1
            return playerTurn
        if (chooseMove == 8 and playerTurn == "x"):
            eight = "x"
            playerTurn = "o"
            botx = 1
            return playerTurn
        if (chooseMove == 8 and playerTurn == "o"):
            eight = "o"
            playerTurn = "x"
            bot = 1
            return playerTurn
        if (chooseMove == 9 and playerTurn == "x"):
            nine = "x"
            playerTurn = "o"
            bot_rightx = 1
            return playerTurn
        if (chooseMove == 9 and playerTurn == "o"):
            nine = "o"
            playerTurn = "x"
            bot_right = 1
            return playerTurn
        if (one == "x" and two == "x" and three == "x"):
            print("X wins")
        if (top_leftx == 1 and top_middlex == 1 and top_leftx == 1):
            print ("X wins")
    # Reset board ect
    update()
    update()
    update()
    update()
    update()
    update()
    update()
    update()
    update()
    print(
            "    " + one + " | " + two + " | " + three + "\n   ___|___|___\n    " + four + " | " + five + " | " + six + "\n   ___|___|___\n    " + seven + " | " + eight + " | " + nine + "\n      |   |")
    duh = input("again y/n ")
    if (duh == "n"):
        yes = 1
