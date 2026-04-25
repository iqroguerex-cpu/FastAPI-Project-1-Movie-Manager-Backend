# 🎬 Movie Manager API (AWS Serverless)

<p align="center">

[![Live API](https://img.shields.io/badge/API-Live-success?style=for-the-badge)](https://act0h7myif.execute-api.ap-south-1.amazonaws.com/default/)
![AWS](https://img.shields.io/badge/AWS-Serverless-orange?style=for-the-badge\&logo=amazonaws)
![Lambda](https://img.shields.io/badge/AWS-Lambda-yellow?style=for-the-badge\&logo=awslambda)
![DynamoDB](https://img.shields.io/badge/Database-DynamoDB-blue?style=for-the-badge\&logo=amazondynamodb)
![API Gateway](https://img.shields.io/badge/API-Gateway-green?style=for-the-badge)

</p>

---

## 🚀 Overview

A fully **serverless REST API** built using **AWS Lambda, API Gateway, and DynamoDB** for managing a collection of movies.

This API supports core **CRUD operations** and is designed for scalability, low cost, and real-time performance without managing servers.

---

## 🌐 Live API

**Base URL**

https://act0h7myif.execute-api.ap-south-1.amazonaws.com/default/

---

## ✨ Features

* 🎬 Get all movies
* 🔎 Get movie by title
* ➕ Add new movie
* ❌ Delete movie
* ⚡ Fast serverless execution
* ☁️ Scalable AWS infrastructure
* 🗄️ Persistent storage using DynamoDB

---

## 🛠 Tech Stack

### Backend

* AWS Lambda
* API Gateway
* DynamoDB

### Language

* Python

### Deployment

* AWS Serverless Architecture

---

## 📂 Project Structure

```bash id="awsstruct1"
movie-manager-serverless
│
├── lambda_function.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. **API Gateway** receives HTTP requests
2. Triggers **AWS Lambda function**
3. Lambda processes logic
4. Data is stored/retrieved from **DynamoDB**
5. Response is returned to client

---

## 📡 API Endpoints

| Method | Endpoint          | Description     |
| ------ | ----------------- | --------------- |
| GET    | `/movies`         | Get all movies  |
| POST   | `/movies`         | Add a new movie |
| DELETE | `/movies/{title}` | Delete a movie  |

---

## 🎯 Example Request

### Add Movie

```json id="awsreq1"
{
  "title": "Inception",
  "genre": "Sci-Fi"
}
```

---

## 🌐 Frontend Application

Frontend Dashboard:

👉 https://staging.d3mluupf1gyxaw.amplifyapp.com/

Frontend Repository:

👉 https://github.com/your-username/your-frontend-repo

---

## ☁️ Architecture

* **Frontend** → AWS Amplify
* **Backend** → AWS Lambda
* **Routing** → API Gateway
* **Database** → DynamoDB

---

## 🔮 Future Improvements

* ✏️ Update movie endpoint
* 🔎 Search & filter movies
* 🔐 Authentication (JWT / AWS Cognito)
* ⭐ Rating system
* 📊 Analytics

---

## 📄 License

This project is open-source and available for educational purposes.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
