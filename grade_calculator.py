# Grade Calculator Program

def main():
    # 1. Ask the user to enter the student's name
    student_name = input("Enter the student's name: ")

    # 2. Ask the user to enter marks for three subjects
    print("\nPlease enter the marks for three subjects (0-100):")
    try:
        # 3. Convert the marks to numbers (float for decimal support)
        mark1 = float(input("Subject 1: "))
        mark2 = float(input("Subject 2: "))
        mark3 = float(input("Subject 3: "))

        # 4. Calculate the average mark
        average_mark = (mark1 + mark2 + mark3) / 3

        # Display results with nice formatting
        print("\n" + "="*30)
        print(f"Student Report: {student_name}")
        print("-" * 30)
        print(f"Average Mark:   {average_mark:.2f}")

        # 5. If the average is greater than or equal to 40, print "Pass"
        # 6. Otherwise print "Fail"
        if average_mark >= 40:
            print("Result:         PASS")
        else:
            print("Result:         FAIL")
        print("="*30)

    except ValueError:
        print("\nError: Please enter valid numerical values for the marks.")

if __name__ == "__main__":
    main()
