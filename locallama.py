# streamlit run locallama.py
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

import streamlit as st

from dotenv import load_dotenv
import os



# load krna bhai humesha .env file wrna access kasie milega mai bhul jata hu
load_dotenv() 


# Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# PROMPT TEMPLATE
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        # (("user","Question:(question)"))
        ("human", "{question}")
    ]
)



# streamlit framework
st.title('Langchain Demo With llama2')
input_text = st.text_input("Search the topic u want")

# openai llm

llm = OllamaLLM(model ="llama3.1")
output_parsor = StrOutputParser()
chain = prompt|llm|output_parsor

if input_text:
    st.write(chain.invoke({'question':input_text}))



