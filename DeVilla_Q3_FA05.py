# DeVilla_Q3_FA05.py
# Task: Compare Daily Activity Across All Participants

# Same dataset: Names = ["Me", "Lia", "Jake"]; Days = Monday to Friday
names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],  # My steps (Mon-Fri)
    [4000, 4100, 3900, 4200, 4600],  # Lia's steps
    [6000, 5800, 5900, 6100, 6200]   # Jake's steps
]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Calculate total steps per day (loop by column)
daily_totals = []
for col in range(len(steps[0])):  # Loop through each day column
    day_total = 0
    for row in range(len(steps)):  # Sum steps across all participants
        day_total += steps[row][col]
    daily_totals.append(day_total)
    print(f"{days[col]} total steps: {day_total}")

# Find most active day
most_active_idx = daily_totals.index(max(daily_totals))
print(f"\nMost active day overall: {days[most_active_idx]} (Total steps: {daily_totals[most_active_idx]})")
