def check_classes():
    classes = []
    failures = []
    for i in range(3):
        grade = input(f"Enter the grade for class {i+1}: ").upper()
        classes.append(grade)
        if grade == 'F':
            failures.append(i+1)

    if failures:
        for fail in failures:
            print(f"You have failed and need to retake class {fail}")
    else:
        print("You have passed all classes!")

# Call the function to run the check
check_classes()
