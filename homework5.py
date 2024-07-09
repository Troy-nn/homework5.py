immutable_var = ('ocean', 1005, False, 'work')
print(immutable_var)
# immutable_var[0] = 'beach' - данная операция невозможна, т.к. элементы кортежа не могут подлежать изменению, в отличие от списка
mutable_list = ['ocean', 1005, False, 'work']
mutable_list[0] = 'beach'
print(mutable_list)
