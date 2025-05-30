import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to server")

@sio.event
def disconnect():
    print("Disconnected from server")

@sio.on("task_assigned")
def on_task_assigned(data):
    print("\nNew Task Received:")
    print(f"Title: {data['title']}")
    print(f"Description: {data['description']}")
    print(f"Assigned To: {data['assignee']}\n")

if __name__ == "__main__":
    sio.connect("http://localhost:8000")
    sio.wait()  # Keeps the client running
