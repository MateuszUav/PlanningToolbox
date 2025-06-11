from tkcalendar import Calendar
from tkinter import filedialog
import csv
DB_USER = "s30765"
DB_PASSWORD = "oracle12"
DB_DSN = "db-oracle.pjwstk.edu.pl:1521/baza.pjwstk.edu.pl"
def show_calendar_window():
    def on_date_selected(event):
        selected_date = cal.selection_get()
        date_label.config(text=f"Selected Date: {selected_date}")
        entry_date.set(selected_date.strftime("%Y-%m-%d"))

    def import_csv_for_selected_date(data_type):
        path = filedialog.askopenfilename(
            title=f"Import {data_type.upper()} CSV",
            filetypes=[("CSV Files", "*.csv")]
        )
        if not path:
            return

        try:
            db = FitnessDBInserter(DB_USER, DB_PASSWORD, DB_DSN)
            with open(path, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # skip header
                selected = datetime.datetime.strptime(entry_date.get(), "%Y-%m-%d").date()

                for row in reader:
                    if data_type == 'workout':
                        type_, desc, duration, cal_burned = row
                        db.insert_workout(
                            current_user_id, selected, type_, desc, float(duration), float(cal_burned)
                        )
                    elif data_type == 'pr':
                        name, value, unit = row
                        db.insert_personal_record(
                            current_user_id, name, float(value), unit, selected
                        )
                    elif data_type == 'goal':
                        title, target, current, unit = row
                        db.insert_goal(
                            current_user_id, title, target, current, unit, selected
                        )

            db.commit()
            db.close()
            messagebox.showinfo("Import", f"{data_type.upper()} import complete for {selected}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    calendar_window = tk.Toplevel(root)
    calendar_window.title("Workout Calendar")

    cal = Calendar(calendar_window, selectmode='day', year=2025, month=6, day=10, date_pattern='yyyy-mm-dd')
    cal.pack(pady=10)
    cal.bind("<<CalendarSelected>>", on_date_selected)

    date_label = tk.Label(calendar_window, text="No date selected")
    date_label.pack()

    entry_date = tk.StringVar()
    form_frame = tk.Frame(calendar_window)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Workout Type").grid(row=0, column=0)
    workout_type_entry = tk.Entry(form_frame)
    workout_type_entry.grid(row=0, column=1)

    tk.Label(form_frame, text="Description").grid(row=1, column=0)
    workout_desc_entry = tk.Entry(form_frame)
    workout_desc_entry.grid(row=1, column=1)

    tk.Label(form_frame, text="Duration (min)").grid(row=2, column=0)
    workout_duration_entry = tk.Entry(form_frame)
    workout_duration_entry.grid(row=2, column=1)

    tk.Label(form_frame, text="Calories Burned").grid(row=3, column=0)
    workout_calories_entry = tk.Entry(form_frame)
    workout_calories_entry.grid(row=3, column=1)

    tk.Label(form_frame, text="PR Exercise Name").grid(row=4, column=0)
    pr_exercise_entry = tk.Entry(form_frame)
    pr_exercise_entry.grid(row=4, column=1)

    tk.Label(form_frame, text="Record Value").grid(row=5, column=0)
    pr_value_entry = tk.Entry(form_frame)
    pr_value_entry.grid(row=5, column=1)

    tk.Label(form_frame, text="Unit").grid(row=6, column=0)
    pr_unit_entry = tk.Entry(form_frame)
    pr_unit_entry.grid(row=6, column=1)

    tk.Label(form_frame, text="Goal Title").grid(row=7, column=0)
    goal_title_entry = tk.Entry(form_frame)
    goal_title_entry.grid(row=7, column=1)

    tk.Label(form_frame, text="Target Value").grid(row=8, column=0)
    goal_target_entry = tk.Entry(form_frame)
    goal_target_entry.grid(row=8, column=1)

    tk.Label(form_frame, text="Current Value").grid(row=9, column=0)
    goal_current_entry = tk.Entry(form_frame)
    goal_current_entry.grid(row=9, column=1)

    tk.Label(form_frame, text="Unit").grid(row=10, column=0)
    goal_unit_entry = tk.Entry(form_frame)
    goal_unit_entry.grid(row=10, column=1)

    def submit_all():
        try:
            selected = datetime.datetime.strptime(entry_date.get(), "%Y-%m-%d").date()
            db = FitnessDBInserter(DB_USER, DB_PASSWORD, DB_DSN)

            if workout_type_entry.get():
                db.insert_workout(
                    current_user_id,
                    selected,
                    workout_type_entry.get(),
                    workout_desc_entry.get(),
                    float(workout_duration_entry.get()),
                    float(workout_calories_entry.get())
                )

            if pr_exercise_entry.get():
                db.insert_personal_record(
                    current_user_id,
                    pr_exercise_entry.get(),
                    float(pr_value_entry.get()),
                    pr_unit_entry.get(),
                    selected
                )

            if goal_title_entry.get():
                db.insert_goal(
                    current_user_id,
                    goal_title_entry.get(),
                    goal_target_entry.get(),
                    goal_current_entry.get(),
                    goal_unit_entry.get(),
                    selected
                )

            db.commit()
            db.close()
            messagebox.showinfo("Success", "Manual entries saved.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    button_frame = tk.Frame(calendar_window)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Submit Entries", command=submit_all).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Import Workouts CSV", command=lambda: import_csv_for_selected_date('workout')).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Import PRs CSV", command=lambda: import_csv_for_selected_date('pr')).grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Import Goals CSV", command=lambda: import_csv_for_selected_date('goal')).grid(row=0, column=3, padx=5)