from random import randint

print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!

What's your guess between 1 and 99?""")
rand_num = randint(1, 100)
tries = 0
number = input(">> ")
while number != "exit":
    try:
        guess = int(number)
        tries += 1
        if guess == rand_num:
            print("Congratulations, you got it!")
            if tries == 1:
                print("Wow! On the first try!")
            else:
                print("You won in %d attempts" % tries)
            if rand_num == 42:
                print("Answer to everything in the universe blah blah blah.")
            break
        elif guess < rand_num:
            print("Too low!")
        elif guess > rand_num:
            print("Too high!")
    except ValueError:
        print("That's not a number")
        continue
    number = input(">> ")
print("Bye bye")
