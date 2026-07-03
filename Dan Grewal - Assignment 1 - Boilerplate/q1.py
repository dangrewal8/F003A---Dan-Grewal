# ***************************************************
# CS03A - Summer 2026
# Assignment 1 - Question 1
# Student Name: Dan Grewal
# SID: 20497712
# ***************************************************

def run():
    # ask the user for the numbers we need
    principal = float(input("Enter the principal amount deposited: "))
    annual_rate = float(input("Enter the annual interest rate as a percent (e.g. 5 for 5%): ")) / 100
    times_per_year = int(input("Enter how many times per year interest is compounded: "))
    years = int(input("Enter the number of years: "))

    # A = P(1 + r/n)^(nt)
    amount = principal * (1 + annual_rate / times_per_year) ** (times_per_year * years)

    print(f"After {years} years, the account will have ${amount:,.2f}")


if __name__ == "__main__":
    run()
