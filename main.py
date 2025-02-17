from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/notes/")
async def get_notes():
    return {"data": [{
        "id": 1, "text": "Первая заметка",
        "id": 2, "text": "Вторая заметка",
        "id": 3, "text": "Третья заметка",
        }]}
