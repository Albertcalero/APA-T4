"""
Albert Calero
"""

class Aleat:
    """
    Clase iteradora que implementa un Generador Lineal Congruente (LGC).

    Genera una secuencia de números pseudoaleatorios basados en la fórmula:
    x_{n + 1} = (a * x_n + c) % m

    Atributos:
        m (int): Módulo del generador.
        a (int): Multiplicador.
        c (int): Incremento.
        x (int): Estado actual o semilla de la secuencia.

    Métodos:
        __next__(): Devuelve el siguiente número pseudoaleatorio.
        __iter__(): Devuelve el propio objeto iterador.
        __call__(x0): Reinicia el estado del generador con una nueva semilla.

    Ejemplos de uso (Doctests):

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        """
        Inicializa el generador. Los argumentos son obligatoriamente por clave.
        """
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __iter__(self):
        """Devuelve el iterador."""
        return self

    def __next__(self):
        """Calcula y devuelve el siguiente número de la secuencia LGC."""
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x0, /):
        """
        Reinicia la secuencia usando una nueva semilla.
        El argumento x0 es forzosamente posicional.
        """
        self.x = x0


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora que implementa un Generador Lineal Congruente (LGC).

    Permite reiniciar la secuencia en cualquier momento enviando un nuevo valor
    de semilla mediante el método .send().

    Argumentos (todos obligatorios por clave):
        m (int): Módulo. Por defecto el de POSIX (2**48).
        a (int): Multiplicador. Por defecto el de POSIX.
        c (int): Incremento. Por defecto el de POSIX.
        x0 (int): Semilla inicial. Por defecto 1212121.

    Ejemplos de uso (Doctests):

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        recibido = yield x
        if recibido is not None:
            x = recibido


if __name__ == "__main__":
    import doctest
    doctest.testmod()