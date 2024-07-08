# -----------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------")
        print(key)
        for i in options[question_num-1]:
            print(i)

        guess = input("Enter a guess (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)

        question_num += 1

    display_score(correct_guesses, guesses)
# -----------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong!")
        return 0
# -----------
def display_score(correct_guesses, guesses):
    print("-----------")
    print("RESULTS")
    print("-----------")

    print("ANSWERS: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("GUESSES: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+ str(score)+"%")
# -----------
def play_again():
    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {
    "Who invented Lamborghini?: ": "A",
    "What year was Lamborghini created?: ": "B",
    "Lamborghini is fierce rivals with which Supercar company?: ": "C",
    "Who founded the rival company?: ": "A"
}

options = [["A. Ferruccio Lamborghini", "B. Richard Feynman", "C. Dex Bryant", "D. Guido van Rossum"],
           ["A. 1953", "B. 1963", "C. 1973", "D. 1983"],
           ["A. Ford", "B. Porsche", "C. Ferrari", "D. McLaren"],
           ["A. Enzo Ferrari", "B. Henry Ford", "C. Ferdinand Porsche", "D. Bruce McLaren"]]


new_game()

while play_again():
    new_game()

print("Byee!")