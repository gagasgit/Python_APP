import random

# AWS Certified Solutions Architect - Associate Quiz
questions = [
    {
        "question": "What is AWS?",
        "options": ["A. A cloud computing platform provided by Google",
                    "B. A cloud computing platform provided by Amazon",
                    "C. A cloud computing platform provided by Microsoft",
                    "D. A cloud computing platform provided by IBM"],
        "answer": "B"
    },
    {
        "question": "What is EC2 in AWS?",
        "options": ["A. A storage service", "B. A database service", "C. A computing service",
                    "D. A networking service"],
        "answer": "C"
    },
    {
        "question": "What is S3 in AWS?",
        "options": ["A. A compute service", "B. A storage service", "C. A database service", "D. A networking service"],
        "answer": "B"
    },
    # Add more questions here...
]


def take_quiz(questions):
    # Shuffle the questions
    random.shuffle(questions)

    # Keep track of the number of correct answers
    score = 0

    # Loop through the questions
    for i, question in enumerate(questions):
        # Print the question
        print(f"Question {i + 1}: {question['question']}")

        # Print the options
        for option in question['options']:
            print(option)

        # Get the user's answer
        answer = input("Your answer (A, B, C, or D): ")

        # Check if the answer is correct
        if answer.upper() == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question['answer']}.")

        print()

    # Print the final score
    print(f"You got {score} out of {len(questions)} questions correct.")


# Start the quiz
take_quiz(questions)
