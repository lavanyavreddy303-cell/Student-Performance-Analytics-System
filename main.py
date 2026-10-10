import pandas as pd
import numpy as np

# Read the student dataset
data = pd.read_csv("student_performance_analytics_dataset.csv")

print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("------------------------------------")

print("\nStudent Details:")
print(data)

print("\nTotal Students:", len(data))

# Subject names from the CSV file
subjects = ["Math", "Physics", "Chemistry"]

# Calculate total and average marks
data["Total"] = data[subjects].sum(axis=1)
data["Average"] = data[subjects].mean(axis=1)

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

# Function to check pass or fail
def check_result(row):
    for subject in subjects:
        if row[subject] < 35:
            return "Fail"
    return "Pass"

# Calculate grade and result
data["Grade"] = data["Average"].apply(calculate_grade)
data["Result"] = data.apply(check_result, axis=1)

print("\nStudent Performance:")
print(data[["Student ID", "Name", "Total",
            "Average", "Grade", "Result"]].round(2))

# Overall class average
print("\nClass Average:", round(np.mean(data["Average"]), 2))

print("Highest Average:", round(data["Average"].max(), 2))
print("Lowest Average:", round(data["Average"].min(), 2))

# Top-performing student
top_student = data.loc[data["Average"].idxmax()]

print("\nTop Performing Student:")
print("Name:", top_student["Name"])
print("Department:", top_student["Department"])
print("Average:", round(top_student["Average"], 2))

# Pass and fail count
print("\nNumber of Students Passed:",
      (data["Result"] == "Pass").sum())

print("Number of Students Failed:",
      (data["Result"] == "Fail").sum())

# Subject-wise analysis
print("\nSubject-wise Average:")
for subject in subjects:
    print(subject, ":", round(data[subject].mean(), 2))

# Best and lowest performing subjects
subject_avg = data[subjects].mean()

print("\nBest Subject:", subject_avg.idxmax())
print("Lowest Subject:", subject_avg.idxmin())

# Attendance analysis
print("\nAverage Attendance:",
      round(data["Attendance (%)"].mean(), 2), "%")

print("\nStudents with Attendance Below 75%:")
print(data[data["Attendance (%)"] < 75][
    ["Student ID", "Name", "Attendance (%)"]
])

# Save the final analysis
data.to_csv("student_performance_results.csv", index=False)

print("\nAnalysis completed successfully!")
print("Results saved to student_performance_results.csv")
