# Import the sqlite3 module to work with SQLite databases in Python
import sqlite3

# Step 1: Connect to (or create) the database file named 'students.db'
# If the file doesn't exist, SQLite will create it automatically
conn = sqlite3.connect("students.db")

# Step 2: Create a cursor object
# A cursor allows us to execute SQL commands on the database
cursor = conn.cursor()

# Step 3: Execute SQL command to create a table
# 'IF NOT EXISTS' ensures we do not create the table again if it already exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  # Unique ID for each application (auto-incremented)
    fullName TEXT NOT NULL,                # Student full name (cannot be empty)
    email TEXT NOT NULL,                   # Student email (cannot be empty)
    phone TEXT NOT NULL,                   # Student phone number (cannot be empty)
    course TEXT NOT NULL,                  # The course the student is applying for
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP  # Automatically stores the submission time
)
""")

# Step 4: Commit the changes
# This saves the table creation to the database file
conn.commit()

# Step 5: Close the database connection
# Always close the connection when done to free up resources
conn.close()

# Step 6: Inform the user that the database was created successfully
print("Database created successfully")