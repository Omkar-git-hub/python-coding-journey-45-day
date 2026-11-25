"""
count_lines_in_file.py

This module provides a simple utility to count the number of lines in a given text file.
It demonstrates basic file handling, exception handling, and a small command-line interface.

Usage:
    python count_lines_in_file.py <path_to_file>

The script will print the number of lines in the specified file or an error message if the file
cannot be accessed.
"""

import sys
from pathlib import Path


def count_lines_in_file(file_path: str | Path) -> int:
    """
    Count the number of lines in the specified file.

    Parameters
    ----------
    file_path : str or pathlib.Path
        Path to the file whose lines are to be counted.

    Returns
    -------
    int
        The number of lines in the file.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    PermissionError
        If the file cannot be accessed due to permission issues.
    """
    path = Path(file_path)

    # Ensure the file exists before attempting to read
    if not path.is_file():
        raise FileNotFoundError(f"No such file: '{file_path}'")

    # Read the file and count lines
    with path.open("r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def _main(argv: list[str] | None = None) -> None:
    """
    Command-line interface for counting lines in a file.

    Parameters
    ----------
    argv : list[str] or None
        List of command-line arguments. If None, sys.argv is used.
    """
    if argv is None:
        argv = sys.argv

    if len(argv) != 2:
        print("Usage: python count_lines_in_file.py <path_to_file>")
        sys.exit(1)

    file_path = argv[1]

    try:
        line_count = count_lines_in_file(file_path)
        print(f"Number of lines in '{file_path}': {line_count}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except PermissionError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    _main()