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









if __name__=="__main__":
    app.run(debug=True  )