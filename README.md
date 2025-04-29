---

# 📄 Athlete Toolbox MVP: Development Plan

---

## 🥅 MVP Goals (User Features)

| ID | Feature | Description |
|:-|:-|:-|
| 1 | User Login | Secure account creation, login, logout |
| 2 | Workout Logging | Add, view, edit training sessions |
| 3 | PR Tracking | Save, update personal bests |
| 6 | Goal Tracker | Create/track training goals |
| 15 | Data Export | Export workouts and PRs to CSV |

🔵 *Bonus (future-ready)*: Workout import (Garmin first, later other apps).

---

## 🏛️ High-Level Architecture

- **Frontend (GUI)** → User Interface (PyQt6 or Tkinter)
- **Backend (Core Logic)** → Python modules (services, controllers)
- **Database (Storage)** → SQLite local file (`athlete_toolbox.db`)
- **External Integration** → Garmin `.fit` or `.tcx` file parser
- **Security** → Password hashing (bcrypt)

```
GUI  <--->  Core Logic  <--->  SQLite DB
                  |
             External Data (Garmin Files)
```

---

## 🛠️ Tech Stack

| Area | Tech |
|:-|:-|
| Language | Python 3.12+ |
| GUI | PyQt6 (preferred) or Tkinter (simpler) |
| Database | SQLite (local `.db` file) |
| ORM | Tiny ORM layer or raw SQL with helpers |
| Auth | bcrypt for password hashing |
| Export | pandas for CSV generation |
| Parsing Garmin Files | fitparse or tcxparser (open-source libs) |
| Charts (optional) | matplotlib or plotly (for future graphs) |
| Dev Tools | venv (virtual environment), Git |

---

## 📚 Database Schema (First Draft)

### Table: `users`
| Column | Type | Notes |
|:-|:-|:-|
| id | INTEGER PRIMARY KEY AUTOINCREMENT |
| username | TEXT UNIQUE NOT NULL |
| password_hash | TEXT NOT NULL |

### Table: `workouts`
| Column | Type | Notes |
|:-|:-|:-|
| id | INTEGER PRIMARY KEY AUTOINCREMENT |
| user_id | INTEGER (FK -> users.id) |
| date | TEXT (ISO string) |
| workout_type | TEXT |
| description | TEXT |
| duration_minutes | INTEGER |
| distance_km | REAL (optional) |

### Table: `personal_records`
| Column | Type | Notes |
|:-|:-|:-|
| id | INTEGER PRIMARY KEY AUTOINCREMENT |
| user_id | INTEGER (FK -> users.id) |
| exercise | TEXT |
| record_value | REAL |
| record_date | TEXT |

### Table: `goals`
| Column | Type | Notes |
|:-|:-|:-|
| id | INTEGER PRIMARY KEY AUTOINCREMENT |
| user_id | INTEGER (FK -> users.id) |
| goal_description | TEXT |
| target_value | REAL |
| current_progress | REAL |
| deadline | TEXT |

---

## 🏗️ Development Roadmap (Step-by-Step)

### Phase 1: Setup
- [ ] Initialize Git repo, create project structure
- [ ] Set up virtual environment (`python -m venv venv`)
- [ ] Install needed libraries (`pip install pyqt6 bcrypt pandas`)

### Phase 2: Database + Core Logic
- [ ] Create SQLite DB (`athlete_toolbox.db`)
- [ ] Build database module (connection handler, CRUD functions)
- [ ] Build auth module (bcrypt password hashing and checking)

### Phase 3: GUI - User Management
- [ ] Build Login Window
- [ ] Build Register Window
- [ ] Session handling (track current logged user)

### Phase 4: Core App GUI
- [ ] Workout Log Window (Add, Edit, View workouts)
- [ ] PR Tracking Window (Add, View PRs)
- [ ] Goal Tracker Window (Create goal, view progress)
- [ ] Export Window (Export workouts/PRs to CSV)

### Phase 5: Garmin Import (Prototype version)
- [ ] Allow user to select `.fit` or `.tcx` file
- [ ] Parse basic info (date, distance, duration)
- [ ] Auto-add into workouts table

### Phase 6: Polish + QA
- [ ] Basic form validation
- [ ] Error messages and success popups
- [ ] DB error handling
- [ ] Light aesthetic tuning of GUI (alignments, colors)

---

## 📂 Project Structure 

```
athlete_toolbox/
│
├── main.py            # Entry point
├── db.py              # Database connection and models
├── auth.py            # Login/Registration logic
├── gui/
│    ├── login_window.py
│    ├── register_window.py
│    ├── main_app_window.py
│    ├── workout_window.py
│    ├── pr_window.py
│    ├── goals_window.py
│    └── export_window.py
├── utils/
│    ├── garmin_parser.py  # Garmin file parsing logic
│    └── csv_exporter.py   # Export helpers
├── assets/              # Icons, logos (optional)
└── README.md
```

---

## 🧩 Libraries to Install Immediately

```bash
pip install pyqt6 bcrypt pandas fitparse
```

Optionally:
```bash
pip install matplotlib
```

---

## 🧠 Smart Notes

- Use **raw SQL** for MVP — no need for heavy ORM.
- Start with **Login/Register** FIRST — everything depends on users.
- **Hardcode Garmin imports** at first (one format), expand later.
- Build **one window fully**, then duplicate for others.
- Keep **DB schema very simple** — overcomplication = death.

---
