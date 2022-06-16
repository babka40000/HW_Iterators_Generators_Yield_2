def flat_generator(list_iter):
    for list_elem in list_iter:
        for element in list_elem:
            yield element


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for elem in flat_generator(nested_list):
        print(elem)
