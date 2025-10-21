
# 🧩 String Analyzer API 🚀

A simple **FastAPI** backend that analyzes strings — computing useful properties such as length, palindrome status, unique characters, word count, SHA-256 hash, and character frequency.


## 🚀 Live Deployment

The API is live and running on **Railway**:  
👉 [https://hng-stage1-backend-string-analayzer-production-48a2.up.railway.app/](https://hng-stage1-backend-string-analayzer-production-48a2.up.railway.app/)

### Example Usage
```bash
GET https://hng-stage1-backend-string-analayzer-production-48a2.up.railway.app/strings/hello

---

## 📦 Features

- Analyze and store string data
- Retrieve analyzed strings by ID
- List all analyzed strings with filtering options
- Filter using **natural language queries**
- Delete strings from storage

---

## 🧠 Tech Stack

* **FastAPI** → for building RESTful APIs
* **Pydantic** → for request validation
* **Uvicorn** → for running the ASGI server

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

(Or manually install)

```bash
pip install fastapi uvicorn pydantic
```

### 4️⃣ Run the server

```bash
uvicorn main:app --reload
```

### 5️⃣ Test the endpoints

* Open **Docs** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Root check → [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Project Structure

```
.
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🌐 API Endpoints

| Method     | Endpoint                              | Description                            |
| ---------- | ------------------------------------- | -------------------------------------- |
| **POST**   | `/strings`                            | Analyze and store a new string         |
| **GET**    | `/strings/{string_value}`             | Retrieve specific analyzed string      |
| **GET**    | `/strings`                            | Get all strings with optional filters  |
| **GET**    | `/strings/filter-by-natural-language` | Use natural language to filter strings |
| **DELETE** | `/strings/{string_value}`             | Delete a string from storage           |

---

## 🧾 Example Natural Language Queries

| Query                                                | Interpreted Filters                          |
| ---------------------------------------------------- | -------------------------------------------- |
| `"all single word palindromic strings"`              | `word_count=1`, `is_palindrome=true`         |
| `"strings longer than 10 characters"`                | `min_length=11`                              |
| `"strings containing the letter z"`                  | `contains_character=z`                       |
| `"palindromic strings that contain the first vowel"` | `is_palindrome=true`, `contains_character=a` |

