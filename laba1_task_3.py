# TODO Найдите количество книг, которое можно разместить на дискете
v = 1.44*1024*1024
n_page, n_lines, n_symbol = 100, 50, 25
total = n_page * n_lines * n_symbol
ans = round(v//(total * 4))
print("Количество книг, помещающихся на дискету:", ans)
