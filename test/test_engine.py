from micrograd.engine import Value


def test_sanity_check():
    x = Value(-4.0)
    z = 2 * x + 2 + x

    z.backward()

    assert z.data == -10.0
    assert x.grad == 3.0
