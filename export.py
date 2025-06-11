import oracledb
import csv

import getpass
#DB_PASSWORD = getpass.getpass("Enter your password: ")
DB_USER = "s30765"
DB_PASSWORD = "oracle12"
#DB_DSN = "jdbc:oracle:thin:@//localhost:1521/freepdb1"
DB_DSN = "db-oracle.pjwstk.edu.pl:1521/baza.pjwstk.edu.pl"

EXPORT_QUERIES = {
    "users": {
        "sql": "SELECT username, email, weight_kg, height_cm, TO_CHAR(birth_date, 'YYYY-MM-DD') FROM user_account",
        "header": ["username", "email", "weight_kg", "height_cm", "birth_date"],
        "filename": "users.csv"
    },
    "workouts": {
        "sql": "SELECT user_id, TO_CHAR(workout_date, 'YYYY-MM-DD'), type, description, duration_min, calories_burned FROM workout",
        "header": ["user_id", "workout_date", "type", "description", "duration_min", "calories_burned"],
        "filename": "workouts.csv"
    },
    "prs": {
        "sql": "SELECT user_id, exercise_name, record_value, unit, TO_CHAR(record_date, 'YYYY-MM-DD') FROM personal_record",
        "header": ["user_id", "exercise_name", "record_value", "unit", "record_date"],
        "filename": "prs.csv"
    },
    "goals": {
        "sql": "SELECT user_id, title, target_value, current_value, unit, TO_CHAR(deadline, 'YYYY-MM-DD'), achieved FROM goal",
        "header": ["user_id", "title", "target_value", "current_value", "unit", "deadline", "achieved"],
        "filename": "goals.csv"
    }
}


def export_table(cursor, query_info):
    cursor.execute(query_info["sql"])
    rows = cursor.fetchall()

    with open(query_info["filename"], "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(query_info["header"])
        writer.writerows(rows)

    print(f"✅ Exported {len(rows)} rows to {query_info['filename']}")


def main():
    connection = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cursor = connection.cursor()

    try:
        for name, q in EXPORT_QUERIES.items():
            export_table(cursor, q)
    except Exception as e:
        print(f"❌ ERROR during export: {e}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
