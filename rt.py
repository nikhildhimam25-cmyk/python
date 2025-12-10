import pr
a=10
b=20
print(a-b)
def add():
  while True:   # <--- added loop so it repeats until correct answer matches
    quizz=[]
    q=input_something("enter question..")
    q1=input_something('1..enter option..')
    q2=input_something('2..enter option..')
    q3=input_something('3..enter option..')
    q4=input_something('4..enter option..')
    global q5
    q5=(input_something('correct option...'))

    # CHECK IF CORRECT OPTION MATCHES ANY OPTION
    if q5 not in [q1, q2, q3, q4]:
        print('Invalid! Correct option must match one of the 4 options.')
        print('Please enter again...\n')
        continue     # <--- ask again, DO NOT exit to main menu

    # If valid → save question
    quizz.append(q)
    quizz.append(q1)
    quizz.append(q2)
    quizz.append(q3)
    quizz.append(q4)

    ans.append(q5)
    quiz.append(quizz)
    print('Question added successfully')
    break   # <--- exit only after SUCCESS
