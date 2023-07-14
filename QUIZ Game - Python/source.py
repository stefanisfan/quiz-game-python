from database import questions
from preprocess import preprocess_data

# Grid test - 18 questions (Mathematics, Physics and Computer Science)
def main():
    answers = ("D", "B", "B", "C", "A", "B", "A", "D", "C", "C", "A", "D", "A", "C", "B", "D", "D", "A")
    guesses = []
    score = 0
    question_num = 0

    quiz = preprocess_data()
    for k, v in quiz.items():
        print("------------------------------------------")
        print(k)
        print(v)
        print(', '.join(v))
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("The answer is corect! ")
        else:
            print("The answer is wrong! ")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    print("\n------------------------------------------")
    print("----------------Final Result----------------")
    print("------------------------------------------\n")

    print("Answers: ")
    for answer in answers:
        print(answer, end=" ")

    print("\n\nGuesses:")
    for guess in guesses:
        print(guess, end=" ")

    score = int(score / len(questions) * 100)
    print(f"\nThe score is: {score}")
