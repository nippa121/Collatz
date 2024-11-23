# Collatz
Experiments in Solving Collatz (3n+1) by Indirect Proof
# Collatz Conjecture Exploration with Python

This repository contains Python code to simulate and analyze the Collatz Conjecture through computational experiments. The goal is to explore the behavior of the Collatz sequence and possibly gain insights that could contribute to an indirect proof of the conjecture.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
- [Functions](#functions)
- [Example](#example)
- [Next Steps](#next-steps)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Collatz Conjecture** is an unsolved mathematical problem that involves a simple iterative sequence:

1. **If the number is even**, divide it by 2.
2. **If the number is odd**, multiply it by 3 and add 1.

The conjecture states that no matter what positive integer you start with, the sequence will always eventually reach 1.

This script allows you to:

- Generate the Collatz sequence for a given starting number.
- Test a range of numbers to see if they reach 1 within a specified number of iterations.
- Identify numbers that do not reach 1 within the iteration limit (if any).

## Features

- **Collatz Sequence Generation**: Compute the sequence for any positive integer.
- **Range Testing**: Test multiple numbers efficiently over a specified range.
- **Customizable Iteration Limit**: Prevent infinite loops with a maximum iteration parameter.
- **Reporting**: Output numbers that do not conform to the conjecture within the given iterations.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/collatz-conjecture-exploration.git
   cd collatz-conjecture-exploration
   ```

2. **Run the Script**

   ```bash
   python collatz.py
   ```

   *(Assuming you save the provided code in a file named `collatz.py`)*

## Functions

### `collatz_sequence(n, max_iterations=10000)`

Generates the Collatz sequence starting from `n`. Stops if the sequence reaches 1 or exceeds `max_iterations`.

- **Parameters:**
  - `n` (*int*): Starting positive integer.
  - `max_iterations` (*int*): Maximum number of iterations before stopping.
- **Returns:**
  - `sequence` (*list*): The generated Collatz sequence.
  - `reached_one` (*bool*): Indicates whether the sequence reached 1.

### `test_collatz_range(start, end, max_iterations=10000)`

Tests the Collatz sequence for numbers in the range `[start, end]`. Reports numbers that do not reach 1 within `max_iterations`.

- **Parameters:**
  - `start` (*int*): Starting number of the range.
  - `end` (*int*): Ending number of the range.
  - `max_iterations` (*int*): Maximum iterations per number.

## Example

```python
def collatz_sequence(n, max_iterations=10000):
    sequence = [n]
    iterations = 0

    while n != 1 and iterations < max_iterations:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        iterations += 1

    reached_one = n == 1
    return sequence, reached_one

def test_collatz_range(start, end, max_iterations=10000):
    non_terminating_numbers = []

    for n in range(start, end + 1):
        _, reached_one = collatz_sequence(n, max_iterations)
        if not reached_one:
            non_terminating_numbers.append(n)
            print(f"Number {n} did not reach 1 within {max_iterations} iterations.")

    if not non_terminating_numbers:
        print(f"All numbers in range {start} to {end} reached 1.")
    else:
        print(f"Numbers that did not reach 1: {non_terminating_numbers}")

# Example usage:
test_collatz_range(1, 100000, max_iterations=10000)
```

This example tests all numbers from 1 to 100,000 and reports any that do not reach 1 within 10,000 iterations.

## Next Steps

To further explore the Collatz Conjecture:

- **Increase Range and Iterations**: Test larger numbers with higher iteration limits.
- **Optimize Performance**: Implement memoization or parallel processing.
- **Data Visualization**: Plot sequences or iteration counts for visual analysis.
- **Mathematical Analysis**: Investigate patterns in numbers that take longer to reach 1.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or suggestions.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add Your Feature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
