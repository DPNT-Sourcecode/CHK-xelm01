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


def test_checkout_r3():
    assert checkout("F") == 10
    assert checkout("FF") == 20
    assert checkout("FFF") == 20
    assert checkout("FFFF") == 30
    assert checkout("FFFFF") == 40
    assert checkout("FFFFFF") == 40


def test_checkout_r4():
    assert checkout("G") == 20
    assert checkout("H") == 10
    assert checkout("I") == 35
    assert checkout("J") == 60
    # assert checkout("K") == 80
    assert checkout("K") == 70
    assert checkout("L") == 90
    assert checkout("M") == 15
    assert checkout("N") == 40
    assert checkout("O") == 10
    assert checkout("P") == 50
    assert checkout("Q") == 30
    assert checkout("R") == 50
    # assert checkout("S") == 30
    assert checkout("S") == 20
    assert checkout("T") == 20
    assert checkout("U") == 40
    assert checkout("V") == 50
    assert checkout("W") == 20
    # assert checkout("X") == 90
    assert checkout("X") == 17
    # assert checkout("Y") == 10
    assert checkout("Y") == 20
    # assert checkout("Z") == 50
    assert checkout("Z") == 21

    assert checkout("HHHHH") == 45
    assert checkout("HHHHHH") == 55
    assert checkout("HHHHHHHHHH") == 80
    assert checkout("HHHHHHHHHHHHHHH") == 125

    # assert checkout("KK") == 150
    # assert checkout("KKK") == 230
    # assert checkout("KKKK") == 300
    assert checkout("KK") == 120
    assert checkout("KKK") == 190
    assert checkout("KKKK") == 240

    assert checkout("NNN") == 120
    assert checkout("NNNM") == 120
    assert checkout("NNNMM") == 135

    assert checkout("PPPPP") == 200
    assert checkout("PPPPPP") == 250

    assert checkout("QQQ") == 80
    assert checkout("QQQQ") == 110
    assert checkout("QQQQQQ") == 160

    assert checkout("RRR") == 150
    assert checkout("RRRQ") == 150
    assert checkout("RRRQQ") == 180

    assert checkout("UUU") == 120
    assert checkout("UUUU") == 120
    assert checkout("UUUUU") == 160

    assert checkout("VV") == 90
    assert checkout("VVV") == 130
    assert checkout("VVVV") == 180
    assert checkout("VVVVV") == 220


def test_checkout_r5():
    assert checkout("STXYZ") == 82
    assert checkout("STXYZZ") == 90
    assert checkout("XZZZ") == 62
    assert checkout("SSSZZZ") == 90


