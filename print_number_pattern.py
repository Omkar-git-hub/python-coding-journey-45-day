#!/usr/bin/env python3
"""
Print Number Pattern

This script prints a numeric triangle pattern where numbers start from 1 and
continue sequentially row by row.

Example output for 5 rows:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

def generate_pattern(rows: int) -> list[str]:
    """
    Generate the number pattern as a list of strings, each representing a row.

    Args:
        rows: Number of rows in the pattern.

    Returns:
        List of strings where each string contains space‑separated numbers for that row.
    """
    pattern = []
    current = 1
    for r in range(1, rows + 1):
        row_numbers = [str(num) for num in range(current, current + r)]
        pattern.append(" ".join(row_numbers))
        current += r
    return pattern


def main() -> None:
    """
    Entry point of the script. Prints a 5‑row number pattern.
    """
    rows = 5
    for line in generate_pattern(rows):
        print(line)


if __name__ == "__main__":
    main()