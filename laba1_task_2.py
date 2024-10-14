list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

average = len(list_players)//2

first = list_players[average:]
second = list_players[:average]

print(second)
print(first)