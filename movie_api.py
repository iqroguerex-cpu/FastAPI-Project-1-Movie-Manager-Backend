from fastapi import FastAPI, Body, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import boto3

app = FastAPI()

# 1. FIX: Middleware to handle AWS Stage Name (/default)
@app.middleware("http")
async def strip_stage_prefix(request: Request, call_next):
    path = request.scope.get("path", "")
    # If AWS prepends /default to the path, we strip it so FastAPI routes work
    if path.startswith("/default"):
        request.scope["path"] = path.replace("/default", "", 1)
    
    response = await call_next(request)
    return response

# 2. CORS Setup - Allows your frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. DynamoDB setup
# Note: Ensure your Lambda has the 'AmazonDynamoDBFullAccess' policy attached
dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
table = dynamodb.Table("movies")

@app.get("/")
async def root():
    return {"message": "Movie Manager API Running with DynamoDB 🚀"}

# Get all movies
@app.get("/movies")
async def get_movies():
    try:
        response = table.scan()
        return response.get("Items", [])
    except Exception as e:
        return {"error": str(e)}

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
    # In DynamoDB put_item replaces the item
    table.put_item(Item=updated_movie)
    return {"message": "Movie updated"}

# Delete movie
@app.delete("/movies/{movie_title}")
async def delete_movie(movie_title: str):
    table.delete_item(Key={"title": movie_title})
    return {"message": "Movie deleted"}

# 4. Lambda handler
handler = Mangum(app)
