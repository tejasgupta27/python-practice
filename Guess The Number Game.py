def game():
    n = 1024
    i = 9
    print("Welcome to Guess the Number Game!\nNo. of guesses left: 10")
    x='Y'
    while i>=0 and (x=='Y' or x=='y'):

        if i == 0:
            print("Your chances are over! :\\ \n Game Over!")
            x = input("Play again? (Y/N)")
            if x == "Y" or x == "y":
                i=9
            elif x == "N":
                print("Thanks for Playing!")
            else:
                print("Invalid Input!")

        a = int(input("Guess the number:\n"))
        print("No. of guesses left:", i)

        if a>n:
            print("I guess you shoult try a smaller number...")
            i-=1
            print("No. of guesses left:", i)
            continue

        elif a<n:
            print("Maybe you should try a larger number... ;)")
            i-=1
            print("No. of guesses left:", i)
            continue

        elif a==n and i==9:
            print("Amazing! You guessed it in the first try! You'r epic!!")
            print("Congrats, You Won!")
            x = input("Play again? (Y/N)")
            if x == "Y" or x == "y":
                i = 9
                continue
            elif x == "N" or x == "n":
                print("Thanks for Playing!")
                break

        elif a==n:
            print("You guessed it right without using all the 10 chances!!")
            print("Congrats, You Won!")
            x = input("Play again? (Y/N)")
            if x == "Y" or x == "y":
                i = 9
                continue
            elif x == "N" or x == "n":
                print("Thanks for Playing!")
                break
game()