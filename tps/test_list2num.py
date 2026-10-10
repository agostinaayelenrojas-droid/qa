
def list2num(arreglo):
    numero = 0
    for cifra in arreglo:
        numero = numero * 10 + cifra
    return numero


def test_list2num_dos_unos():
    assert list2num([1, 1]) == 11


def test_list2num_1211():
    assert list2num([1, 2, 1, 1]) == 1211


def test_list2num_123():
    assert list2num([1, 2, 3]) == 123
