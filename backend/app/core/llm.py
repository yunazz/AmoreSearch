import os
import asyncio
import chromadb
import json
import uuid

from tqdm import tqdm
from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_chroma import Chroma

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_MODEL = "gpt-4o"

COLLECTION_NAME = "data"

COLLECTION_NAME_POST = ""
COLLECTION_NAME_COSMETIC = ""
COLLECTION_NAME_LAW = ""
COLLECTION_NAME_BRAND = ""

client = chromadb.HttpClient(host = "3.35.104.197",port = 10090)

embedding_function = OpenAIEmbeddings(
    base_url = "https://76mqtyy2wie64y-10050.proxy.runpod.net/v1",
    model = "multilingual-e5-large",
    api_key="team3",
    tiktoken_enabled=False,
    embedding_ctx_length = 502
)

vector_store = Chroma(
    collection_name=COLLECTION_NAME, 
    embedding_function=embedding_function, 
    client=client
)

retriever = vector_store.as_retriever(search_kwargs={"k": 3})

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="문맥:\n{context}\n\n질문: {question}\n\n답변:"
)

def query_rag_chain(question: str):
    llm = ChatOpenAI(model="gpt-4", openai_api_key=OPENAI_API_KEY, model_kwargs={"stream": True})
        
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt_template}
    )
    
    return qa_chain.run(question)


class AISearch:
    @staticmethod
    async def search(question: str):
        llm = ChatOpenAI(model="gpt-4", openai_api_key=OPENAI_API_KEY, model_kwargs={"stream": True})
        
        async for chunk in llm.astream(question):
            if chunk.content:
                yield chunk.content  
            await asyncio.sleep(0.1)
    

class IntegrationSearch:
    @staticmethod
    async def search(question: str):
        response = query_rag_chain(question)

        for chunk in response.split(" "):  # 🔹 단어 단위 스트리밍 전송
            yield chunk + " "
            await asyncio.sleep(0.1)