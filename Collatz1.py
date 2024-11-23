def collatz_sequence(n, max_iterations=10000):
    """
    Generates the Collatz sequence starting from n.
    Stops if the sequence reaches 1 or exceeds max_iterations.
    Returns the sequence and a boolean indicating if it reached 1.
    """
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
    """
    Tests the Collatz sequence for numbers in the range [start, end].
    Reports numbers that do not reach 1 within max_iterations.
    """
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
