from quiz_class import quiz_class

# Creating the questions with alternatives OR the FIRST COLUMN

questions_cities = [

    "How many people live in the metropolitan area of Stockholm? \n (a) 1.8 million \n (b) 3.0 million \n (c) 2.2 million \n\n",
    "What is STRING? \n (a) a train line \n (b) an international transport line \n (c) a subway surrounding Oslo \n\n",
    "What is an ecological corridor? \n (a) portion of green land in urban context \n (b) a non deforested area \n (c) a portion of protected land in a rural area \n\n"
]

# Storing the correct answer for each question or the SECOND COLUMN

questions = [
    quiz_class(questions_cities [0], "c"),
    quiz_class(questions_cities [1], "b"),
    quiz_class(questions_cities [2], "a")
]

# Defining the function

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("You got " + str(score) + "/" + str(len(questions)) + "Correct!")


run_test(questions)
