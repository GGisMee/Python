import random, time

bot = 1

choices = ["rock", "paper", "scissors"]


def botplay():
    while bot == 0:
        def you_won():
            print("Congratulations, you won")

        def you_lost():
            print("You lost")

        def play_again():
            PlayChoice = None
            while PlayChoice not in choices:
                PlayChoice = input("Rock, Paper or Scissors?: ").lower()
            CompChoice = random.choice(choices)
            print("computer:", CompChoice)
            print("player:", PlayChoice)

            if PlayChoice == CompChoice:
                print("It was a tie, nobody won")
                if input("Play again?, Yes or No").lower() == "yes":
                    print()
                    play_again()
                else:
                    print("You may exit")
                    exit()

            elif PlayChoice == "rock":
                if CompChoice == "scissors":
                    you_won()
                else:
                    you_lost()

            elif PlayChoice == "paper":
                if CompChoice == "rock":
                    you_won()
                else:
                    you_lost()

            elif PlayChoice == "scissors":
                if CompChoice == "paper":
                    you_won()
                else:
                    you_lost()

        play_again()
        print("")


bot_eller_annan = input("Vill du köra lokalt eller mot en bot? Lokalt eller Bot?: ").lower()
if bot_eller_annan == "bot":
    bot = 0
    botplay()
else:
    def you_won():
        print("player 1 won")


    def you_lost():
        print("player 2 won")

    def play_again():
        p1, p2 = 1,1
        while p1 not in choices:
            p1 = input("Input player 1s choice now; Rock, Paper, Or Scissors: ").lower()
        print("Now for player 2")
        for i in range(0,100):
                print(i+1,"% break")
                time.sleep(0.01)

        while p2 not in choices:
            p2 = input("Input player 2s choice now; Rock, Paper, Or Scissors: ").lower()


        if p1 == p2:
            print("It was a tie, nobody won")
            if input("Play again?, Yes or No: ").lower() == "yes":
                print()
                play_again()
            else:
                print("You may exit")
                exit()
        elif p1 == "rock":
            if p2 == "scissors":
                you_won()
            else:
                you_lost()

        elif p1 == "paper":
            if p2 == "rock":
                you_won()
            else:
                you_lost()

        elif p1 == "scissors":
            if p2 == "paper":
                you_won()
            else:
                you_lost()
    play_again()