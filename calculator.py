def calculate_gpa(grades):
    if not grades:
        return 0.0
    
    total = sum(grades)
    gpa = total / len(grades)
    return gpa
