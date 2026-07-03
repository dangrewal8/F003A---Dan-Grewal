# ***************************************************
# CS03A - Summer 2026
# Assignment 1 - Question 4
# Student Name: Dan Grewal
# SID: 20497712
# ***************************************************

def run():
    tuition = 8000.0

    # add 3% each year and print it, 5 times over
    for year in range(1, 6):
        tuition *= 1.03
        print(f"Year {year}: ${tuition:,.2f}")


if __name__ == "__main__":
    run()
