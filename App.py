# App.py
from Question import Question  # Corrected import statement

question_prompts = [
    "What color are apples?\n (a) Red\n (b) Green\n (c) Orange\n\n",
    "What color are Bananas?\n (a) black\n (b) Yellow\n (c) white\n\n",
    "What color are watermelons?\n (a) Red\n (b) blue\n (c) green\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for question, question_prompt in zip(questions, question_prompts):
        answer = input(question_prompt)
        if answer.lower() == question.answer.lower():
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
