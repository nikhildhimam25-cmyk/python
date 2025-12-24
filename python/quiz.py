
print("-------WELCOME TO QUIZ APP---------")
def f(i):
  print(i)
def input_something(p):
   while True:
    op=input(p).strip().lower()
    if op:
       return op
    print("this cant be blank")
def add():
  quizz=[]
  q=input_something("enter question..")
  q1=input_something('1..enter option..')
  q2=input_something('2..enter option..')
  q3=input_something('3..enter option..')
  q4=input_something('4..enter option..')
  global q5
  q5=(input_something('correct option..'))
  quizz.append(q)
  quizz.append(q1)
  quizz.append(q2)
  quizz.append(q3)
  quizz.append(q4)
  quiz.append(quizz)
  print('Question added sucessfully')
def play():
  if not quiz:
    print("NO QUESTIONS YET")
  else:
   for i,j in enumerate(quiz[0:len]):
    print(j)
def delete():
  if not quiz:
    print("NO QUESTIONS YET")
  else:
    try:
     s=int(input('enter question number to delete '))-1
     p=quiz.pop(s)
     print('QUESTION DELETED SUCCESSFULLY')
    except Exception as e:
      print('Invalid Enter Again')
def listt():
  if not quiz:
    print("NO QUESTIONS YET")
  else:
    for i,j in enumerate(quiz,start=1):
     print(i,j)
quiz=[]
print("--SELECT--")
f("--[A]DD A QUIZ--")
f('--[L]IST OF ALL QUESTIONS--')
f('--[P]LAY QUIZ')
f('--[D]ELETE QUIZ--')
f('--[E]XIT--')
b=len(quiz)
while True:
  a=input('ENTER YOUR CHOICE..').lower().strip()
  if a=='a':
   (add())
  elif a=='p':
    (play())
  elif a=='l':
   (listt())
  elif a=='d':
    (delete())
  elif a=='e':
   print('GOODBYE BUDDY')
   print('HAVE A MARVELLOUS DAY')

# print("-------WELCOME TO QUIZ APP---------")
# def f(i):
#   print(i)
# def input_something(p):
#    while True:
#     op=input(p).strip().lower()
#     if op:
#        return op
#     print("this cant be blank")
# def add():
#   quizz=[]
#   q=input_something("enter question..")
#   q1=input_something('1..enter option..')
#   q2=input_something('2..enter option..')
#   q3=input_something('3..enter option..')
#   q4=input_something('4..enter option..')
#   global q5
#   q5=(input_something('correct option..'))
#   quizz.append(q)
#   quizz.append(q1)
#   quizz.append(q2)
#   quizz.append(q3)
#   quizz.append(q4)
#   quiz.append(quizz)
#   print('Question added sucessfully')
# def play():
#   if quiz:
#     print("NO QUESTIONS YET")
#   else:
#    for i,j in enumerate():
#     print()
# def delete():
#   if not quiz:
#     print("NO QUESTIONS YET")
#   else:
#     try:
#      s=int(input('enter question number to delete '))-1
#      p=quiz.pop(s)
#      print('QUESTION DELETED SUCCESSFULLY')
#     except Exception as e:
#       print('Invalid Enter Again')
# def listt():
#   if not quiz:
#     print("NO QUESTIONS YET")
#   else:
#     for i,j in enumerate(quiz,start=1):
#      print(i,j)
# quiz=[]
# print("--SELECT--")
# f("--[C]REATE A QUIZ--")
# f('--[L]IST OF ALL QUESTIONS--')
# f('--[P]LAY QUIZ')
# f('--[D]ELETE QUIZ--')
# f('--[E]XIT--')
# while True:
#   a=input('ENTER YOUR CHOICE..').lower().strip()
#   if a=='c':
#    (add())
#   elif a=='l':
#    (listt())
#   elif a=='d':
#     (delete())
#   elif a=='e':
#    print('GOODBYE BUDDY')
#    print('HAVE A MARVELLOUS DAY'
#    break