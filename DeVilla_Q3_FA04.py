# DeVilla_Q3_FA04.py
# Challenge Task 1: Find the Top Performer (Step Count Dataset)

# Given dataset with names (bonus included)
names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

# Calculate total steps for each person and store results
total_steps = []
for i in range(len(names)):
    total = sum(steps[i])
    total_steps.append(total)
    print(f"{names[i]}'s total steps: {total}")

# Find top performer, highest total, and lowest total
highest_total = max(total_steps)
lowest_total = min(total_steps)
top_performer = names[total_steps.index(highest_total)]

# Display key results
print(f"\nTop performer: {top_performer} (Total steps: {highest_total})")
print(f"Difference between highest and lowest total steps: {highest_total - lowest_total}")
