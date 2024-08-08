# Python Test Driven Development

This project focuses on Test-Driven Development (TDD) in Python. The primary objective is to write Python functions and create test cases that validate the functions' correctness. This approach helps ensure that your code works as expected before deploying it.

## Project Structure

- `0-add_integer.py`: Python module that defines the `add_integer` function.
- `tests/0-add_integer.txt`: Text file containing test cases for the `add_integer` function.

## Requirements

- Python 3.8.5
- Ubuntu 20.04 LTS
- All code files should be executable.
- Follow PEP 8 style guidelines.
- All test files should be in the `tests` directory.

## Usage

### Running the Function

You can use the `add_integer` function directly by importing it:

```python
from 0-add_integer import add_integer

print(add_integer(2, 3))  # Output: 5
