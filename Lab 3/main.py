# ***************************************************
# CS03A - Summer 2026
# Lab 3 - Challenge 2
# Student Name: Dan Grewal
# SID: 20497712
# ***************************************************

def max(a, b):
    # return whichever number is bigger
    if a > b:
        return a
    else:
        return b


def main():
    first = int(input("Enter the first integer: "))
    second = int(input("Enter the second integer: "))
    print(f"The greater value is {max(first, second)}")


if __name__ == "__main__":
    main()
