from .hello_solution import hello


def test_hello_name():
    assert hello("Raz") == "Hello, Raz!"
