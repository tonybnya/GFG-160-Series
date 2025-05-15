"""
Custom functions for testing purpose.
"""

# Functions for testing
def print_pass(func_name: str) -> None:
    """Printer for passed test."""
    print(f"{func_name}:\t Pass ✅")


def print_fail(func_name: str) -> None:
    """Printer for failed test."""
    print(f"{func_name}:\t Fail ❌")


def tester(
    func: callable,
    input_: any,
    expected: any
) -> None:
    """Tester function."""
    print(f"Expected: {expected}")
    if func(input_) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)
