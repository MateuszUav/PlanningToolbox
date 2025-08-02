---

# ~~🏋️ Fitness Tracker System (Oracle DB + Python + Tkinter GUI)~~
Project abandoned due to lack of contribution and support. 

A modular fitness tracking system built using Python and Oracle SQL. It supports user registration, goal tracking, workout logs, personal records, and data import/export through CSV—all wrapped with a simple Tkinter GUI.

---

## 📦 Features

* ✅ User registration & login (with SHA-256 password hashing)
* 📊 Track workouts, personal records (PRs), and goals
* 🧾 Import/export data to/from CSV
* 🧑‍💻 Clean object-oriented design using a custom `FitnessDBInserter` class
* 💻 GUI with login/register functionality (Tkinter)
* 📁 Compatible CSV schema for data migration

---

## 📁 Folder Contents

| File                 | Description                                         |
| -------------------- | --------------------------------------------------- |
| `main.py`            | Entry point placeholder                             |
| `gui.py`             | Tkinter-based GUI for login/registration            |
| `db_inserter.py`     | Class for inserting data into Oracle DB             |
| `import.py`          | Imports data from CSV to DB                         |
| `export.py`          | Exports data from DB to CSV                         |
| `fitness_schema.sql` | Full Oracle SQL schema for the fitness database     |
| `inserts.sql`        | Sample data inserts                                 |
| `expectedCSV.txt`    | Shows expected CSV file structure for import/export |

---

## 🧠 Schema Overview

```sql
user_account (user_id, username, email, weight_kg, height_cm, birth_date, created_at)
workout (user_id, workout_date, type, description, duration_min, calories_burned)
personal_record (user_id, exercise_name, record_value, unit, record_date)
goal (user_id, title, target_value, current_value, unit, deadline, achieved)
user_password (user_id, password_hash, active)
```

All foreign keys are **cascading on delete**. Passwords are stored hashed and marked as active/inactive.

---

## 🚀 Setup Instructions

### 1. Clone and Set Up Oracle DB

```bash
git clone https://github.com/your_username/fitness-tracker-oracle.git
cd fitness-tracker-oracle
```

Create the schema in Oracle:

```sql
-- In SQL*Plus or similar
@fitness_schema.sql
@inserts.sql
```

### 2. Install Python Requirements

```bash
pip install oracledb
```

### 3. Configure DB Credentials

Update the DB credentials in:

* `gui.py`
* `import.py`
* `export.py`

You can replace them with `getpass.getpass()` for security.

---

## 🛠 Usage

### Run GUI

```bash
python gui.py
```

### Import CSV Data

```bash
python import.py
```

### Export Data to CSV

```bash
python export.py
```

---

## 📑 Expected CSV Format

See [expectedCSV.txt](./expectedCSV.txt) or use exported files as templates.

Example `users.csv`:

```csv
username,email,weight_kg,height_cm,birth_date
mimi,mimi@example.com,87.5,180,2003-04-21
```

---

## 📌 Notes

* The GUI allows only registration and login.
* Inserted users automatically get a default hashed password and can be assigned workouts, PRs, and goals via CSV import.
* Extendable for more analytics or web-based frontend.

---

## 🔒 Security

* Passwords are hashed using SHA-256 before being stored.
* Use SSL/TLS and environment variables in production.

---

## 🧑‍💻 Author

Built by a CS & Robotics student as a modular backend + GUI solution for tracking personal fitness metrics using Oracle DB.

---
