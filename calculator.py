

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    print("Welcome to the Advanced Calculator!")
    
    operations = {
        '1': ('Addition', add),
        '2': ('Subtraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide)
    }
    
    while True:
        print("\nAvailable operations:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in operations:
            print("Invalid selection. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numerical values.")
            continue
        
        operation_name, operation_function = operations[choice]
        result = operation_function(num1, num2)
        print(f"\nResult of {operation_name} ({num1} and {num2}): {result}")

# Run the calculator function
calculator()
