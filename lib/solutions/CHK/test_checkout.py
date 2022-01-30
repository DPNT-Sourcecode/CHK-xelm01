from .checkout_solution import checkout


def test_checkout():
    assert checkout("") == 0
    assert checkout("A") == 50
    assert checkout("B") == 30
    assert checkout("C") == 20
    assert checkout("D") == 15
    assert checkout("a") == -1
    assert checkout("-") == -1
    assert checkout("ABCa") == -1
    assert checkout("AxA") == -1
    assert checkout("ABCD") == 115
    assert checkout("A") == 50
    assert checkout("AA") == 100
    assert checkout("AAA") == 130
    assert checkout("AAAA") == 180
    # assert checkout("AAAAA") == 230
    # assert checkout("AAAAAA") == 260
    assert checkout("AAAAA") == 200
    assert checkout("AAAAAA") == 250
    assert checkout("B") == 30
    assert checkout("BB") == 45
    assert checkout("BBB") == 75
    assert checkout("BBBB") == 90
    assert checkout("ABCDABCD") == 215
    assert checkout("BABDDCAC") == 215
    assert checkout("AAABB") == 175
    # assert checkout("ABCDCBAABCABBAAA") == 505
    assert checkout("ABCDCBAABCABBAAA") == 495


def test_checkout_r2():
    assert checkout("E") == 40
    assert checkout("EE") == 80
    assert checkout("EEB") == 80
    assert checkout("EEBB") == 110
    assert checkout("EEEBB") == 150
    assert checkout("EEEEBB") == 160
    assert checkout("AAAAAAAA") == 330
