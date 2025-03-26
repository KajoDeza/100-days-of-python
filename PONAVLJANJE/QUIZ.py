questions = [
        {
                "question":"What is the Earth's natural satellite?",
                "options": ("A. NASA satellites", "B. Moon", "C. OneWeb"),
                "correct_answer":"B"

        },

        {
                "question":"What did Dante Alighieri write?",
                "options":("A. Divine Comedy", "B. Masha and the bear", "C. Crime and punishment"),
                "correct_answer": "A"

        },

        {
                "question":"What country is not a continent?",
                "options":("A. New York", "B. Australia", "C. Europe"),
                "correct_answer":"A"
        },

        {
                "question":"Can you feel pain in your brain?",
                "options":("A. Yes", "B. No", "C. Maybe"),
                "correct_answer": "B"
        },

        {
                "question":"If we throw a rock and a feather in the outer space, "
                           "which one will fall faster to the ground?",
                "options":("A. The rock", "B. Both", "C. The feather"),
                "correct_answer":"B"
        }
]

def quiz(questions):
        score = 0
        for question in questions:
                print(question["question"])
                for option in (question["options"]):
                        print(option)
                the_answer = input("What is your answer?: ").upper()
                if the_answer == question["correct_answer"]:
                        score += 1
                        print("Correct")
                else:
                        print("Wrong")

        print(f"Your total score is: {score} out of 5")

quiz(questions)