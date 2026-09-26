# Programming Calculator

A command-line calculator built in Python that combines number system conversions, arithmetic operations, and bitwise operations in a single menu-driven tool.

## Overview

Programming Calculator is a terminal-based utility designed for students and developers who frequently work with number systems and low-level bit manipulation. Instead of switching between separate tools for base conversion, basic math, and bitwise logic, this program brings all three into one simple interactive menu.

## Features

### Number System Conversion

- Decimal to Binary
- Decimal to Octal
- Decimal to Hexadecimal
- Binary to Decimal
- Octal to Decimal
- Hexadecimal to Decimal

### Arithmetic Operations

- Addition
- Subtraction
- Multiplication
- Integer Division
- Modulus

### Bitwise Operations

- Bitwise AND
- Bitwise OR
- Bitwise XOR
- Bitwise NOT
- Left Shift
- Right Shift

## Other Features

- Input validation with re-prompting on invalid entries
- Divide-by-zero handling for division and modulus
- Continuous loop menu until the user chooses to exit

## Technologies Used

- Python 3

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-folder>
   ```
2. Ensure Python 3 is installed:
   ```bash
   python3 --version
   ```
3. No external dependencies are required — the project uses only Python's standard library.

## How to Run

You'll be shown a numbered menu. Enter the number corresponding to the operation you want (1–18), follow the prompts, and press Enter to continue after each result. Choose option 18 to exit.

```bash
python3 programming_calculator.py
```

## Example

```text
Enter your choice: 1
Enter number: 42
Decimal :42
Binary :0b101010
```

## Testing

Manually test each menu option (1–18) with valid inputs, invalid inputs (e.g. letters instead of numbers), and edge cases (e.g. division by zero, negative shift amounts) to confirm the program handles them gracefully.

## Project Structure

```text
├── programming_calculator.py # Main program file
└── README.md
```

## Future Enhancements

- Add support for floating-point arithmetic
- Add a GUI version
- Add calculation history/logging
- Add unit tests

## Programming Lines

### Number System Conversion

1. Decimal to Binary
2. Decimal to Octal
...
