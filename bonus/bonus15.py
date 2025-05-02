# this is so imp we have implemented mcq questions type, practice again
import json
with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:  # this is a nested for loop
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice =  int(input("Enter your answer:"))
    question ["user_choice"] = user_choice # this line take inout from user to check the correct answer


score = 0
for index, question in enumerate(data):

    if question["user_choice"] == question["correct_answer"]:
        # checking correct or not
        score = score + 1
        result  = "correct answer"
    else:
        result = "wrong answer"  # updating the score initial it was zero. whihch is defind on top score is o

    message = f"{result}{index + 1} - your answer: {question['user_choice']} " \
              f"correct answer:{question['correct_answer']}"
    print(message)# checking aand giving user what he entered
    


print(score, "/", len(data)) # it will print like 1 / 2 are correct.