def my_list_genorator():
    for i in range(5):
        yield i

x = [my_list_genorator()]
print(x)

print(i for i in range(5))