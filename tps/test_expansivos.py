def expand(arreglo):
  salida = []
  numero = arreglo[0]
  cantidad = 1

  for i in range(1, len(arreglo)):
      if arreglo[i] == numero:
        cantidad += 1
      else:
        salida.append(cantidad)
        salida.append(numero)

        numero = arreglo[i]
        cantidad = 1
  salida.append(cantidad)
  salida.append(numero)
  return salida

def test_expand():
    assert expand([1, 1, 2, 1, 1]) == [2, 1, 1, 2, 2, 1]

def test_expand_dos_iguales():
    assert expand([1, 1]) == [2, 1]

def test_expand_tres_iguales():
    assert expand([1, 1, 1]) == [3, 1]