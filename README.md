# Python Web App

A simple web application built with Flask.

## 🚀 Features

- `/` returns: **Hello, World!**
- `/health` returns: **200 OK**

## 🧱 Requirements

- Docker (to build and run)

## 🛠️ Build and Run

```bash
docker build -t python-web-app .
docker run -p 8000:8000 python-web-app
```

## 🌐 Endpoints

- [`/`](http://localhost:8000/) → `Hello, World!`
- [`/health`](http://localhost:8000/health) → `200 OK`

## 🧪 Testing

To check if the app is running properly:

```bash
curl -i http://localhost:8000/health
```

Expected response:

```
HTTP/1.0 200 OK
...
OK
```

## 📁 Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## 📝 License

Anton Zherebtsov
