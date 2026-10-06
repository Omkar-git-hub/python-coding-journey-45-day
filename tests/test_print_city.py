import io
import sys
import pytest

from hello import print_city

def test_print_city_output(capsys):
    # Capture the output of print_city
    print_city()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Your city is San Francisco"