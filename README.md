# String Analyzer API 🚀

A simple **FastAPI** backend that analyzes strings — checking their properties like length, palindrome status, unique characters, word count, hash value, and more.

---

## 📦 Features
- Analyze and store string data  
- Retrieve analyzed strings by ID  
- Get all stored strings  
- Delete a string by value  
- (working on that rn) Filter by natural language query  

---

## 🧠 Tech Stack
- **FastAPI** — for backend API  
- **Pydantic** — for data validation  
- **Uvicorn** — for running the server  

---

## ⚙️ Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
````

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install fastapi uvicorn pydantic
   ```

4. **Run the app**

   ```bash
   uvicorn main:app --reload
   ```

5. **Visit**

   * API Docs → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   * Root endpoint → [http://127.0.0.1:8000](http://127.0.0.1:8000)

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

## 🧩 To Do

* [ ] Implement `/strings/filter-by-natural-language`
