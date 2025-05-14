from.import db

class Book(db.Model):
    bookId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), nullable=False)#the refernce from the user
    def to_dict(self):
          return {"bookId":self.bookId,"title":self.title,"author":self.author,"userId": self.userId}

class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)  
    password = db.Column(db.String(128), nullable=False)  
    def to_dict(self):
           return{"userId":self.userId,"username":self.username,"email":self.email,"password":self.password}    