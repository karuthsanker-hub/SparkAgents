import calculator

def test_calculate_gpa():
    # Test case 1: Average GPA
    grades = [3.0, 3.5, 4.0]
    assert calculator.calculate_gpa(grades) == 3.5
    
    # Test case 2: All A's
    grades = [4.0, 4.0, 4.0]
    assert calculator.calculate_gpa(grades) == 4.0
    
    # Test case 3: Empty list of grades
    grades = []
    assert calculator.calculate_gpa(grades) == 0.0

# Run the tests
if __name__ == '__main__':
    test_calculate_gpa()
