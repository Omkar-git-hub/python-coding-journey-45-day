"""
Utility module for writing data to a text file.

The primary function, :func:`write_data_to_file`, opens the specified file
in write mode (creating it if it does not exist) and writes the provided
string data to it.  The file is closed automatically using a context
manager.  The function returns ``None`` and raises any exception that
occurs during the write operation, allowing callers to handle errors
explicitly.

Typical usage:

>>> write_data_to_file('example.txt', 'Hello, world!')
>>> with open('example.txt', 'r') as f:
...     content = f.read()
...     print(content)
Hello, world!
"""

import os
from typing import Union


def write_data_to_file(filename: Union[str, os.PathLike], data: str) -> None:
    """
    Write the given string ``data`` to the file specified by ``filename``.

    Parameters
    ----------
    filename : str or os.PathLike
        The path to the file that should receive the data.  If the file
        does not exist, it will be created.  If it does exist, its
        contents will be overwritten.
    data : str
        The text to write to the file.

    Returns
    -------
    None

    Raises
    ------
    OSError
        If the file cannot be opened or written to.
    """
    # Ensure the directory exists if a relative path is provided
    dir_name = os.path.dirname(filename)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name, exist_ok=True)

    # Write data to the file using a context manager to guarantee closure
    with open(filename, "w", encoding="utf-8") as file_obj:
        file_obj.write(data)