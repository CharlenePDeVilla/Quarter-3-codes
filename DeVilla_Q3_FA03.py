# DeVilla_Q3_FA03.py
# Activity 2: Summarizing Test Scores Dataset with Arrays

# 1. Reuse 2D Array from Activity 1
# Rows = Students (A-E); Columns = Subjects (Math, Science, English)
test_scores = [
    [85, 92, 78],   # Student A
    [79, 88, 91],   # Student B
    [95, 80, 85],   # Student C
    [82, 78, 90],   # Student D 
    [70, 83, 87]    # Student E
]
student_names = ["Student A", "Student B", "Student C", "Student D", "Student E"]


# 2. Summarize the Dataset
print("=== STUDENT TEST SCORES SUMMARY ===\n")

# Print each row clearly + calculate row totals/averages
for i in range(len(test_scores)):
    student = student_names[i]
    scores = test_scores[i]
    total = sum(scores)
    average = total / len(scores)
    
    print(f"{student}: Scores = {scores}")
    print(f"  Total Score: {total} | Average Score: {average:.1f}\n")


# 3. Short Explanation
print("=== EXPLANATION ===")
print("Using a 2D array made it easy to group each student’s scores together and loop through rows/columns to calculate totals/averages without rewriting code for each entry.")
print("Printing each row and computing totals was straightforward with loops and built-in functions like sum().")
print("The trickiest part was flattening the array to find the overall maximum score, but nesting lists made it manageable once I broke down the steps.")
