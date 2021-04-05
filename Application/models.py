from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)

    def toDict(self):
        return{
            "user_id":self.user_id,
            "username":self.username,
            "password":self.password
                    }

    def add_password(self,password):
        self.password = generate_password_hash(password, method='sha256')

    def verify_password():
        return check_password_hash(self.password, password)

class SavedMovie(db.Model):
    list_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"))
    rating = db.Column(db.Integer, nullable = False)

    def toDict(self):
        return{
            "list_id":self.list_id,
            "user_id":self.user_id,
            "movie_id":self.movie_id,
            "rating":self.rating
                    }

class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key = True)
    movie_name = db.Column(db.String(120), nullable = False)
    cast_id = db.Column(db.Integer, db.ForeignKey("cast.cast_id"))
    crew_id = db.Column(db.Integer, db.ForeignKey("crew.crew_name"))
    release_date = db.Column(db.Integer, nullable = False)

    def toDict(self):
        return{
            "movie_id":self.movie_id,
            "movie_name":self.movie_name,
            "cast_id":self.cast_id,
            "crew_id":self.crew_id,
            "release_date":self.release_date
                }

class Cast(db.Model):
    cast_id = db.Column(db.Integer, primary_key = True)
    cast_name = db.Column(db.String(120))

    def toDict(self):
        return{
            "cast_id":self.cast_id,
            "cast_name":self.cast_name
                }

class Crew(db.Model):
    crew_id  = db.Column(db.Integer, primary_key = True)
    crew_name = db.Column(db.String(120))

    def toDict(self):
        return{
            "crew_id":self.crew_id,
            "crew_name":self.crew_name
                }
