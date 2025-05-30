from fastapi import FastAPI
import socketio
from .models import Task
from .email_utils import send_email_notification

# Setup socket.io
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = FastAPI()
socket_app = socketio.ASGIApp(sio, other_asgi_app=app)

@sio.event
async def connect(sid, environ):
    print("Client connected:", sid)

@sio.event
async def disconnect(sid):
    print("Client disconnected:", sid)

@app.post("/assign-task")
async def assign_task(task: Task):
    await sio.emit("task_assigned", {
        "title": task.title,
        "description": task.description,
        "assignee": task.assignee_email
    })
    send_email_notification(
        to_email=task.assignee_email,
        subject="New Task Assigned",
        body=f"Task Title: {task.title}\n\n{task.description}"
    )
    return {"message": "Task assigned"}
