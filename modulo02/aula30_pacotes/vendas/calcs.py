from vendas.format import preco


def aumento(valor, porcentagem, formata=False):
    res = valor + (valor * (porcentagem / 100))
    if formata:
        return preco.real(res)
    return res


def reducao(valor, porcentagem, formata=False):
    res = valor - (valor * (porcentagem / 100))
    if formata:
        return preco.real(res)
    return res
