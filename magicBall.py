
import random
import time

play_again = 'yes'
print('Hello World, I am the Magic 8 Ball, What is your name?')
name = input()
print('Hello ' + name)

while play_again == 'yes':
    str(input("Welcome to the Magic 8-Ball. Enter your question: ")).lower()

    # Delay output for 1 second each
    print("Thinking...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print()

    # Generate a random integer/response
    response = random.randint(0, 20)

    if response == 1:
        print("Not just no, hell no!")
    elif response == 2:
        print("Sure thing.")
    elif response == 3:
        print("Don't count on it.")
    elif response == 4:
        print("Maybe not.")
    elif response == 5:
        print("Count on it.")
    elif response == 6:
        print("The Universe says maybe.")
    elif response == 7:
        print("I don't see why not.")
    elif response == 8:
        print("The future looks good for you.")
    elif response == 9:
        print("That's for sure.")
    elif response == 10:
        print("Maybe.")
    elif response == 11:
        print("There's a chance.")
    elif response == 12:
        print("Certainly!")
    elif response == 13:
        print("Keep doing what you're doing and it'll happen.")
    elif response == 14:
        print("Not over my dead 8 Ball.")
    elif response == 15:
        print("No.")
    elif response == 16:
        print("Yes.")
    elif response == 17:
        print("All depends on if you've been good for Santa this year.")
    elif response == 18:
        print("Not in this lifetime.")
    elif response == 19:
        print("Someday, but not today.")
    elif response == 20:
        print("Right after you hit the lottery.")
    else:
        print("Not a valid question!")

    play_again = str(input("Would you like to ask another question? yes/no ")).lower()
    if play_again == 'no':
        print("Goodbye! Thanks for playing!")
        exit()
    elif play_again=='yes':
        play_again='yes'
    else:
        print('I apologies, I did not catch that. Please repeat.')
        play_again='yes'


