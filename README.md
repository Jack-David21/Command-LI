# CLI Authentication System

A secure, modular **command-line authentication and task management system** built using Python.  
This project demonstrates core backend concepts such as user registration, login, password hashing, persistence, per-user data handling, and clean program structure.

---

## Features

### Authentication
- User registration with validation  
- Secure password hashing (SHA-256)  
- Login with limited retry attempts (3)  
- Case-insensitive usernames  
- Hidden password input using `getpass`  

### To-Do Management (Per User)
- Add tasks  
- View tasks  
- Mark tasks as complete / incomplete  
- Edit task titles  
- Delete tasks  
- Tasks persist across sessions  

### System
- Persistent storage using JSON  
- Modular project structure  
- Menu-driven CLI interface  

---

## Project Structure

```
.
├── main.py # Entry point and menu control
├── auth.py # Authentication logic (register & login)
├── to_dos.py # Per-user to-do operations
├── storage.py # Persistence layer (JSON read/write)
├── users.json # User and task data (ignored in GitHub)
└── README.md
```


---

## Concepts Covered

- Authentication fundamentals  
- Password hashing vs plain-text storage  
- Persistence (RAM vs disk)  
- Separation of concerns  
- File handling with JSON  
- Secure input handling  
- Program flow control  
- Modular Python design  
- Per-user data management  

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/Jack-David21/Command-LI.git
```

2. Navigate to the project directory:
```bash
cd Command-LI
```

3. Run the application:
```bash
python main.py
```


## Security Notes
- Passwords are never stored in plain text
- Passwords are hashed using SHA-256
- users.json is excluded from version control via .gitignore
- Password input is hidden using getpass

⚠️ This project is intended for learning purposes and is not production-ready.


## Requirements

- Python 3.8 or higher  
- No external dependencies  


## Future Improvements

- Password salting (bcrypt / argon2)
- Password reset / change functionality
- Improved session handling
- Database integration (SQLite / PostgreSQL)
- Web version using FastAPI
- Unit and integration testing

## Author

Built as a learning project to understand backend fundamentals, authentication workflows, and modular CLI application design.
