from fastapi import FastAPI

app = FastAPI(title="Task API")
tasks = []

@app.get("/health")
def health():
    return {"healthy": True}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(title: str):
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    return task
