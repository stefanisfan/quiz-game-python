from database import intrebari
from preprocess import preprocess_data

# Test grila - 18 intrebari (Matematica, Fizica si Informatica)
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
        guess = input("Apasati (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("Raspunsul este corect! ")
        else:
            print("Raspunsul este gresit! ")
            print(f"{answers[question_num]} este raspunsul corect")
        question_num += 1

    print("\n------------------------------------------")
    print("-------------Rezultatul final-------------")
    print("------------------------------------------\n")

    print("Raspunsuri: ")
    for answer in answers:
        print(answer, end=" ")

    print("\n\nGhicitori:")
    for guess in guesses:
        print(guess, end=" ")

    score = int(score / len(intrebari) * 100)
    print(f"\nScorul este: {score}")