# a dictionary that stores question and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1": {
        "question": "What is the capital of India?",
        "answer": "Delhi"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer: ")
    print("")

    if answer.lower() == value["answer"].lower():
        print("Correct Answer!!")
        score = score + 1
        print("Current Score is: " + str(score))
        print("")
        print("")

    else:
        print("Wrong Answer!!")
        print("The Correct answer is: " + value["answer"])
        print("Current Score is: " + str(score))
        print("")
        print("")


print("Got " + str(score) + " out of 4 Qestions Correctly!!")
print("")
print("Percentage is " + str(int(score / 4 * 100)) + "%")
print("")
