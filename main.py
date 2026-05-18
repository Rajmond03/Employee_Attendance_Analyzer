import csv
import json

processed_rows = []
overtimes = {}


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
    
try:
    
    with open(INPUT_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:

                hours = float(row["hours_worked"])
            except ValueError:

                print(
                    f"invalid hours value: "
                    f"{row['hours_worked']}"
                )
                continue

            status = get_status(hours)

            processed_rows.append({
                "employee_name": row["employee_name"],
                "hours_worked": hours,
                "status": status
            })
except FileNotFoundError:
    print(f"File not found: {INPUT_FILE}")

    exit()
    
with open(OUTPUT_CSV_FILE, "w", newline="") as file:
    writer = csv.DictWriter(
        file, 
        fieldnames = [
            "employee_name",
            "hours_worked",
            "status"
        ]
    )
    writer.writeheader()

    writer.writerows(processed_rows)

with open(OUTPUT_CSV_FILE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        hours_worked = float(row["hours_worked"])

        if row["status"] == "overtime":

            overtime_hours = hours_worked - 8   
            
            employee_name = row["employee_name"]
            
            if employee_name in overtimes:
                overtimes[employee_name] += overtime_hours

            else:
                overtimes[employee_name] = overtime_hours


with open(OUTPUT_JSON_FILE, "w", encoding = "utf-8") as file:
    json.dump(overtimes, file, indent=4)



