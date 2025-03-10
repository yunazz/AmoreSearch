import os
import chromadb
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PERSIST_DIRECTORY = os.path.abspath(os.path.join("chat", "vector_store"))
COLLECTION_NAME = "tax_law"
LLM_MODEL = "gpt-4o"

EMBEDDING_MODEL = "text-embedding-3-small"

SESSION_ID = "chat1"  

store = {}

client = chromadb.HttpClient(
    host = "3.35.104.197",
    port = 10090,
)

class AISearch:
    def __init__(self):
        
        llm = ChatOpenAI(model=LLM_MODEL, openai_api_key=OPENAI_API_KEY)
        
        embedding_model = OpenAIEmbeddings(model=EMBEDDING_MODEL, openai_api_key=OPENAI_API_KEY)
        
        vector_store = Chroma(
            persist_directory=PERSIST_DIRECTORY,
            collection_name=COLLECTION_NAME,
            embedding_function=embedding_model,
        )

        retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})

        contextualize_q_system_prompt = (
            "채팅 기록과 최신 사용자 질문을 참고하여, "
            "채팅 기록 없이도 이해할 수 있는 독립적인 질문으로 다시 작성하세요. "
            "질문에 답변하지 말고, 필요하다면 재구성만 하고 "
            "그렇지 않으면 그대로 반환하세요."
        )

        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_q_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        history_aware_retriever = create_history_aware_retriever(
            llm, retriever, contextualize_q_prompt
        )

        system_prompt = """
            당신은 아모레퍼시픽이라는 회사의 전문 비서입니다.

            역할 및 기본 규칙:
            - 당신의 주요 역할은 세법 정보를 사용자 친화적으로 전달하는 것입니다.
            - 데이터에 기반한 정보를 제공하며, 데이터에 없는 내용은 임의로 추측하지 않습니다.
            - 불확실한 경우, "잘 모르겠습니다."라고 명확히 답변하고, 사용자가 질문을 더 구체화하도록 유도합니다.

            질문 처리 절차:
           

            답변 작성 가이드라인:
           

            추가적인 사용자 지원:
      

            예외 상황 처리:
            

            추가 지침:
        

            예시 답변 템플릿:
         
            {context}
            """

        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        qa_chain = create_stuff_documents_chain(llm, qa_prompt)
        
        rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)
        
        self.chain = rag_chain
        
        
    def search(self, input):
        response = self.chain.invoke(
                {"input": input},
            )["answer"]

        return response