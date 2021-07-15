class A:
    """
    Padrão singleton, onde a classe criará apenas um único objeto
    os seguintes serão cópias do mesmo objeto.
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_exist'):
            cls._exist = object.__new__(cls)
        return cls._exist

    def __init__(self):
        print('__init__')

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print(key, value)


a = A()
b = A()
c = A()
# print(f'{id(a)} | {id(b)} | {id(c)}')
a(1, 2, 3, nome='Gui')
a.nome = 'Deia'
