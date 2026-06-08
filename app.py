# # # this is what is open ai paid version and u need to pay for it

# # streamlit run app.py se chalega



from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPEN_API_KEY"] = os.getenv("OPEN_API_KEY")

# Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system ", "You are a helpful assistant. Please response to the user queries")
        (("user", "Question:(question)"))
    ]
)



# streamlit framework
st.title('Langchain Demo With OPEN API')
input_text = st.text_input("Search the topic u want")

# openai llm

llm = ChatOpenAI(model ="gpt-3.5-turbo")
output_parsor = StrOutputParser()
chain = prompt|llm|output_parsor

if input_text:
    st.write(chain.invoke({'question':input_text}))




# this is what is open ai paid version and u need to pay for it





