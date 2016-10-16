__author__ = 'patricio_lopez'


def parentesis_balanceados(string):
    """
    Verifica que solo tenga parentesis que se cierren.
    """
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False

    return count == 0


def test_parentesis_balanceados():
    input = "g(x) = ((2^x)+5*(42/f(x)))"
    assert parentesis_balanceados(input)


def test_parentesis_desbalanceados():
    input = "(2^(2^(2)) * 4"
    assert not parentesis_balanceados(input)


def test_sin_parentesis():
    input = "4+5"
    assert parentesis_balanceados(input)


def test_input_vacio():
    input = ""
    assert parentesis_balanceados(input)


def test_parentesis_mal_cerrados():
    input = "(2+4))((6%3)"
    assert not parentesis_balanceados(input)
