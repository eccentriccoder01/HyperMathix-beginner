def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        return "Error: Division by zero is not allowed"
    return x / y

def display_menu():
    """Display calculator menu"""
    print("\n=== CALCULATOR ===")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("==================")

def get_numbers():
    """Get two numbers from user input"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers")
        return None, None

def main():
    """Main calculator function"""
    print("Welcome to the Calculator CLI App!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-5): ")
            
            if choice == '5':
                print("Thank you for using the calculator. Goodbye!")
                break
            
            if choice in ['1', '2', '3', '4']:
                num1, num2 = get_numbers()
                
                if num1 is None or num2 is None:
                    continue
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")
                
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")
                
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"Result: {num1} × {num2} = {result}")
                
                elif choice == '4':
                    result = divide(num1, num2)
                    if isinstance(result, str):  # Error message
                        print(result)
                    else:
                        print(f"Result: {num1} ÷ {num2} = {result}")
            
            else:
                print("Error: Invalid choice. Please select 1-5.")
                
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()