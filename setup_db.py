from app import app, db  # Importing app and db from app.py

with app.app_context():  # Activate application context
    db.create_all()  # Create tables in the database
    print("Database tables created successfully!")