# 📓 NoteSaver — Simple Python Note-Taking App

NoteSaver is a lightweight **command-line Python application** that lets users quickly add, view, and manage personal notes.  
This project demonstrates basic **file I/O**, **modular code**, and **timestamp handling** — a clean, beginner-friendly example for your ETL/dev portfolio.

---

## ✨ Features
- 📝 Add new notes with **automatic timestamps**  
- 📄 View all saved notes in chronological order  
- 💾 Persistent storage using a plain text file (`Notes.txt`)  
- 🎯 Simple menu-driven CLI for ease of use

---

## 🛠️ Built With
- **Python 3**  
- Standard library modules: `datetime`, `os` (no external packages required)

---

## 🚀 Quickstart — Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/vsvidhya93/NoteSaver.git
cd NoteSaver
```

2. **Run the app**
```bash
python main.py
```

---

## 📂 Project Structure
```
NoteSaver/
├── Main.py         # Main menu and user interaction
├── Functions.py    # Logic for adding and viewing notes
├── Notes.txt       # Stores all saved notes (auto-created)
└── README.md       # Project documentation
```

---

## 📄 Example Output
```
Welcome to Note Saver!

1. Add a new note
2. View all notes
3. Exit

Enter your choice: 1
Enter your note: Buy groceries
Note saved successfully!
-------------------------------------------------------
```

---

## 🔧 Implementation Notes
- `Functions.py` contains two main functions:
  - `Add_Notes(note)` — appends a timestamped note to `Notes.txt`
  - `View_Notes()` — prints notes from `Notes.txt`
- Use context managers (`with open(...)`) to handle files safely.

---

## 🔮 Future Enhancements (Ideas)
- Add ability to **delete** or **edit** notes
- Add **search** (keyword) or **filter by date**
- Export notes to **CSV** or **JSON**
- Add simple **encryption** or password protection

---

## 📜 License
This project is licensed under the **MIT License** — see `LICENSE` for details.

---

## 🙋 Author
**Vidhya Lakshmi Venkatraman Sankar** — ETL Developer (rebuilt skills: Python, file I/O, ETL basics)  
Contact: vsvidhya93@gmail.com
