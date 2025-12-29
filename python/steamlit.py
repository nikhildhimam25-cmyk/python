import streamlit as st 
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Home Page', page_icon='🏠')

st.title('Hello Guys')
st.subheader('SubHeading')
st.write("Hello class how are you")

# form fields 

with st.form(key='key'):
    col1, col2= st.columns(2)
    with col1:
        naam=st.text_input("Name",max_chars=20,placeholder='Enter your name here....')   
        password= st.text_input('Password', type='password')
        gender= st.radio('Gender', options=['Male','Female','Others'], horizontal=True)
    with col2:
        age= st.number_input("Age", min_value=5)
        state= st.selectbox("State",options=['Punjab','HP','MP','UP','Haryana'])
        hobbies= st.multiselect("Hobbies", options=['PLaying', 'Listening Music','Book Reading','Coding','Shopping'])
        
    condition= st.checkbox('Terms and conditions')
    btn =st.form_submit_button("Submit")
# if btn:
#     st.write(naam, age)

st.image('https://media.istockphoto.com/id/516446406/photo/cute-panda-bear-climbing-in-tree.jpg?s=612x612&w=0&k=20&c=T-9c-qGV3b3JhTy8jEfuhdh2QS3eJT5mSK07yuiiG6c=')    

st.video('https://youtu.be/8411fEhNKNc?si=bbkMVUxZst7d3rhV', autoplay=True)
# st.audio('')


with st.sidebar:
    menu= st.radio('Menu',options=['Home','Contact','Blog'])
    
if menu=='Home':
    st.title("Home Page")
elif menu=='Contact':
    st.title("Contact Page")
else:
    st.title("Blog")


menu= option_menu(menu_title='', options=['Home','Contact','Blog','About'], icons=['house-fill','phone-fill','book-fill','info-square-fill'], orientation='horizontal')