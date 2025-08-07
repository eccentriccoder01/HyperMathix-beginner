# Calculator CLI App

A simple command-line calculator application written in Python that performs basic arithmetic operations.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, and division
- **Interactive Menu**: User-friendly command-line interface
- **Error Handling**: Handles division by zero and invalid input
- **Input Validation**: Ensures users enter valid numbers
- **Graceful Exit**: Clean exit options and interrupt handling

## Requirements

- Python 3.x

## Installation

1. Clone or download the calculator script
2. Ensure Python 3.x is installed on your system
3. No additional dependencies required

## Usage

Run the calculator from the command line:

```bash
python calculator.py
```

### Menu Options

When you run the application, you'll see the following menu:

```
=== CALCULATOR ===
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
==================
```

### How to Use

1. **Start the application** by running the Python script
2. **Select an operation** by entering a number (1-5)
3. **Enter two numbers** when prompted
4. **View the result** displayed on screen
5. **Continue** with more calculations or **exit** by selecting option 5

### Example Session

```
Welcome to the Calculator CLI App!

=== CALCULATOR ===
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
==================
Enter your choice (1-5): 1
Enter first number: 10
Enter second number: 5
Result: 10.0 + 5.0 = 15.0
```

## Functions

The calculator includes the following functions:

- `add(x, y)` - Adds two numbers
- `subtract(x, y)` - Subtracts second number from first
- `multiply(x, y)` - Multiplies two numbers
- `divide(x, y)` - Divides first number by second (with zero-division protection)
- `display_menu()` - Shows the operation menu
- `get_numbers()` - Handles user input and validation
- `main()` - Main application loop

## Error Handling

The calculator handles several types of errors:

- **Division by Zero**: Returns an error message instead of crashing
- **Invalid Input**: Prompts user to enter valid numbers
- **Invalid Menu Choice**: Asks user to select from valid options (1-5)
- **Keyboard Interrupt**: Gracefully exits when Ctrl+C is pressed

## Technical Details

- Written in Python 3
- Uses built-in functions only (no external libraries)
- Supports floating-point arithmetic
- Command-line interface using `input()` and `print()`

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for any improvements.