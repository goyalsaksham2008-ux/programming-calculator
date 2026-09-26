def show_menu():

print("\n" + "=" * 50)

print("Programming lines")

print("=" * 50)

print("\nNumber System Conversion")

print("1. Decimal to Binary")

print("2. Decimal to Octal")

print("3. Decimal to Hexadecimal")

print("4. Binary to Decimal")

print("5. Octal to Decimal")

print("6. Hexadecimal to Decimal")

print("\nArithmetic Operations")

print("7. Addition")

print("8. Subtraction")

print("9. Multiplication")

print("10. Integer division")

print("11. Modulus")

print("\nBitwise Operations")

print("12.. )

Print("13. Bitwise OR")

print("14. Bitwise XOR")

print("15. Bitwise NOT")

print("16. Left Shift")

print("17. Right Shift")

print("\n18. EXIT")

print("=" * 50)

def get_decimal():

while True:

try:

return int(input("Enter number: "))

except ValueError:

print("Invalid input. Please enter an integer number.")

def get_binary():

while

value = input("Enter binary number: ")

if value.startswith("-"):

digits = value[1:]

digits = value

if digits and all(digit in "01" for digit, in digits):

return int(value, 2)

print("Invalid number.")

def get_octal():

while

value = input("Enter octal number: ")

try:

return int(value, 8)

except ValueError:

print("Invalid octal number.")

def get_hexadecimal():

while True:

value = input("Enter hexadecimal number: ")

try:

return int(value, 16)

except ValueError:

hexadecimal number.")

def decimal_to_binary():

number = get_decimal()

print("\nDecimal :" number)

print("Binary  :" bin(number))

def decimal_to_octal():

number = get_decimal()

print("\nDecimal :" number)

print("Octal   :" oct(number))

def decimal_to_hexadecimal():

number = get_decimal()

print("\nDecimal     :" number)

print("Hexadecimal :" hex(number).upper())

def binary_to_decimal():

number = get_binary()

print("\nBinary  :" bin(number))

print("Decimal :" number)

def octal_to_decimal():

number = get_octal()

print("\nOctal   :" oct(number))

print("Decimal :" number)

def hexadecimal_to_decimal():

number = get_hexadecimal()

print("\nHexadecimal :" hex(number).upper())

print("Decimal     :" number)

get_two_numbers():

while True:

try:

a = int(input("Enter first number: "))

b = int(input("Enter second number: "))

return a, b

except ValueError:

print("Invalid input. Please enter integers.")

def addition():

a b = get_two_numbers()

print("\nResult:" a + b)

subtraction():

a b = get_two_numbers()

print("\nResult:" a. B)

def multiplication():

a b = get_two_numbers()

print("\nResult:" a * b)

def integer_division():

a b = get_two_numbers()

if b == 0:

print("\nError: Cannot divide by zero.")

return

print("\nResult:" a // b)

modulus():

a b = get_two_numbers()

if b == 0:

print("\nError: Cannot use zero as divisor.")

return

print("\nResult:" a % b)

def bitwise_and():

a b = get_two_numbers()

print("\nResult:" a & b)

def bitwise_or():

a b = get_two_numbers()

print("\nResult:" a | b)

def bitwise_xor():

a b = get_two_numbers()

print("\nResult:" a ^ b)

def bitwise_not():

number = get_decimal()

print("\nResult:" ~number)

def left_shift():

number = get_decimal()

while True:

try:

positions = int(input("Enter the number of positions: "))

if positions < 0:

print("Shift amount cannot be negative.")

continue

break

except ValueError:

print("Enter an integer.")

print("\nResult:" number << positions)

def right_shift():

number = get_decimal()

while True:

try:

positions = int(input("Enter the number of positions: "))

if positions < 0:

print("Shift amount cannot be negative.")

continue

break

except ValueError:

print("Enter a real integer.")

print("\nResult:" number >> positions)

def main():

while True:

show_menu()

choice = input("\nEnter your choice: ")

if choice == "1":

decimal_to_binary()

elif choice == "2":

decimal_to_octal()

elif choice == "3":

decimal_to_hexadecimal()

elif choice == "4":

binary_to_decimal()

elif choice == "5":

octal_to_decimal()

elif choice == "6":

hexadecimal_to_decimal()

elif choice == "7":

addition()

elif choice == "8":

subtraction()

elif choice == "9":

multiplication()

elif choice == "10":

integer_division()

elif choice == "11":

modulus()

elif choice == "12":

bitwise_and()

elif choice == "13":

bitwise_or()

elif choice == "14":

, bitwise_xor()

elif choice == "15":

bitwise_not()

elif choice == "16":

left_shift()

elif choice == "17":

right_shift()

elif choice == "18":

print("\nThank you for using Programming Calculator!")

break

else:

print("\nInvalid choice. Please choose from 1 to 18.")

input("\nPress Enter to continue")

if __name__ == "__main__":

main()