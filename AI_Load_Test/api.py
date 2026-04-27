# Import required modules from Flask
from flask import Flask, request, jsonify

# Import Helper class for database operations
from helper import Helper

# Initialize Flask application
app = Flask(__name__)

# Create database helper object
db = Helper()

# Create table when application starts
db.create_table()


# Home route to check if API is running
@app.route("/")
def home():
    return jsonify({"message": "API is running"})


# Route to fetch all notes (READ operation)
@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(db.get_notes())


# Route to create a new note (CREATE operation)
@app.route("/notes", methods=["POST"])
def create_note():
    # Get JSON data from request body
    data = request.get_json()

    # Validate input: title is required
    if not data or "title" not in data:
        return jsonify({"error": "Title required"}), 400

    # Insert note into database
    note_id = db.post_notes(
        data["title"],
        data.get("description", "")
    )

    # Return success response with created note ID
    return jsonify({
        "message": "Note created",
        "id": note_id
    }), 201


# Route to fetch a single note by ID (READ operation)
@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    note = db.get_note(note_id)

    # Check if note exists
    if note:
        return jsonify(note)

    # Return error if not found
    return jsonify({"error": "Not found"}), 404


# Route to update an existing note (UPDATE operation)
@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    # Get JSON data from request
    data = request.get_json()

    # Update note in database
    db.update_note(
        note_id,
        data.get("title"),
        data.get("description")
    )

    # Return success message
    return jsonify({"message": "Updated"})


# Route to delete a note (DELETE operation)
@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    # Delete note from database
    db.delete_note(note_id)

    # Return success message
    return jsonify({"message": "Deleted"})


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=8005)