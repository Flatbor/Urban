immutable_var = (5, 'text', True, 0.11)
print('Immutable_var: ', immutable_var)

# immutable_var[0] = '12'
# кортеж - неизменяемая коллекция

mutable_list = list(immutable_var)
mutable_list[0] = '12'
print('Mutable_list: ', mutable_list)