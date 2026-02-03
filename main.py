import calculator

def main():
    grades_input = input("Enter grades separated by spaces: ")
    grades = list(map(float, grades_input.split()))
    
    gpa = calculator.calculate_gpa(grades)
    print(f"GPA: {gpa}")
    
    if calculator.check_risk(gpa):
        print("Alert: GPA is below 3.0")

if __name__ == '__main__':
    main()
