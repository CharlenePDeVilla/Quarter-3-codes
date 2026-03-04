# DeVilla_Q3_FA02.py
# Mini-Dataset Project: Weekly Test Scores for 5 Students Across 3 Subjects


# 1. Real-World Scenario & 2D Array Structure
# Rows: 5 individual students (Student A to Student E)
# Columns: Test scores for 3 subjects (Math, Science, English)
print("=== 2D Array Structure ===")
print("Rows = Students (A-E) | Columns = Subjects (Math, Science, English)\n")


# 3. Sample 2D Array
test_scores = [
    [85, 92, 78],   # Student A
    [79, 88, 91],   # Student B
    [95, 80, 85],   # Student C
    [82, 75, 90],   # Student D
    [70, 83, 87]    # Student E
]


# 4. Basic Array Operations
# Access and print a specific value (Student C's Math score)
print("1. Specific Value Access:")
print(f"Student C's Math score: {test_scores[2][0]}\n")

# Update a specific value (Student D's Science score from 75 to 78)
test_scores[3][1] = 78
print("2. Value Update:")
print(f"Updated Student D's Science score to 78. New row for Student D: {test_scores[3]}\n")

# Summarize data (calculate average Math score across all students)
math_scores = [row[0] for row in test_scores]
average_math = sum(math_scores) / len(math_scores)
print("3. Dataset Summary:")
print(f"Average Math score for all students: {average_math:.1f}\n")


# 5. Reflection
print("=== Reflection ===")
print("I chose this dataset because test scores are a common real-world example where organized tabular data is essential for tracking student performance.")
print("A 2D array helps by grouping related data points – each row keeps all scores for one student, and each column keeps scores for one subject, making it easy to access, update, or analyze specific parts of the data.")
print("This structure also simplifies calculations like class averages, as we can quickly extract entire columns or rows for processing.")
