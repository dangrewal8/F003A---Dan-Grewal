# ***************************************************
# CS03A - Summer 2026
# Assignment 1 - Question 2
# Student Name: Dan Grewal
# SID: 20497712
# ***************************************************

def run():
    month = int(input("Enter the month as a number: "))
    day = int(input("Enter the day: "))
    year = int(input("Enter the two-digit year: "))

    # if the month times the day equals the year then its magic
    if month * day == year:
        print("That date is magic!")
    else:
        print("That date is not magic.")


if __name__ == "__main__":
    run()
