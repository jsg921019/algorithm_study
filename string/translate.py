# make table using maketrans

# method 1: dictionary

table = str.maketrans({'a':'A', # normal
                        98:'B', # from ordinal
                        'c': 67, # to ordinal
                        'd' : 'D~~', # to string of arbitary length
                        'e' : None}) # delete

print('abcdef'.translate(table))

# method 2 : using two equal length strings and one string for deletion

table = str.maketrans('abcde', 'ABCDE', 'fg')

print('abcdef'.translate(table))