import pytest
from age import print_age, AGE

def test_print_age(capsys):
    print_age()
    captured = capsys.readouterr()
    assert captured.out.strip() == f"Your age is {AGE}"}