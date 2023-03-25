# Выведите на экран все уникальные гео-ID из значений словаря ids.
# Т.е. список вида [213, 15, 54, 119, 98, 35]


def get_list_unique(dict_):
    ids_list1 = []
    ids_set = set()

    for i in ids:
        ids_list1.append(ids[i])

    for i in range(len(ids_list1)):
        for j in ids_list1[i]:

            ids_set.add(j)

    ids_list2 = list(ids_set)

    return ids_list2



ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

print(get_list_unique(ids))
