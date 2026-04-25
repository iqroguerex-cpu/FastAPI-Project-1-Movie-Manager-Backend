from fastapi import FastAPI, Body, Query
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import boto3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DynamoDB setup
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("movies")


@app.get("/")
async def root():
    return {"message": "Movie Manager API Running with DynamoDB 🚀"}


# Get all movies
@app.get("/movies")
async def get_movies():
    response = table.scan()
    return response.get("Items", [])


# Get movie by title
@app.get("/movies/title/{movie_title}")
async def get_movie(movie_title: str):
    response = table.get_item(Key={"title": movie_title})
    return response.get("Item", {"message": "Movie not found"})


# Filter by genre
@app.get("/movies/genre")
async def get_by_genre(genre: str = Query(...)):
    response = table.scan()
    return [
        item for item in response.get("Items", [])
        if item.get("genre", "").lower() == genre.lower()
    ]


# Create movie
@app.post("/movies")
async def create_movie(movie=Body()):
    table.put_item(Item=movie)
    return {"message": "Movie added"}


# Update movie
@app.put("/movies/{movie_title}")
async def update_movie(movie_title: str, updated_movie=Body()):
    table.put_item(Item=updated_movie)
    return {"message": "Movie updated"}


# Delete movie
@app.delete("/movies/{movie_title}")
async def delete_movie(movie_title: str):
    table.delete_item(Key={"title": movie_title})
    return {"message": "Movie deleted"}


# Lambda handler
handler = Mangum(app)
