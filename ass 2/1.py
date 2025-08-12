# 1 Convert the time entered in hh,min and sec into seconds.

num = int(input("Enter a number (in seconds): "))
def calculate_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

hrs, mins, secs = calculate_time(num)
print(f'{hrs} hours, {mins} minutes, and {secs} seconds.')
