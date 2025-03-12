import os
# import chromadb

from langchain_openai import ChatOpenAI
# from langchain.chains import create_retrieval_chain
# from langchain.vectorstores import Chroma
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain.chains import create_history_aware_retriever
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# PERSIST_DIRECTORY = os.path.abspath(os.path.join())
# COLLECTION_NAME = ""

LLM_MODEL = "gpt-4o"

# EMBEDDING_MODEL = "text-embedding-3-small"
# SESSION_ID = ""  

# store = {}

# client = chromadb.HttpClient(
#     host = "3.35.104.197",
#     port = 10090,
# )

# chroma = Chroma(
#                 collection_name="HyQE", 
#                 embedding_function=embedding_function, 
#                 client=client
#             )

class AISearch:
    def __init__(self):
        
        self.llm = ChatOpenAI(model=LLM_MODEL, openai_api_key=OPENAI_API_KEY)
        
        # embedding_model = OpenAIEmbeddings(model=EMBEDDING_MODEL, openai_api_key=OPENAI_API_KEY)
        
        # vector_store = Chroma(
        #     persist_directory=PERSIST_DIRECTORY,
        #     collection_name=COLLECTION_NAME,
        #     embedding_function=embedding_model,
        # )

        # retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})

        # contextualize_q_system_prompt = (
        #    
        # )

        # contextualize_q_prompt = ChatPromptTemplate.from_messages(
        #     [
        #         ("system", contextualize_q_system_prompt),
        #         MessagesPlaceholder("chat_history"),
        #         ("human", "{input}"),
        #     ]
        # )

        # history_aware_retriever = create_history_aware_retriever(
        #     llm, retriever, contextualize_q_prompt
        # )

        # system_prompt = """
        #  
        #     """

        # qa_prompt = ChatPromptTemplate.from_messages(
        #     [
        #         ("system", system_prompt),
        #         MessagesPlaceholder("chat_history"),
        #         ("human", "{input}"),
        #     ]
        # )

        # qa_chain = create_stuff_documents_chain(llm, qa_prompt)
        
        # rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)
        
        # self.chain = rag_chain
        
        

    def search(self, input_text):
        response = self.llm.invoke(input_text)  
        
        return response 