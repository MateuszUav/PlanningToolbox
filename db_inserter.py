import oracledb
import datetime

INSERT_USER_SQL = """
    INSERT INTO user_account (username, email, weight_kg, height_cm, birth_date)
    VALUES (:username, :email, :weight_kg, :height_cm, :birth_date)
    RETURNING user_id INTO :id_out
"""

INSERT_WORKOUT_SQL = """
    INSERT INTO workout (user_id, workout_date, type, description, duration_min, calories_burned)
    VALUES (:user_id, :workout_date, :type, :description, :duration_min, :calories_burned)
"""

INSERT_PR_SQL = """
    INSERT INTO personal_record (user_id, exercise_name, record_value, unit, record_date)
    VALUES (:user_id, :exercise_name, :record_value, :unit, :record_date)
"""

INSERT_GOAL_SQL = """
    INSERT INTO goal (user_id, title, target_value, current_value, unit, deadline, achieved)
    VALUES (:user_id, :title, :target_value, :current_value, :unit, :deadline, :achieved)
"""
INSERT_PASSWORD_SQL = """
    INSERT INTO user_password (user_id, password_hash, active)
    VALUES (:user_id, :password_hash, 'Y')
"""



class FitnessDBInserter:
    def __init__(self, user, password, dsn):
        self.connection = oracledb.connect(user=user, password=password, dsn=dsn)
        self.cursor = self.connection.cursor()
        self._pending = False

    def insert_user(self, username, email, weight_kg, height_cm, birth_date):
        id_var = self.cursor.var(oracledb.NUMBER)
        self.cursor.execute(INSERT_USER_SQL, {
            "username": username,
            "email": email,
            "weight_kg": weight_kg,
            "height_cm": height_cm,
            "birth_date": birth_date,
            "id_out": id_var
        })
        self._pending = True
        return int(id_var.getvalue()[0])

    def insert_workout(self, user_id, workout_date, type, description, duration_min, calories_burned):
        self.cursor.execute(INSERT_WORKOUT_SQL, {
            "user_id": user_id,
            "workout_date": workout_date,
            "type": type,
            "description": description,
            "duration_min": duration_min,
            "calories_burned": calories_burned
        })
        self._pending = True

    def insert_personal_record(self, user_id, exercise_name, record_value, unit, record_date):
        self.cursor.execute(INSERT_PR_SQL, {
            "user_id": user_id,
            "exercise_name": exercise_name,
            "record_value": record_value,
            "unit": unit,
            "record_date": record_date
        })
        self._pending = True

    def insert_goal(self, user_id, title, target_value, current_value, unit, deadline, achieved='N'):
        self.cursor.execute(INSERT_GOAL_SQL, {
            "user_id": user_id,
            "title": title,
            "target_value": target_value,
            "current_value": current_value,
            "unit": unit,
            "deadline": deadline,
            "achieved": achieved
        })
        self._pending = True


    def insert_password(self, user_id, password_hash):
        self.cursor.execute(INSERT_PASSWORD_SQL, {
            "user_id": user_id,
            "password_hash": password_hash
        })
        self._pending = True

    def commit(self):
        if self._pending:
            self.connection.commit()
            self._pending = False

    def close(self):
        self.cursor.close()
        self.connection.close()
