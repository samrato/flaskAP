from flask import Flask,jsonify,request,Blueprint
from flask_jwt_extended import jwt_required
from.models import Book
from .import db

books_bp=Blueprint("books",__name__,url_prefix="/getbook")

#my simulated database i want to simulate 
# books = [
#     {"id": 1, "title": "Atomic Habits", "author": "James Clear"},
#     {"id": 2, "title": "Deep Work", "author": "Cal Newport"},
#     {"id": 3, "title": "Thong", "author": "Caluka"},
#     {"id": 4, "title": "Burko gurd", "author": "kamau"},
#     {"id": 5, "title": "Starlab", "author": "willington juma"}
# ]
#the entry point of a flask APi consumer routes 
@books_bp.route('/')
def home():
    return jsonify({"message":"Welcome to rest Api"})
#then after home is another one here 
@books_bp.route('/register')
def register():
    return jsonify({"status": "OK", "code": 200})

#return all books or staffs
@books_bp.route('/books' ,methods=['GET'])
def GetAll_Books():
    try:
        book=Book.query.all()
        if not book:
                return jsonify({"Message":"There is no books available"})
        return jsonify([b.to_dict() for b in book])
    except Exception as e:
        return jsonify({"error":"failed to send books to fetch","details":str(e)}),500
#get a book by id s consumers api 
@books_bp.route('/books/<int:id>',methods=['PUT'])
def update(id):
    try:
        data=request.get_json()
        book=Book.query.get_or_404(id)
        book.title=data.get('title',book.title)
        book.author=data.get('author',book.author)
        db.session.commit()
        return jsonify({"message":"Books updated succsfully"})
    except Exception as e:
        return jsonify({"maasge":"internal server error","details":str(e)})
    

# add another boks or items in the data base
@books_bp.route('/books',methods=['POST'])
def Add():
    try:
        data=request.get_json()
        title=data.get("title",'').strip()
        author=data.get("author",'').strip()
        if not title or not author :
            return jsonify({"message":"Fill in all field"}),422
        book=Book(title=title,author=author)
        db.session.add(book)
        db.session.commit()
        return jsonify(book.to_dict()),201
    except Exception as d:
        return jsonify({"message":"Internal server error","details":str(d)})
    

# # 🟠 PUT - Update a book
# @books_bp.route('/books/<int:id>', methods=['PUT'])
# def update_book(id):
#     data = request.get_json()
#     for book in books:
#         if book["id"] == id:
#             book["title"] = data.get("title", book["title"])
#             book["author"] = data.get("author", book["author"])
#             return jsonify(book)
#     return ("Book not found", 404)

# --- Route 5: DELETE a book ---
@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    try:
       data=request.get_json()
       book=Book.query.get_or_404(book_id)
       db.session.delete(book)
       db.session.commit()
       return jsonify({'message':"Books is deleted succesfully"}),201

    except Exception as e:
       return jsonify({"message":"Failed to delete boks","detailes":str(e)})



