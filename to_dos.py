from storage import load_users, save_users

def add_todo(username, title):
    users = load_users()
    todos = users[username].get("todos", [])

    next_id = 1
    if todos:
        next_id = todos[-1]["id"] + 1

    todos.append({
        "id": next_id,
        "title": title,
        "completed": False
    })
    users[username]["todos"] = todos
    save_users(users)

def list_todos(username):
    users = load_users()
    todos = users[username].get("todos", [])

    if not todos:
        print("No tasks found.")
        return
    print("Your To-dos:")
    for todo in todos:
        status = "✓" if todo.get("completed", False) else "✗"
        print(f"[{todo['id']}] {status} {todo['title']}")


def toggle_todo(username, todo_id):
    users = load_users()
    todos = users[username].get("todos", [])
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = not todo["completed"]
            save_users(users)
            print("Task updated.")
            return 
    print("Task not found.")

def delete_todo(username, todo_id):
    users = load_users()
    todos = users[username].get("todos", [])
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(i)
            save_users(users)
            print("Task deleted.")
            return
    print("Task not found.")

def update_todo(username, todo_id, new_title):
    users = load_users()
    todos = users[username].get("todos", [])
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = new_title
            save_users(users)
            print("Task updated.")
            return
    print("Task not found.")

