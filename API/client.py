import requests
import streamlit as st


# def openai_response(input_text):
#     reponse = requests.post("http://localhost:8000/essay/invoke",
#     json={'input':{'topic:input_text'}})


#     return reponse.json()['output']['content']



def ollama_response(input_text1):
    response =requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text1}})
    # print(response.json())
    return response.json()['output']


st.title('Langchain demo with llama api')
# input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")



# if input_text:
#     st.write(openai_response(input_text))


if input_text1:
    st.write(ollama_response(input_text1))

