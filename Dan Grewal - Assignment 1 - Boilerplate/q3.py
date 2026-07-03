# ***************************************************
# CS03A - Summer 2026
# Assignment 1 - Question 3
# Student Name: Dan Grewal
# SID: 20497712
# ***************************************************

def run():
    total_seconds = int(input("Enter a number of seconds: "))

    # start at the biggest unit that fits and work down. // gives the whole number, % gives the leftover
    if total_seconds >= 86400:
        days = total_seconds // 86400
        leftover = total_seconds % 86400
        hours = leftover // 3600
        leftover = leftover % 3600
        minutes = leftover // 60
        seconds = leftover % 60
        print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    elif total_seconds >= 3600:
        hours = total_seconds // 3600
        leftover = total_seconds % 3600
        minutes = leftover // 60
        seconds = leftover % 60
        print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
    elif total_seconds >= 60:
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        print(f"{minutes} minutes, {seconds} seconds")
    else:
        print(f"{total_seconds} seconds")


if __name__ == "__main__":
    run()
