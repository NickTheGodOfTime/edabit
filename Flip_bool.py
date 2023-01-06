def flip_bool(b):
    if b == "True" or "0":
        return "1"
    else:
        return "0"
    



a = flip_bool(True)
print(a)
a = flip_bool(False)
print(a)
a = flip_bool(1)
print(a)
a = flip_bool(0)
print(a)