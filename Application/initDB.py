from main import db, app, Movie, Cast, Crew
import csv, ast

db.drop_all()
db.create_all(app=app)

# replace any null values with None to avoid db errors
def noNull(val):
    if str(val) == "":
        return None
    return val

'''
#Cast & Crew
with open('./Application/tmdb_5000_credits.csv', 'r') as credits:
    reader = csv.DictReader(credits)

    for line in reader:
        cast = ast.literal_eval(line['cast'])
        crew = ast.literal_eval(line['crew'])

        for member in cast: #Cast
            #member['name'] //Real Name
            #member['id']
            #member['cast_id']
            #member['character']
            #member['gender']

            db.session.add(
                Cast(
                    #id=noNull(member['id']),
                    cast_id=noNull(member['cast_id']),
                    credit_id=noNull(member['credit_id']),
                    name=noNull(member['name']),
                    character=noNull(member['character']),

                    movie_id=noNull(line['movie_id'])
                )
            )
        
        #db.session.commit() #save

        for member in crew: #Crew
            #member['name'] //Real Name
            #member['id']
            #member['credit_id']
            #member['department']
            #member['job']

            db.session.add(
                Crew(
                    #id=noNull(member['id']),
                    credit_id=noNull(member['credit_id']),
                    name=noNull(member['name']),
                    department=noNull(member['department']),
                    job=noNull(member['job']),

                    movie_id=noNull(line['movie_id'])
                )
            )
            
db.session.commit() #save
castList = Cast.query.limit(10)
crewList = Crew.query.limit(10)
print(castList[5].name)
print(crewList[5].name)
'''

#'''
#Movies
movies = []
i = 0
with open('./Application/API/movies_metadata.csv', 'r', encoding="utf8") as movie:
    reader = csv.DictReader(movie)

    for line in reader:
        movies.append(
            {
                'title':line['title'],
                'lang':line['original_language'],
                'genres':"",
                'poster':"",
                'overview':line['overview'],
                'release_date':line['release_date'],

                'imdb_id':line['imdb_id']
            }
        )
        i = i+1
        if i == 5000:
            break

i = 0
with open('./Application/API/MovieGenre.csv', 'r') as movieStuff:
    reader = csv.DictReader(movieStuff)

    for line in reader:
        for movie in movies:
            if int(line['imdbId']) == int(movie['imdb_id']):
                movie['poster'] = line['Poster']
                movie['genres'] = line['Genre']
    
        i = i+1
        if i == 5000:
            break


print(movies[0])

#db.session.commit() #save

#movieList = Movie.query.limit(10)
#print(movieList[5].title)
#'''
