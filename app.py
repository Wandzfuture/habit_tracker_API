from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


# Database setup
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Initialize the database
init_db()


@app.route('/bookmarks', methods=['POST'])
def add_bookmark():
    data = request.get_json()
    title = data['title']
    url = data['url']
    category = data['category']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    query = """
    INSERT INTO bookmarks (title, url, category)
    VALUES (?, ?, ?)
    """
    c.execute(query, (title, url, category))
    conn.commit()
    conn.close()

    return jsonify({"message": "Bookmark added!"}), 201


@app.route('/bookmarks', methods=['GET'])
def get_bookmarks():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bookmarks")
    bookmarks = c.fetchall()
    conn.close()

    return jsonify(bookmarks)


@app.route('/bookmarks/<int:id>', methods=['DELETE'])
def delete_bookmark(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM bookmarks WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Bookmark deleted!"})


if __name__ == '__main__':
    app.run(debug=True)
