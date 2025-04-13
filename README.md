# PlanningToolbox

# MVP requirments:

Here's a clear and actionable **project plan** for the "Niezbędnik Ucznia" (Student Toolkit) system, written from the perspective of a professional software engineer.

---

## 🎯 **MVP Goal**
Create a desktop application with:
- User login & registration
- Editable class schedule (plan lekcji)
- Gradebook (dziennik ocen)
- Basic performance statistics
- Export functionality (PDF or CSV)
- Persistent, encrypted user data via ORM

---

## 🧱 **High-Level Architecture**
```
[GUI Frontend] ←→ [App Logic (Controllers)] ←→ [Database via ORM]
      ↑                                         ↓
 [PDF/CSV Export]                        [Encrypted User Data]
```

### Components:
1. **Frontend (GUI)** – Simple, interactive interface (Tkinter or PyQt)
2. **Application Logic** – Handles user interaction, input validation, business logic
3. **Database Layer** – Uses ORM (e.g., SQLAlchemy)
4. **Export Module** – PDF and CSV generation
5. **Security** – Password hashing + encrypted data

---

## 🧰 **Suggested Tech Stack**
| Layer           | Technology           |
|----------------|----------------------|
| GUI            | Tkinter (standard) or PyQt5 (more modern) |
| ORM            | SQLAlchemy           |
| DB Engine      | SQLite (for MVP)     |
| Security       | `bcrypt`, `cryptography` for data encryption |
| Export         | `reportlab` for PDF, `csv` module for CSV |
| Documentation  | `pdoc` or `Sphinx` + `LaTeX`/`wkhtmltopdf` for PDF |
| Version Control| Git + GitHub         |
| Packaging      | `pyinstaller` (optional for .exe) |

---

## 📌 **Task Breakdown**

### 🔐 User Authentication
- [ ] Register new user (hashed password, encrypted profile data)
- [ ] Login with validation
- [ ] Save user sessions (optional)

### 📅 Plan Lekcji (Schedule)
- [ ] GUI to add/edit/delete subjects per day
- [ ] Save schedule to DB
- [ ] Export to PDF/CSV

### 📓 Dziennik Ocen (Gradebook)
- [ ] Add/edit/delete grades by subject
- [ ] Track dates, grade types
- [ ] Export to PDF/CSV

### 📊 Statystyki
- [ ] Average grade per subject
- [ ] Overall average
- [ ] Graphs (optional with `matplotlib`)
- [ ] Export to PDF

### 📂 Export Modules
- [ ] PDF generation for each module
- [ ] CSV fallback

### 💾 Persistence Layer
- [ ] Define ORM models: User, Schedule, Grade
- [ ] Encrypt sensitive fields (user data)
- [ ] Initialize and migrate DB

### 📘 Documentation
- [ ] Docstrings for all methods/classes
- [ ] Generate HTML/PDF docs with `pdoc` or `Sphinx`
- [ ] README with usage instructions

### 🚀 Deployment
- [ ] Package app
- [ ] Upload to GitHub
- [ ] Include documentation and example DB file

---

## 📈 **Development Steps**

### Week 1 – Setup & Auth
- Initialize GitHub repo
- Set up project structure and virtual environment
- Implement user registration/login (with bcrypt)
- Create basic GUI layout

### Week 2 – Schedule & Gradebook
- Build GUI + DB logic for plan lekcji
- Add gradebook functionality
- Connect DB with GUI

### Week 3 – Statistics & Export
- Implement stats module
- Add PDF/CSV export (use dummy data first)
- Finalize DB models and test encryption

### Week 4 – Polishing & Documentation
- Final GUI improvements
- Generate documentation and convert to PDF
- Package everything and push to GitHub

---

## 📁 Suggested Folder Structure
```
NiezbednikUcznia/
├── main.py
├── gui/
│   ├── login.py
│   ├── schedule.py
│   ├── grades.py
│   └── stats.py
├── models/
│   ├── user.py
│   ├── schedule.py
│   └── grade.py
├── services/
│   ├── auth.py
│   ├── encryption.py
│   └── export.py
├── docs/
│   └── generated_docs.pdf
├── README.md
└── requirements.txt
```

---

Would you like a starter template in Python or the GitHub repo structure zipped up to kick things off?


