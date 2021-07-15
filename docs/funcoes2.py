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


def multiplica(x, y, z=None):
    """
    Multiplica x,y,z
    :param x: número
    :type x: int or float
    :param y: número
    :type y: int or float
    :param z: número
    :type z: int, float or Nome
    :return: Soma entre x, y e z
    :rtype: int or float
    """
    if not z:
        return x * y
    else:
        return x * y * z
