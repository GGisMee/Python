def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print("------------------------------------------------------")
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("(Enter A, B, C or D): ").upper()
        guesses.append(guess)  # detta för att lägga till en och en för varje input!

        correct_guesses += check_awnser(questions.get(key), guess)
        question_num += 1  # ett annat sätt att skriva questions_num = questions_num + 1

    display_score(correct_guesses, guesses)
#  ----------------------------------------------------
def check_awnser(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0


#  ----------------------------------------------------
def display_score(correct_guesses, guesses):
    print("----------------------------------------------------")
    print("Results:")
    print("----------------------------------------------------")

    print("Answers:", end="") # end gör att det inte blir ett radnedhopp som slut utan börjar på samma rad!
    for i in questions:
        print(questions.get(i)+" ", end="")
    print()

    print("Guesses:", end="")
    for i in guesses:
        print(i+" ", end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
#  ----------------------------------------------------
def play_again():
    response = input(
        "----------------------------------------------------\nDo you want to paly again?: (Yes or No):").lower()
    if response == "yes":
        return True
    else:
        return False


#  ----------------------------------------------------

questions = {  # användning av dictionary för att stora flera values med ett value i sig
    "Question 1; Who created Python?: ": "A",
    "Question 2; What year was Python created?: ": "B",
    "Question 3; Python is tributed to which comedy group?: ": "C",
    "Question 4; Is the Earth round?: ": "A"
}  # dessa svar är de korrekta svaren!

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Suckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

new_game()
while play_again():
    new_game()
print("You may exit"), exit()