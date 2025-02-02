from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student data
with open("q-vercel-python.json", "r") as file:
    data = json.load(file)
students = {student["name"]: student["marks"] for student in data}

@app.get("/api")
async def get_marks(name: list[str]):
    marks = [students.get(n, None) for n in name]
    return {"marks": marks}
