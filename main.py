
import pandas as pd
import numpy as np

def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"

def get_result(average, attendance):
    if average >= 40 and attendance >= 75:
        return "PASS"
    else:
        return "FAIL"

def main():
    students = pd.read_csv("students.csv")
    subjects = ["Python", "SQL", "Statistics"]

    students["Total"] = students[subjects].sum(axis=1)
    students["Average"] = np.round(
        students["Total"] / len(subjects), 2
    )

    students["Grade"] = [
        get_grade(avg) for avg in students["Average"]
    ]

    students["Result"] = [
        get_result(students.loc[i, "Average"],
                   students.loc[i, "Attendance"])
        for i in range(len(students))
    ]

    print("\\n" + "=" * 65)
    print("          STUDENT PERFORMANCE ANALYTICS")
    print("=" * 65)
    print("Total Students :", len(students))
    print("Class Average  :", round(np.mean(students["Average"]), 2))

    top_students = students.sort_values(
        by="Average", ascending=False
    ).head(3)

    print("\\nTOP 3 PERFORMERS")
    print("-" * 40)
    for i in range(len(top_students)):
        print(i + 1, top_students.iloc[i]["Name"],
              "- Average:", top_students.iloc[i]["Average"])

    print("\\nSUBJECT-WISE AVERAGES")
    print("-" * 40)
    for subject in subjects:
        print(subject, ":", round(students[subject].mean(), 2))

    print("\\nRESULT SUMMARY")
    print("Passed Students :", (students["Result"] == "PASS").sum())
    print("Failed Students :", (students["Result"] == "FAIL").sum())

    students.to_csv("students.csv", index=False)

    print("\\nFINAL STUDENT REPORT")
    print("-" * 65)
    print(students.to_string(index=False))
    print("=" * 65)
    print("ANALYSIS COMPLETED")

if __name__ == "__main__":
    main()
