# DeVilla_Q3_FA07.py
# Activity: Summarize Step Count Dataset Using 2D Arrays

# Reused 2D Array from Activity 1: Rows = People, Columns = Daily Steps (Mon-Fri)
names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

# Print each row clearly
print("=== DAILY STEP COUNTS PER PARTICIPANT ===")
for i in range(len(names)):
    print(f"{names[i]}: {steps[i]}")

# Calculate and display row totals + averages
print("\n=== SUMMARY PER PARTICIPANT ===")
row_totals = []
for i in range(len(names)):
    total = sum(steps[i])
    average = total / len(steps[i])
    row_totals.append(total)
    print(f"{names[i]} - Total Steps: {total} | Average Daily Steps: {average:.1f}")

# Optional: Find overall maximum value in the dataset
all_steps = [step for row in steps for step in row]
max_step = max(all_steps)
print(f"\nOptional: Highest single-day step count across all participants: {max_step}")

# Short Explanation (3-4 sentences)
print("\n=== EXPLANATION ===")
print("Using a 2D array grouped related data neatly – each row held all daily steps for one person, so I could loop through rows to calculate totals/averages without rewriting code.")
print("Printing each row and computing sums/averages was easy with built-in functions like sum() and simple loops.")
print("The trickiest part was flattening the array to find the overall maximum step count, but breaking it down into a nested list comprehension made it manageable.")
