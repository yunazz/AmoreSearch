# 💄AmoreSearch

AmoreSearch는 sLLM을 기반으로 아모레퍼시픽에서 사용할 수 있는 <b>사내 검색 시스템</b>으로 핵심 목표는 <b>sLLM</b>을 개발하고 <b>파인튜닝</b>하여 최적화된 검색 경험을 제공하는 것입니다.

<!-- [🔗 AmoreSearch 웹서비스](http://15.165.170.3) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [📽️ 시연 영상]() -->

<br/>

## 1. 프로젝트 개요
### 📅 작업 기간
2025.01.21 ~ 2025.03.20 

<br/>

### 🛠️ 기술스텍
- **프론트엔드**: `Nuxt.js` → NuxtImg, Vuetify ···
- **백엔드**: `FastAPI` → Langchain, Chromadb, PyMySQL, Pydantic, PyJWT ···
- **데이터베이스**: `MariaDB`, `ChromaDB`
- **LLM, Embedding 모델**: `RunPod`  → llm - Qwen2.5-72B-Instruct / 임베딩 - multilingual-e5-large
- **서버 인프라**: `AWS EC2`, `S3`

<br/>

## 2. 프로젝트 소개
### 🚀 주요 기능
- AI 검색
- 회사소식, 사내문서 조회 및 검색
- 화장품 조회 및 검색
- 직원관리
- 업계 최신뉴스 및 저널 모아보기 

<br/>

### 🏰️ 시스템 아키텍처 구조 
<img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN06-FINAL-3Team/blob/main/images/%5BAmoreSearch%5D%20%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98.png"/>
- CI/CD: Github Actions
- EC2 인스턴스 1: 프론트엔드(Nuxt.js), 백엔드(FastAPI), MariaDB 배포
- EC2 인스턴스 2: 벡터 스토어(ChromaDB) 배포 및 관리
- LLM, Embedding 모델: RunPod에서 실행하여 검색 성능 최적화
- AWS S3: 데이터 저장 및 관리

<br/>

### 📱 UI
<p><img src="./images/login.gif" width="50%"/><img src="./images/search.gif" width="50%"/></p>
<p><img src="./images/amorestory.gif" width="50%"/><img src="./images/news.gif" width="50%"/></p>
<p><img src="./images/cosmetic.gif" width="50%"/><img src="./images/favorite.gif" width="50%"/></p>
<p><img src="./images/mypage.gif" width="50%"/><img src="./images/member.gif" width="50%"/></p>

<br/>

### 💾 데이터베이스
- MariaDB
- ChromaDB
- AWS S3 

<br/>

### 🪛  sLLM 모델링 과정에서 했던 실험
- **Embedding 모델 성능 평가** 
    - bge-m3
    - multilingual-e5-large (✅)
- **HyQE**
- **HyQE 질문을 위한 sLLM 모델 미세조정**

### 📌 이번 프로젝트를 마치며 새롭게 알게된 부분
- CI/CD
- Vuetify3
- Fast Api
- Fine Tuning
- Tool Calling 
https://python.langchain.com/docs/concepts/tool_calling/

<br/>

LangChain을 활용한 Tool Calling 으로 Agentic 하게 구현하고자 함
- query에 따른 각 collection 선택 후 retrieve
- Cosin Similarity를 통한 HyQE 질문을 활용한 답변 ReRank
- ReRank를 통해 관련된 질문 4개 추출
