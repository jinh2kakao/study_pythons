# def calculate_all(num1, num2):
#     """
#     Performs addition, subtraction, multiplication, and division on two numbers.
#     Returns 'division_error' if division by zero occurs.
# 
#     Args:
#         num1 (int or float): The first number.
#         num2 (int or float): The second number.
# 
#     Returns:
#         tuple: A tuple containing the results of (addition, subtraction, multiplication, division).
#                Division result will be 'division_error' if num2 is 0.
#     """
#     addition = num1 + num2
#     subtraction = num1 - num2
#     multiplication = num1 * num2
#     division = num1 / num2 if num2 != 0 else 'division_error'
#     
#     return (addition, subtraction, multiplication, division)
# 
# if __name__ == "__main__":
#     # Provided test data
#     test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
#     test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]
# 
#     print("--- Function Test Results ---")
#     print("-----------------------------")
# 
#     # Iterate through the test data and print results
#     for i, (a, b) in enumerate(zip(test_a, test_b)):
#         results = calculate_all(a, b)
#         print(f"Pair {i+1}: num1={a}, num2={b}")
#         print(f"  Addition: {results[0]}")
#         print(f"  Subtraction: {results[1]}")
#         print(f"  Multiplication: {results[2]}")
#         print(f"  Division: {results[3]}")
#         print("-" * 30)

# --- New content added as per instruction ---

def calculate_all(num1, num2):
    """
    Performs addition, subtraction, multiplication, and division on two numbers.
    Returns 'division_error' if division by zero occurs.

    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.

    Returns:
        tuple: A tuple containing the results of (addition, subtraction, multiplication, division).
               Division result will be 'division_error' if num2 is 0.
    """
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else 'division_error'
    
    return (addition, subtraction, multiplication, division)

if __name__ == "__main__":
    # Provided test data
    test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
    test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

    print("\n--- NEW Function Test Results ---")
    print("---------------------------------")

    # Iterate through the test data and print results
    for i, (a, b) in enumerate(zip(test_a, test_b)):
        results = calculate_all(a, b)
        print(f"Pair {i+1}: num1={a}, num2={b}")
        print(f"  Addition: {results[0]}")
        print(f"  Subtraction: {results[1]}")
        print(f"  Multiplication: {results[2]}")
        print(f"  Division: {results[3]}")
        print("-" * 30)
