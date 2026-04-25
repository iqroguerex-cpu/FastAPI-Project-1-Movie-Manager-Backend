from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MOVIES = [
    {"title": "Inception", "director": "Christopher Nolan", "genre": "sci-fi", "rating": 9},
    {"title": "Interstellar", "director": "Christopher Nolan", "genre": "sci-fi", "rating": 9},
    {"title": "The Dark Knight", "director": "Christopher Nolan", "genre": "action", "rating": 9},
    {"title": "Avengers", "director": "Joss Whedon", "genre": "action", "rating": 8},
    {"title": "Titanic", "director": "James Cameron", "genre": "romance", "rating": 8}
]


@app.get("/")
async def root():
    return {"message": "Movie Manager API Running"}


@app.get("/movies")
async def display_movies():
    return MOVIES


@app.get("/movies/{movie_title}")
async def read_movie_by_movie_title(movie_title: str):
    for movie in MOVIES:
        if movie.get("title").casefold() == movie_title.casefold():
            return movie
    return {"message": "Movie does not exist"}


@app.get("/movies/")
async def movie_by_genre(genre: str):
    movies_by_genre = []
    for movie in MOVIES:
        if movie.get("genre").casefold() == genre.casefold():
            movies_by_genre.append(movie)
    return movies_by_genre


@app.get("/movies/{director}/")
async def movies_by_director_genre(director: str, genre: str):
    result = []
    for movie in MOVIES:
        if (
            movie.get("director").casefold() == director.casefold()
            and movie.get("genre").casefold() == genre.casefold()
        ):
            result.append(movie)
    return result


@app.post("/movies/create_movie")
async def add_movies(create_movie=Body()):
    MOVIES.append(create_movie)
    return {"message": "Movie added successfully"}


@app.put("/movies/update_movie")
async def update_movies(update_movie=Body()):
    for i in range(len(MOVIES)):
        if MOVIES[i].get("title").casefold() == update_movie.get("title").casefold():
            MOVIES[i] = update_movie
            return {"message": "Movie updated successfully"}
    return {"message": "Movie not found"}


@app.delete("/movies/delete_movie/{movie_title}")
async def delete_movie(movie_title: str):
    for i in range(len(MOVIES)):
        if MOVIES[i].get("title").casefold() == movie_title.casefold():
            MOVIES.pop(i)
            return {"message": "Movie deleted successfully"}
    return {"message": "Movie not found"}
