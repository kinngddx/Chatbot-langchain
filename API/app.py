from fastapi import FastAPI

from langchain_core.prompts  import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
# from langchain_community.llms import ollama
from langchain_ollama import OllamaLLM
# from langchain_core.prompts.base import BasePromptTemplate


from dotenv import load_dotenv

load_dotenv()

# os.environ['OPEN_API_KEY'] = os.getenv("OPEN_API_KEY")



app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)


# adding routes
# add_routes(
#     app,
#     ChatOpenAI(),
#     path = "/openai"
# )

# model = ChatOpenAI()

##ollama llama 2

llm = OllamaLLM(model="llama3.1")



# prompt 1 for chatgpt and prompt 2 for free lllama
# prompt1 =ChatPromptTemplate("write me a essay about a {topic} with 200 words")
prompt2 =ChatPromptTemplate.from_template("write me a poem about a {topic} with 200 words")


# add_routes(
#     app,
#     prompt1|model,
#     path = "/essay"
# )

# routes added for lllamam
add_routes(
    app,
    # prompt2|model,
    prompt2|llm,
    path = "/poem"
)



if __name__=="__main__":
    uvicorn.run(app,host = "localhost",port=8000)
