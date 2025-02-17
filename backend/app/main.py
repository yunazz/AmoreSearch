from fastapi import FastAPI

app = FastAPI()

# 라우터 정의
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

