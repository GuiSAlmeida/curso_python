def master(fn):  # função decoradora
    def slave(*args, **kwargs):
        print('decorada')
        fn(*args, **kwargs)

    return slave


@master  # decorador
def hello():
    print('Fala oi')


@master
def outra_fn(msg):
    print(msg)


outra_fn('gui')
