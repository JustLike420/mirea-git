from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/notes/")
async def get_notes():
    return {"data": [
        {"id": 1, "text": "Первая заметка"},
        {"id": 2, "text": "Вторая заметка"},
        {"id": 3, "text": "Третья заметка"},
        ]}

@app.get("/notes/{note_id}")
async def get_note_by_id(note_id: int):
    data = {
        1: "Первая заметка",
        2: "Вторая заметка",
        3: "Третья заметка",
        }
    if note_id not in data.keys():
        return {}
    
    return {"data": {
        "id": note_id, "text": data[note_id]
        }}
