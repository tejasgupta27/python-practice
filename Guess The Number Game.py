n = 1024 #number already given to computer
i = 9 #number of chances
print("Welcome to Guess the Number Game!\nNo. of guesses left: 10")
x='Y'
while i>=0 and (x=='Y' or x=='y'):
    #when all chances are over
    if i == 0:
        print("Your chances are over! :\\ \n Game Over!")
        x = input("Play again? (Y/N)")
        if x == "Y" or x == "y":
            i=9
        elif x == "N":
            print("Thanks for Playing!")
        else:
            print("Invalid Input!")
    
    a = int(input("Guess the number:\n")) #a = number guessed by end user
    print("No. of guesses left:", i)

     #when guessed number is more than given number
    if a>n:
        print("I guess you shoult try a smaller number...")
        i-=1
        print("No. of guesses left:", i)
        continue

     #when guessed number is less that given number
    elif a<n:
        print("Maybe you should try a larger number... ;)")
        i-=1
        print("No. of guesses left:", i)
        continue

     #when user guesses the number in first attempt
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

     #when user guesses the number, but not in first attempt
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
