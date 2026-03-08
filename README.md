# 🎬 Movie Manager API (FastAPI)

This is the **backend API** for the Movie Manager application built using **FastAPI**.

The API allows users to manage a collection of movies by performing **CRUD operations**.

Live API:
https://fastapi-project-1-movie-manager.onrender.com

API Docs:
https://fastapi-project-1-movie-manager.onrender.com/docs

---

# 🚀 Features

* Get all movies
* Get movie by title
* Filter movies by genre
* Filter movies by director and genre
* Add new movie
* Update movie
* Delete movie

---

# 🛠 Tech Stack

Backend Framework

* FastAPI

Server

* Uvicorn

Deployment

* Render

Language

* Python

---

# 📂 Project Structure

```
movie-manager-api
│
├── movie_api.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation (Local Setup)

Clone the repository

```
git clone https://github.com/YOUR_USERNAME/fastapi-project-1-movie-manager.git
```

Go into the folder

```
cd fastapi-project-1-movie-manager
```

Install dependencies

```
pip install -r requirements.txt
```

Run the server

```
uvicorn movie_api:app --reload --port 8002
```

Open API docs

```
http://127.0.0.1:8002/docs
```

---

# 📡 API Endpoints

| Method | Endpoint                           | Description                |
| ------ | ---------------------------------- | -------------------------- |
| GET    | /movies                            | Get all movies             |
| GET    | /movies/{movie_title}              | Get movie by title         |
| GET    | /movies/?genre=action              | Filter by genre            |
| GET    | /movies/{director}/?genre=sci-fi   | Filter by director & genre |
| POST   | /movies/create_movie               | Add movie                  |
| PUT    | /movies/update_movie               | Update movie               |
| DELETE | /movies/delete_movie/{movie_title} | Delete movie               |

---

# 🎯 Example Movie Object

```
{
  "title": "Inception",
  "director": "Christopher Nolan",
  "genre": "sci-fi",
  "rating": 9
}
```

---

# 🌐 Frontend

The frontend UI for this project is hosted separately:

Frontend Repo:
https://github.com/iqroguerex-cpu/FastAPI-Project-1-Movie-Manager-Frontend

Live UI:
https://iqroguerex-cpu.github.io/FastAPI-Project-1-Movie-Manager-Frontend/

---

# 📄 License

This project is open-source and available for learning and educational purposes.
