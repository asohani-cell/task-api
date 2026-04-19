from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: str):
    tasks.append(task)
    return {"message": "Task added"}
