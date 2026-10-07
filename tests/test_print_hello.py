import pytest
from hello import say_hello

def test_say_hello(capsys):
    """Test that say_hello prints the expected greeting."""
    say_hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World"