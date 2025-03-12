import os

from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# COLLECTION_NAME = ""

LLM_MODEL = "gpt-4o"

class AISearch:
    def __init__(self):
        
        self.llm = ChatOpenAI(model=LLM_MODEL, openai_api_key=OPENAI_API_KEY)
        

    def search(self, input_text):
        response = self.llm.invoke(input_text)  
        
        return response 