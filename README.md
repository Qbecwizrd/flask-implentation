# 🏪 Flask Store API

A simple **Flask-based REST API** for creating stores and managing items inside them.
Think of it as your **mini e-commerce backend** — lightweight, fast, and easy to extend 🚀

---

## ✨ Features

* 🏬 **Create and fetch stores**
* 📦 **Add items** to a specific store
* 🔍 **Retrieve all items** in a store
* ⚡ **Lightweight & beginner-friendly Flask app**

---

## 📂 Project Structure

```
store-api/
│── app.py        # Main Flask app
│── README.md     # Project Documentation
```

---

## ▶️ How to Run

1. **Clone the repo** 🖥️

   ```bash
   git clone https://github.com/yourusername/store-api.git
   cd store-api
   ```

2. **Install dependencies** 📦

   ```bash
   pip install flask
   ```

3. **Run the app** 🚀

   ```bash
   python app.py
   ```

4. API will be available at 👉 `http://127.0.0.1:5000/`

---

## 🔑 Endpoints

### 1️⃣ Get all stores 🏪

```http
GET /store
```

✅ Example Response:

```json
{
  "store": [
    {
      "name": "My Store",
      "items": [
        { "name": "chair", "price": 15.99 }
      ]
    }
  ]
}
```

---

### 2️⃣ Create a new store ➕

```http
POST /store
```

📌 Example Request:

```json
{ "name": "Book Store" }
```

✅ Example Response:

```json
{ "name": "Book Store", "items": [] }
```

---

### 3️⃣ Add an item to a store 📦

```http
POST /store/<name>/item
```

📌 Example Request:

```json
{ "name": "Table", "price": 49.99 }
```

✅ Example Response:

```json
{ "name": "Table", "price": 49.99 }
```

---

### 4️⃣ Get a single store 🔍

```http
GET /store/<name>
```

✅ Example Response:

```json
{
  "name": "My Store",
  "items": [
    { "name": "chair", "price": 15.99 }
  ]
}
```

---

### 5️⃣ Get items from a store 🛒

```http
GET /store/<name>/item
```

✅ Example Response:

```json
{
  "items": [
    { "name": "chair", "price": 15.99 }
  ]
}
```

---

## 💡 Future Enhancements

* 🔐 Add authentication (JWT)
* 🗄️ Persist data with a real database (SQLite / PostgreSQL)
* 🌐 Deploy on Render / Railway / Heroku
* 📊 Build a small frontend to visualize stores

---

## 🧑‍💻 Author

Built with ❤️ using **Flask** by *Abdul Jabbar* ✨

---

Do you want me to make this README **professional (GitHub portfolio style)** or keep it **fun & playful with emojis** like this version?
