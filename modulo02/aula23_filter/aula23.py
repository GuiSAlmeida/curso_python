from dados import produtos, pessoas, nums

# novos_nums = [num for num in nums if num > 5]
novos_nums = filter(lambda num: num > 5, nums)
print(list(novos_nums))

novos_produtos = filter(lambda p: p['preço'] > 50, produtos)
print(list(novos_produtos))

novas_pessoas = filter(lambda pessoa: pessoa['idade'] > 18, pessoas)
print(list(novas_pessoas))
