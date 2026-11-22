"""Read Data From a File

This module provides a simple utility function to read the entire
contents of a text file and return it as a string. If the file does
not exist, the function returns ``None`` instead of raising an
exception, allowing callers to handle the missing‑file case
gracefully.

Typical usage::

    content = read_data_from_file('example.txt')
    if content is None:
        print('File not found')
    else:
        print(content)
"""

from __future__ import annotations


def read_data_from_file(file_path: str) -> str | None:
    """
    Read the entire contents of the file located at *file_path*.

    Parameters
    ----------
    file_path: str
        Path to the file to be read.

    Returns
    -------
    str | None
        The file contents as a string if the file exists; otherwise
        ``None``.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    # Simple manual test when the module is executed directly.
    import sys

    if len(sys.argv) != 2:
        print("Usage: python read_data_from_file.py <path_to_file>")
        sys.exit(1)

    path = sys.argv[1]
    data = read_data_from_file(path)
    if data is None:
        print(f"File not found: {path}")
    else:
        print(data)