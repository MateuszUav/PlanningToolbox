-- Sample inserts
INSERT INTO user_account (username, email, weight_kg, height_cm, birth_date)
VALUES ('max', 'max@example.com', 87.5, 180, DATE '2003-04-21');

INSERT INTO workout (user_id, workout_date, type, description, duration_min, calories_burned)
VALUES (1, SYSDATE - 1, 'Strength', 'Heavy lower body: squat 5x5, RDLs, lunges', 75, 550);

INSERT INTO personal_record (user_id, exercise_name, record_value, unit, record_date)
VALUES (1, 'Deadlift', 200, 'kg', DATE '2025-03-20');

INSERT INTO goal (user_id, title, target_value, current_value, unit, deadline, achieved)
VALUES (1, '3km under 12 minutes', '11:59', '12:45', 'minutes', DATE '2025-06-15', 'N');