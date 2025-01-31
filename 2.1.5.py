def check():
    classes = ["math", "english", "science"]
    failures = []
    for i in range(3):
        grade = input(f"Enter the grade for class {classes[i]}: ").upper()
        if grade == 'F':
            failures.append(classes[i])
    
    if failures:
        for fail in failures:
            print(f"You have failed and need to retake {fail}")
    else:
        print("You have passed all classes!")

check()
