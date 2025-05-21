# 🧠 NLP Text Classification API

An end-to-end, production-ready REST API for sentiment classification using FastAPI and Hugging Face Transformers. Built with secure JWT authentication and containerized with Docker for seamless deployment.

## 🚀 Features

- ⚡ **FastAPI**: High-performance asynchronous web API framework.
- 🤖 **Transformers**: Uses Hugging Face's `distilbert-base-uncased-finetuned-sst-2-english` for sentiment analysis.
- 🔐 **JWT Authentication**: Simple and secure token-based login system.
- 🐳 **Dockerized**: Easily containerized and deployable anywhere.
- 🧪 **Interactive Swagger UI** for testing endpoints.
- ☁️ **Production-ready**: Designed for deployment on cloud services like AWS EC2.

---

## 📂 Project Structure
```text
nlp-text-classification-api/
├── app/
│   ├── main.py        # FastAPI application logic
│   └── auth.py        # JWT token creation and verification
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker image definition
├── .dockerignore      # Docker ignore rules
└── README.md          # Project overview
```
---

## 🔐 Authentication

- **Username**: `admin`
- **Password**: `pass123`
- On successful login via `/login`, you'll receive a Bearer token.
- Use this token to access the `/predict` endpoint.

---

## ⚙️ Setup & Run

### 1. Run Locally (with virtualenv)

```bash
git clone https://github.com/NioshaHejazi/nlp-text-classification-api.git
cd nlp-text-classification-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Then go to:
📍 http://localhost:8000/docs to test the API.
### 2. Run with Docker
```bash
docker build -t nlp-api .
docker run -p 8000:8000 nlp-api
```
## 🔄 Example Prediction

Once the Docker container is running, you can use the `/login` endpoint to get a JWT token, and then use it to make predictions.

#### Step 1: Get a token

Make a `POST` request to the `/login` endpoint:

```bash
curl -X 'POST' \
  'http://localhost:8000/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "admin",
  "password": "pass123"
}'
```
This will return a token like:
```json
{
  "access_token": "your-token-here",
  "token_type": "bearer"
}
```
#### Step 2: Make a prediction
Use the token from the previous step to access the /predict endpoint:

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer your-token-here' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "I love working on this project"
}'
```
Example response:
```json
{
  "user": "admin",
  "label": "POSITIVE",
  "score": 0.9987
}
```
---

## 🐍 Tech Stack

- **Python 3.10**
- **FastAPI** – Web framework for building APIs
- **Hugging Face Transformers** – Pretrained BERT model for text classification
- **Torch (CPU version)** – Backend for the model
- **Python-JOSE** – JWT token creation and verification
- **Docker** – Containerization and deployment

---

## 🧼 Coming Soon

- Model customization
- Dataset ingestion pipeline
- Multi-label classification
- AWS/GCP deployment guide
- CI/CD with GitHub Actions

---

## 📜 License

MIT License © Niosha Hejazi
