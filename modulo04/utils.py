def size_format(size):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo:
        ext = 'B'
    elif size < mega:
        size /= kilo
        ext = 'K'
    elif size < giga:
        size /= mega
        ext = 'M'
    elif size < tera:
        size /= giga
        ext = 'G'
    elif size < peta:
        size /= tera
        ext = 'T'
    else:
        size /= peta
        ext = 'P'

    size = round(size, 2)
    return f'{size}{ext}'.replace('.', ',')
