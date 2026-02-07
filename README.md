# CLI Authentication System

A secure, modular **command-line authentication system** built using Python.  
This project demonstrates core backend concepts such as user registration, login, password hashing, persistence, and clean program structure.


## Features

- User registration with validation  
- Secure password hashing (SHA-256)  
- Login with limited retry attempts  
- Persistent storage using JSON  
- Hidden password input using `getpass`  
- Modular project structure  
- Menu-driven CLI interface  



## Project Structure

```
.
├── main.py        # Entry point and menu control
├── auth.py        # Authentication logic (register & login)
├── storage.py     # Persistence layer (JSON read/write)
├── users.json     # User data (ignored in GitHub)
└── README.md
```


## Concepts Covered

- Authentication fundamentals  
- Password hashing vs plain-text storage  
- Persistence (RAM vs disk)  
- Separation of concerns  
- File handling with JSON  
- Secure input handling  
- Program flow control  
- Modular Python design  


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

- Passwords are **never stored in plain text**
- Passwords are hashed using **SHA-256**
- `users.json` is excluded from version control via `.gitignore`
- Password input is hidden using `getpass`

> ⚠️ This project is intended for learning purposes and is not production-ready.


## Requirements

- Python 3.8 or higher  
- No external dependencies  


## Future Improvements

- Logout and session handling  
- Per-user features (e.g. to-do lists)  
- Password reset / change functionality  
- Database integration  
- Web version using FastAPI  
- Unit testing  


## Author

Built as a learning project to understand backend fundamentals and authentication workflows.
