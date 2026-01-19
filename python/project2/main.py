import streamlit as st
if "quiz" not in st.session_state:
  st.session_state.quiz = []
if "ans" not in st.session_state:
    st.session_state.ans = []
if "check" not in st.session_state:
    st.session_state.check = []
  
st.set_page_config(page_title="Quiz App", page_icon="🧠")
st.title("WELCOME TO QUIZ APP ")
with st.sidebar:
    select=st.radio(label="menu",options=["ADD QUESTIONS","LIST","UPDATE","DELETE","PLAY"])
if select=="ADD QUESTIONS":
 st.session_state.quizz=[]
 q=st.text_input("enter question..").strip()
 q1=st.text_input('1..enter option..').strip()
 q2=st.text_input('2..enter option..').strip()
 q3=st.text_input('3..enter option..').strip()
 q4=st.text_input('4..enter option..').strip()
 q5=st.selectbox(options=[q1,q2,q3,q4],label="CORRECT OPTION",placeholder="select correct option")
 if st.button(label="ADD",key="add"):
  if q and q1 and q2 and q3 and q4:
    st.session_state.quizz.append(q)
    st.session_state.quizz.append(q1)
    st.session_state.quizz.append(q2)
    st.session_state.quizz.append(q3)
    st.session_state.quizz.append(q4)
    st.session_state.quiz.append(st.session_state.quizz)
    st.session_state.ans.append(q5)
    st.success("QUESTION ADDED SUCESSFULLY")
if  select=="LIST":
 if not st.session_state.quiz:
   st.write("NO QUESTIONS SAVED YET")
 else:
   for i,j in enumerate(st.session_state.quiz[0:len(st.session_state.quiz)]):
    st.write("Q..",i+1,j[0],"?")
    st.write("1.",j[1])
    st.write("2.",j[2])
    st.write("3.",j[3])
    st.write("4.",j[4])
if select=="UPDATE":
  st.subheader("UPDATE QUIZ")
  if not  st.session_state.quiz:
    st.write("NO QUESTIONS YET")
  else:
    opt=["QUESTION","OPTION 1","OPTION 2","OPTION 3","OPTION 4"]
    a=st.number_input(min_value=1,max_value=len(st.session_state.quiz),label="enter question number")
    option=st.selectbox(label="select what to change",options=opt)
    a3=st.text_input("enter new option/question ")
    if st.button("UPDATE",key="update"):
      if option==opt[0]:
       st.session_state.quiz[a-1][0]=a3
      if option==opt[1]:
       st.session_state.quiz[a-1][1]=a3
      if option==opt[2]:
       st.session_state.quiz[a-1][2]=a3
      if option==opt[3]:
       st.session_state.quiz[a-1][3]=a3
      if option==opt[4]:
       st.session_state.quiz[a-1][4]=a3
      st.success("UPDATED SUCESSFULLY")
if select=="DELETE":
  st.subheader("DELETE QUIZ")
  if not  st.session_state.quiz:
    st.write("NO QUESTIONS YET")
  else:
   a=st.number_input(min_value=1,max_value=len(st.session_state.quiz),label="enter question number")
   if st.button(label="DELETE OUESTION",key="DELETE"):
     st.session_state.quiz.pop(a-1)
     st.success("QUESTION DELETED SUCESSFULLY")



if select=="PLAY":
  st.subheader("PLAY QUIZ")
  if not  st.session_state.quiz:
    st.write("ADD SOME QUESTIONS TO PLAY ")
  else:
    for i,j in enumerate(st.session_state.quiz):
      pass
      st.session_state.checkk=[]
      st.write(st.session_state.quiz[i][0])
      a=st.radio(label="",options=st.session_state.quiz[i][1:5], key=j )
      st.session_state.checkk.append(a)
      st.session_state.check.append(st.session_state.checkk)
    if st.button(label="SUBMIT",key="play"):
     for n,p in enumerate(st.session_state.check):
      pass
     for y,j in enumerate(st.session_state.ans):
      pass
      score = 0
      if st.session_state.check[n] in st.session_state.ans[y]:
           score+= 1
           st.success("QUIZ COMPLETED")
           st.write("YOUR SCORE IS:", score)
         #  else:
        #   score = 0  
        #   for i in range(len(st.session_state.check)):
        #    if st.session_state.check[i] in  st.session_state.ans[y]:
        #     score += 1
        #   st.success("QUIZ COMPLETED")
        #   st.write("YOUR SCORE IS:", score) 


          































# ---------- Session State ----------
# if "quiz" not in st.session_state:
#     st.session_state.quiz = []   # each question = [q, o1, o2, o3, o4]
# if "ans" not in st.session_state:
#     st.session_state.ans = []    # correct answers


# ---------- Sidebar Menu ----------
# menu = st.sidebar.radio(
#     " MENU",
#     [" Add Quiz", "▶Play Quiz", "List Questions", "Update Question", " Delete Question"]
# )``

# # ---------- ADD QUIZ ----------
# if menu == "Add Quiz":
#     st.subheader(" Add a New Question")

#     q = st.text_input("Enter Question")
#     o1 = st.text_input("Option 1")
#     o2 = st.text_input("Option 2")
#     o3 = st.text_input("Option 3")
#     o4 = st.text_input("Option 4")

#     correct = st.selectbox("Select Correct Option", [o1, o2, o3, o4])

#     if st.button("Add Question"):
#         if q and o1 and o2 and o3 and o4:
#             st.session_state.quiz.append([q, o1, o2, o3, o4])
#             st.session_state.ans.append(correct)
#             st.success(" Question added successfully")
#         else:
#             st.error(" All fields are required")


# # ---------- PLAY QUIZ ----------
# elif menu == "▶Play Quiz":
#     st.subheader("▶Play Quiz")

#     if not st.session_state.quiz:
#         st.warning(" No questions yet")
#     else:
#         for i, q in enumerate(st.session_state.quiz):
#             st.markdown(f"**Q{i+1}. {q[0]}**")
#             user_ans = st.radio(
#                 "Choose an option:",
#                 q[1:],
#                 key=f"radio_{i}"
#             )

#             if st.button(f"Submit Answer {i+1}"):
#                 if user_ans == st.session_state.ans[i]:
#                     st.success(" GOOD BACHA ")
#                 else:
#                     st.error("❌ Wrong Answer")

  
# # ---------- LIST QUESTIONS ----------
# elif menu == "List Questions":
#     st.subheader(" All Questions")

#     if not st.session_state.quiz:
#         st.warning(" No questions yet")
#     else:
#         for i, q in enumerate(st.session_state.quiz, start=1):
#             st.write(f"**{i}. {q[0]}**")
#             st.write("Options:", q[1:])


# # ---------- UPDATE QUESTION ----------
# elif menu == " Update Question":
#     st.subheader("Update Question")

#     if not st.session_state.quiz:
#         st.warning(" No questions yet")
#     else:
#         q_no = st.number_input(
#             "Enter Question Number",
#             min_value=1,
#             max_value=len(st.session_state.quiz)
#         ) - 1

#         choice = st.selectbox(
#             "What do you want to change?",
#             ["Question", "Option 1", "Option 2", "Option 3", "Option 4"]
#         )

#         new_text = st.text_input("Enter New Text")

#         if st.button("Update"):
#             index = {"Question": 0, "Option 1": 1, "Option 2": 2, "Option 3": 3, "Option 4": 4}
#             st.session_state.quiz[q_no][index[choice]] = new_text
#             st.success(" Change Done")


# # ---------- DELETE QUESTION ----------
# elif menu == "🗑️ Delete Question":
#     st.subheader("🗑️ Delete Question")

#     if not st.session_state.quiz:
#         st.warning(" No questions yet")
#     else:
#         q_no = st.number_input(
#             "Enter Question Number to Delete",
#             min_value=1,
#             max_value=len(st.session_state.quiz)
#         ) - 1

#         if st.button("Delete"):
#             st.session_state.quiz.pop(q_no)
#             st.session_state.ans.pop(q_no)
#             st.success(" Question Deleted Successfully")


