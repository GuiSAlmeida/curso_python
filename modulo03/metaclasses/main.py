M = type('metaclasse', (), {})  # (name, bases = classes herdadas, namespace = atributos e métodos)

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_cls' in namespace:
            del namespace['attr_cls']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_cls = "valor A"


class B(A):
    attr_cls = "valor B"


b = B()
print(b.attr_cls)
