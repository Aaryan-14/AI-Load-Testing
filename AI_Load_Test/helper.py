# Import SQLite3 for database operations
import sqlite3

# Database file name
DB_NAME = "notes.db"


# Helper class to manage all database interactions
class Helper:

    # Private method to establish a database connection
    def _connect(self):
        conn = sqlite3.connect(DB_NAME, timeout=10)
        
        # Enable dictionary-like access for rows
        conn.row_factory = sqlite3.Row
        
        return conn

    # Create notes table if it does not already exist
    def create_table(self):
        conn = self._connect()
        
        conn.execute("""
        CREATE TABLE IF NOT EXISTS notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        conn.commit()
        conn.close()

    # Fetch all notes from database
    def get_notes(self):
        conn = self._connect()
        
        # Execute query and fetch all rows
        notes = conn.execute("SELECT * FROM notes").fetchall()
        
        conn.close()
        
        # Convert each row to dictionary format
        return [dict(n) for n in notes]

    # Insert a new note into the database
    def post_notes(self, title, description):
        conn = self._connect()
        cursor = conn.cursor()
        
        # Parameterized query to prevent SQL injection
        cursor.execute(
            "INSERT INTO notes (title, description) VALUES (?, ?)",
            (title, description)
        )
        
        conn.commit()
        
        # Get the ID of the newly inserted note
        note_id = cursor.lastrowid
        
        conn.close()
        
        return note_id

    # Fetch a single note by ID
    def get_note(self, note_id):
        conn = self._connect()
        
        note = conn.execute(
            "SELECT * FROM notes WHERE id=?",
            (note_id,)
        ).fetchone()
        
        conn.close()
        
        # Return dictionary if found, otherwise None
        return dict(note) if note else None

    # Update an existing note
    def update_note(self, note_id, title, description):
        conn = self._connect()
        
        conn.execute(
            "UPDATE notes SET title=?, description=? WHERE id=?",
            (title, description, note_id)
        )
        
        conn.commit()
        conn.close()

    # Delete a note by ID
    def delete_note(self, note_id):
        conn = self._connect()
        
        conn.execute(
            "DELETE FROM notes WHERE id=?",
            (note_id,)
        )
        
        conn.commit()
        conn.close()