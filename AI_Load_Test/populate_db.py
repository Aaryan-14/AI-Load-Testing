# Import SQLite3 for database operations
import sqlite3

# Establish connection to the database file
conn = sqlite3.connect("notes.db")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Insert 200 sample records into the notes table
for i in range(200):
    cursor.execute(
        "INSERT INTO notes (title, description) VALUES (?, ?)",
        (f"Note {i}", "Test data")  # Dynamic title with static description
    )

# Commit the transaction to save changes
conn.commit()

# Close the database connection
conn.close()

# Print success message
print("Database populated successfully")