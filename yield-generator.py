# acumula itens a serem retornados de uma função

def simple_generator():
    x = 1
    yield x
    yield x + 1
    yield x + 2

generator_object = simple_generator()

print(generator_object)
# print(next(generator_object))
# print(next(generator_object))
# print(next(generator_object))

for i in generator_object:
    print(i)
