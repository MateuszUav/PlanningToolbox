from db_inserter import FitnessDBInserter
import csv
import datetime

import getpass
#DB_PASSWORD = getpass.getpass("Enter your password: ")
DB_USER = "s30765"
DB_PASSWORD = "oracle12"
#DB_DSN = "jdbc:oracle:thin:@//localhost:1521/freepdb1"
DB_DSN = "db-oracle.pjwstk.edu.pl:1521/baza.pjwstk.edu.pl"

def import_users(db, path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            username, email, weight_kg, height_cm, birth_date = row
            user_id = db.insert_user(username, email, float(weight_kg), float(height_cm), datetime.datetime.strptime(birth_date, '%Y-%m-%d').date())
            print(f"✅ Inserted user '{username}' (ID: {user_id})")

def import_workouts(db, path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            user_id, workout_date, type_, description, duration_min, calories_burned = row
            db.insert_workout(int(user_id), datetime.datetime.strptime(workout_date, '%Y-%m-%d').date(), type_, description, float(duration_min), float(calories_burned))
            print(f"✅ Workout for user {user_id} on {workout_date} added.")

def import_personal_records(db, path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            user_id, exercise_name, record_value, unit, record_date = row
            db.insert_personal_record(int(user_id), exercise_name, float(record_value), unit, datetime.datetime.strptime(record_date, '%Y-%m-%d').date())
            print(f"✅ PR '{exercise_name}' for user {user_id} on {record_date} added.")

def import_goals(db, path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            user_id, title, target_value, current_value, unit, deadline, achieved = row
            db.insert_goal(int(user_id), title, target_value, current_value, unit, datetime.datetime.strptime(deadline, '%Y-%m-%d').date(), achieved)
            print(f"✅ Goal '{title}' for user {user_id} added.")

def main():
    db = FitnessDBInserter(DB_USER, DB_PASSWORD, DB_DSN)
    try:
        import_users(db, "users.csv")
        import_workouts(db, "workouts.csv")
        import_personal_records(db, "prs.csv")
        import_goals(db, "goals.csv")
        db.commit()
    except Exception as e:
        print(f"❌ ERROR: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()

