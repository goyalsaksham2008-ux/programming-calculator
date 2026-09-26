# Project Statement

## Problem Statement

Students and beginner programmers frequently need to perform number system conversions (decimal, binary, octal, hexadecimal), basic arithmetic, and bitwise operations while learning core programming and computer science concepts. These tasks are usually scattered across different tools, calculators, or manual pen-and-paper methods, making practice slow and error-prone.

There is a need for a single, lightweight command-line tool that consolidates these operations, reinforces understanding of number systems and bitwise logic, and provides instant, validated results.

## Scope of the Project

The project is a terminal-based Programming Calculator built in Python. It covers:

- Conversion between decimal, binary, octal, and hexadecimal number systems
- Standard arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Integer division
  - Modulus
- Bitwise operations:
  - AND
  - OR
  - XOR
  - NOT
  - Left shift
  - Right shift
- Input validation and graceful error handling (e.g. invalid numbers, division by zero, negative shift amounts)

The scope is limited to integer-based operations and a text-based menu interface. It does not include floating-point arithmetic, a graphical interface, or persistent storage of calculation history — these are noted as future enhancements.

## Target Users

- Computer Science / programming students learning number systems and bitwise logic
- Beginner developers who want a quick reference/calculator for base conversions and bitwise operations
- Instructors demonstrating number system concepts in a classroom setting

## High-Level Features

1. **Number System Conversion** — Convert values between decimal, binary, octal, and hexadecimal.
2. **Arithmetic Module** — Perform addition, subtraction, multiplication, integer division, and modulus on two integers.
3. **Bitwise Operations Module** — Perform AND, OR, XOR, NOT, left shift, and right shift on integers.
4. **Input Validation** — Re-prompts the user on invalid input instead of crashing.
5. **Interactive Menu** — A continuously running, numbered menu system (options 1–18) that loops until the user exits.
