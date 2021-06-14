try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except ImportError:
    raise


from pacote1.modulo1 import variavel1
from pacote2.modulo2 import variavel2

print(variavel1, variavel2)
