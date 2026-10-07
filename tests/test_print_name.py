import pytest
from print_name import print_name

def test_print_name(capsys):
    print_name()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Your Name"