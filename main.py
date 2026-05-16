import csv
import json



INPUT_FILE = "attendance.csv"
OUTPUT_CSV_FILE = "statuses.csv"
OUTPUT_JSON_FILE = "overtime_employees.json"

def get_status(hours_worked):
    if hours_worked < 8:
        return "underworked"
    
    elif hours_worked == 8:
        return "normal_hours"

    else:
        return "overtime"
    
