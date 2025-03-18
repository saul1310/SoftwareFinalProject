from pomodoro import minutes_to_seconds, countdown_timer

# Ask user for input regarding study time, rest time, and the number of cycles
study = input("Enter your focus interval in minutes: ")
rest = input("Enter your break interval in minutes: ")
cycles = int(input("Enter the number of cycles you wish to complete (focus + break = 1 cycle): "))

# Convert the study and rest times to seconds
study_sec, rest_sec = minutes_to_seconds(study, rest)

# Run the cycles
for cycle in range(cycles):
    print(f"\nCycle {cycle + 1} - Study Time")
    countdown_timer(study_sec)  # Focus session
    print(f"\nCycle {cycle + 1} - Rest Time")
    countdown_timer(rest_sec)  # Break session

print("The timer has ended, and all cycles have been completed")
