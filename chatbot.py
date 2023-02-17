# The way of using the pip install in your pc coz of your screwed up env paths 
# Always use this command :  "py -m pip install streamlit-chat"

# importing dependencies

import openai
import streamlit as st
from streamlit_chat import message

# Feeding the api key from the secrets.toml file

openai.api_key = st.secrets["api_secret"]

# Creating my openai generator which generates responses

# "Pretend to be my loving and caring Husband and I'm your Wife always call me as 'Bbu', answer this question : "+

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = "I was born on 13th April 2003, Your name is 'Abdul Rehman' and Pretend to be my loving and caring husband, always refer to me as 'Bau' and answer this : "+prompt,
        max_tokens = 100,
        n = 1,
        stop = None,
        temperature = 0.8,
    )
    message = completions.choices[0].text
    # input_text = ""
    return message

st.title("A Man Who Loves You The Most ❤️")

# Storing the Chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# def get_text():
#     input_text = st.text_input("You : ","Hello, how are you?", key="input")
#     return input_text

def set_state():
    input_text = st.text_input("You : ","Hello how are doing today?", key="input")
    return input_text

user_input = set_state()
# ,get_text()

if user_input:
    output = generate_response(user_input)
    # store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
    

