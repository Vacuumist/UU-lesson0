def apply_all_func(int_list, *functions):
     result = {}
     for f in functions:
          result.update({f.__name__: f(int_list)})
     return result

def list_power(num_list, power):
     result = []
     for i in num_list:
          result.append(i ** power)
     return result

def cube(num_list):
     return list_power(num_list, 3)

def sqrt(num_list):
     return list_power(num_list, 0.5)

def cuberoot(num_list):
     return list_power(num_list, 1 / 3)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

print(apply_all_func([1, 2, 3, 4], cube, sqrt, cuberoot))
