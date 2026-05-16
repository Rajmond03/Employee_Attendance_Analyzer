import csv
import json

processed_rows = []


INPUT_FILE = "C:/Users/Rajmond/Desktop/Programozás/Gyakorlás/In progress/Employee_Attendance_Analyzer/input/attendance.csv"
OUTPUT_CSV_FILE = "C:/Users/Rajmond/Desktop/Programozás/Gyakorlás/In progress/Employee_Attendance_Analyzer/output/statuses.csv"
OUTPUT_JSON_FILE = "C:/Users/Rajmond/Desktop/Programozás/Gyakorlás/In progress/Employee_Attendance_Analyzer/output/overtime_employees.json"

def get_status(hours_worked):
    if hours_worked < 8:
        return "underworked"
    
    elif hours_worked == 8:
        return "normal_hours"

    else:
        return "overtime"
    
with open(INPUT_FILE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        hours = float(row["hours_worked"])

        status = get_status(hours)

        processed_rows.append({
            "employee_name": row["employee_name"],
            "hours_worked": hours,
            "status": status
        })



