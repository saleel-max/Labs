my_dict = {"apple": 5, "banana": 2, "cherry": 8, "date": 1}

asc_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending by values:", asc_values)

desc_values = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending by values:", desc_values)
