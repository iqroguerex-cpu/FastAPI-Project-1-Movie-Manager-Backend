# 🎬 Movie Manager API (FastAPI)

[![Live API](https://img.shields.io/badge/API-Live-success?style=for-the-badge)](https://fastapi-project-1-movie-manager.onrender.com)
[![API Docs](https://img.shields.io/badge/Docs-Swagger-blue?style=for-the-badge)](https://fastapi-project-1-movie-manager.onrender.com/docs)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge\&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge\&logo=fastapi)
![Render](https://img.shields.io/badge/Hosted%20on-Render-purple?style=for-the-badge)

A **REST API built with FastAPI** for managing a collection of movies.
The API supports full **CRUD operations** and filtering capabilities.

---

# 🌐 Live API

**Base URL**

https://fastapi-project-1-movie-manager.onrender.com

**Interactive API Docs**

https://fastapi-project-1-movie-manager.onrender.com/docs

---

# 🚀 Features

* 🎬 Get all movies
* 🔎 Get movie by title
* 🎭 Filter movies by genre
* 👨‍🎬 Filter by director and genre
* ➕ Add new movie
* ✏️ Update movie
* ❌ Delete movie
* 📚 Interactive API documentation (Swagger)

---

# 🛠 Tech Stack

### Backend

* **FastAPI**
* **Python**

### Server

* **Uvicorn**

### Deployment

* **Render**

---

# 📂 Project Structure

```id="9l4r2k"
fastapi-project-1-movie-manager
│
├── movie_api.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation (Local Setup)

Clone the repository

```id="ho3o9o"
git clone https://github.com/iqroguerex-cpu/fastapi-project-1-movie-manager.git
```

Navigate into the project folder

```id="6soky9"
cd fastapi-project-1-movie-manager
```

Install dependencies

```id="9u4wru"
pip install -r requirements.txt
```

Run the FastAPI server

```id="a2qknf"
uvicorn movie_api:app --reload --port 8002
```

Open the interactive API documentation

```id="6r6x1q"
http://127.0.0.1:8002/docs
```

---

# 📡 API Endpoints

| Method | Endpoint                             | Description                |
| ------ | ------------------------------------ | -------------------------- |
| GET    | `/movies`                            | Get all movies             |
| GET    | `/movies/{movie_title}`              | Get movie by title         |
| GET    | `/movies/?genre=action`              | Filter movies by genre     |
| GET    | `/movies/{director}/?genre=sci-fi`   | Filter by director & genre |
| POST   | `/movies/create_movie`               | Add a new movie            |
| PUT    | `/movies/update_movie`               | Update a movie             |
| DELETE | `/movies/delete_movie/{movie_title}` | Delete a movie             |

---

# 🎯 Example Movie Object

```id="nnv4ta"
{
  "title": "Inception",
  "director": "Christopher Nolan",
  "genre": "sci-fi",
  "rating": 9
}
```

---

# 🌐 Frontend Application

The **frontend dashboard** for this API is hosted separately.

Frontend Repository
https://github.com/iqroguerex-cpu/FastAPI-Project-1-Movie-Manager-Frontend

Live Frontend UI
https://iqroguerex-cpu.github.io/FastAPI-Project-1-Movie-Manager-Frontend/

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

https://fastapi-project-1-movie-manager.onrender.com/docs

---

# 📄 License

This project is **open-source** and available for **learning and educational purposes**.

---

⭐ If you like this project, consider **starring the repository**.
