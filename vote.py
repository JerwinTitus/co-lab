def check_eligibility(age):
    if age >= 18:
        print("Congratulations! You are eligible to vote.")
    else:
        print("Sorry, you are not eligible to vote yet.")

def main():
    try:
        age = int(input("Please enter your age: "))
        check_eligibility(age)
    except ValueError:
        print("Please enter a valid age as a number.")

if __name__ == "__main__":
    main()
