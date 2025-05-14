from flask import Flask,jsonify,request,Blueprint
from flask_jwt_extended import jwt_required,get_jwt_identity
from.models import Book,User
from .import db,bcrypt

books_bp=Blueprint("books",__name__,url_prefix="/")

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

#return all books or staffs from the data base 
@books_bp.route('/books' ,methods=['GET'])
def GetAll_Books():
    try:
        book=Book.query.all()
        if not book:
                return jsonify({"Message":"There is no books available"})
        return jsonify([b.to_dict() for b in book])
    except Exception as e:
        return jsonify({"error":"failed to send books to fetch","details":str(e)}),500
#get update the books int the data base  
@books_bp.route('/books/<int:id>',methods=['PUT'])
@jwt_required()
def update(id):
    try:
        current_user= int(get_jwt_identity())
        if not  current_user:
            return jsonify({"message":"Unauthorized: User ID not found in token"}),401
        book = Book.query.get(id)
        if not book:
            return jsonify({"message": f"Book with ID {id} not found"}), 404
        if book.userId != current_user:
             return jsonify({"message":"Unauthorized to update this book"}), 403
        data=request.get_json()
        book.title=data.get('title',book.title)
        book.author=data.get('author',book.author)
        db.session.commit()
        return jsonify({"message":"Books updated succsfully"})
    except Exception as e:
        return jsonify({"maasge":"internal server error","details":str(e)})
    

# add another boks or items in the data base
@books_bp.route('/books/juma',methods=['POST'])
@jwt_required()
def Add_book():
    try:
        print("Reached Add route") 
        current_user_id=int(get_jwt_identity())
        print(f"Current User ID: {current_user_id}")
        if not  current_user_id:
            return jsonify({"message":"Unauthorized: User ID not found in token"}),401
        user = User.query.get(current_user_id)
        if not user:
            return jsonify({"message": "Unauthorized: User does not exist"}), 401
       
        data=request.get_json()
        title=data.get("title",'').strip()
        author=data.get("author",'').strip()
        if not title or not author :
            return jsonify({"message":"Fill in all field"}),422
        book=Book(title=title,author=author ,userId=current_user_id )
        db.session.add(book)
        db.session.commit()
        return jsonify({"message":"book added succesfully"},book.to_dict()),201
    except Exception as d:
        return jsonify({"message":"Internal server error","details":str(d)})
    

#get a specific book for a specific user in the database 
@books_bp.route('/books/<int:id>', methods=['PUT'])
@jwt_required
def get_User_spec_Book(id):
  try:
      urrent_user_id = int(get_jwt_identity())


  except Exception as e:
      return jsonify({"Message":"Internal server error"}),500
 






#this is for deleting a book from the given user 
@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
@jwt_required()
def delete_book(book_id):
    try:
       current_user= int(get_jwt_identity())
       if not  current_user:
            return jsonify({"message":"Unauthorized: User ID not found in token"}),401
       book = Book.query.get(book_id)
       if not book:
            return jsonify({"message": f"Book with ID {book_id} not found"}), 404
       if book.userId != current_user:
           return jsonify({"message":"Unauthorized to delete this book"}), 403
       db.session.delete(book)
       db.session.commit()
       return jsonify({'message':"Books is deleted succesfully"}),201

    except Exception as e:
       return jsonify({"message":"Failed to delete boks","detailes":str(e)})



