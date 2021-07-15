"""Titulo do módulo

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nam rhoncus posuere risus ut viverra. Cras sollicitudin cursus augue at congue.
Quisque scelerisque aliquet sem at pellentesque.
Ut eu ex mattis magna placerat sollicitudin.
Vestibulum id porttitor dolor, ac auctor ipsum.
Vestibulum quis libero nec arcu vulputate efficitur.
Etiam varius turpis ut eros pharetra pulvinar. Vivamus nibh nunc,
fermentum et pretium porttitor, blandit sit amet massa.
"""

variavel = 'valor'


def funcao(x, y):
    """Soma x e y"""
    return x + y

def multiplica(x,y,z=None):
    """Multiplica x,y,z

    fermentum et pretium porttitor, blandit sit amet massa.
    """
    if not z:
        return x * y
    else:
        return x * y * z
