immutable_var = tuple([77, "Ada", False])
print(immutable_var)
print("tuple[0] = 177 TypeError: 'type' object does not support item assignment")
mutable_list = (88, "Pascal", True)
print(mutable_list)
mutable_list = 188
print(mutable_list)
