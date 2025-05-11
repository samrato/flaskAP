from flask import Flask,jsonify
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



if __name__=="__main__":
    app.run(debug=True  )