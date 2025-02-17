# Flask TODO App

This is a simple Flask-based TODO application with CRUD functionality using SQLite.

## Features
- 📌 Add, update, and delete tasks
- 📌 Uses Flask and SQLAlchemy
- 📌 SQLite as the database
- 📌 Simple and clean UI with HTML templates

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/flask-todo-app.git
   cd flask-todo-app
   ```

2. Install dependencies:
   ```sh
   pip install flask flask_sqlalchemy
   ```

3. Setup the database:
   ```sh
   python setup_db.py
   ```

4. Run the application:
   ```sh
   python app.py
   ```

5. Open your browser and go to:
   ```sh
   http://127.0.0.1:5000/
   ```

## File Structure
```
flask-todo-app/
│── app.py         # Main Flask application
│── setup_db.py    # Database setup script
│── templates/
│   ├── index.html  # Home page template
│   ├── update.html # Update page template
│── static/        # CSS, JS, and images
│── todo.db        # SQLite database file (auto-created)
│── README.md      # Project documentation
```

## API Routes
| Route              | Method | Description |
|--------------------|--------|-------------|
| `/`               | GET/POST | Home page, display and add tasks |
| `/update/<SNO>`   | GET/POST | Update a task |
| `/delete/<SNO>`   | GET     | Delete a task |

## Contributing
Feel free to fork the repository and submit pull requests with improvements.

## License
This project is licensed under the MIT License.

---
Happy coding! 🚀
