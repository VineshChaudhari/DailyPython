# Student Grade Calculator (if-elif-else)

def calculate_result():
    marks = []
    for i in range(5):
        m = int(input(f"Enter marks for course {i+1}: "))
        marks.append(m)
    
    passing = all(m >= 40 for m in marks)
    
    if not passing:
        print("Result: FAIL")
    else:
        aggregate = sum(marks) / 5
        if aggregate > 75:
            print(f"Aggregate: {aggregate:.2f}% | Grade: Distinction")
        elif 60 <= aggregate < 75:
            print(f"Aggregate: {aggregate:.2f}% | Grade: First Division")
        elif 50 <= aggregate < 60:
            print(f"Aggregate: {aggregate:.2f}% | Grade: Second Division")
        elif 40 <= aggregate < 50:
            print(f"Aggregate: {aggregate:.2f}% | Grade: Third Division")