from flask import Flask,jsonify,request
app=Flask(__name__)

#my simulated database i want to simulate 
books = [
    {"id": 1, "title": "Atomic Habits", "author": "James Clear"},
    {"id": 2, "title": "Deep Work", "author": "Cal Newport"},
    {"id": 3, "title": "Thong", "author": "Caluka"},
    {"id": 4, "title": "Burko gurd", "author": "kamau"},
    {"id": 5, "title": "Starlab", "author": "willington juma"}
]
#the entry point of a flask APi consumer routes 
@app.route('/')
def home():
    return jsonify({"message":"Welcome to rest Api"})
#then after home is another one here 
@app.route('/register')
def register():
    return jsonify({"status": "OK", "code": 200})

#return all books or staffs
@app.route('/books' ,methods=['GET'])
def GetAll():
    return jsonify(books)

#get a book by id s consumers api 
@app.route('/books/<int:id>',methods=['GET'])
def GetID(id):
    for book in books:
        if book['id']==id:
               return jsonify(book)
    return jsonify({"message":"Books is not found"})

# add another boks or items in the data base
@app.route('/books',methods=['POST'])
def Add():
    data=request.get_json()
    book_to_add = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }
    books.append(book_to_add)
    # Return the new book with "created" status
    return jsonify(book_to_add), 200


# 🟠 PUT - Update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    for book in books:
        if book["id"] == id:
            book["title"] = data.get("title", book["title"])
            book["author"] = data.get("author", book["author"])
            return jsonify(book)
    return ("Book not found", 404)

# --- Route 5: DELETE a book ---
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """Remove a book from our collection"""
    # Find the book index
    for i, book in enumerate(books):
        if book["id"] == book_id:
            # Remove it and return success
            deleted_book = books.pop(i)
            return jsonify(deleted_book)
    # If book doesn't exist
    return jsonify({"error": "Book not found"}), 404









if __name__=="__main__":
    app.run(debug=True  )