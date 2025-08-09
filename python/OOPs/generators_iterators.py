"""
generators - > they are a type of iterator, can only traverse once
"""

for i in range(78):  # generating on the fly, may be we dnt have ram for this to be stored
    print(i)


# range -> generator, once done, we cant go back

def squar(number):
    for i in range(number):
        return i ** 2


squar(3)  # -> it will give 0. in case of return, the program has ended ,and if yu again execute t ill again give 0


# lets use yield:

def squar(number):
    for i in range(number):
        yield i ** 2


a = squar(3)  # a generator object
next(a)
next(a)  # ... same way. yield has stored the local value


# yield keyword return -> return value of a function. nthing runs after that print -> prints on console and function
# continues yield -> on the fly generates -> it gives generator object, why? to save ram -> it is capable of
# generating this many numbers , when needed i can generate )

def gen(n):
    for i in range(n):
        yield i




g = gen(12345678)
print(g)

# g = gen(3)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# same is there in for loop ->
#
# for i in g:
#     print(i)

# not getting StopIteration because for loop handles that error automatically

h = "harry"  # iterable ( you can iterate)
# # print(iter(h)) -> give string iterator and then run __next__() method on that
itr = iter(h)  # made iterator from iterable


# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__()) # so on and so forth

# for char in h:
#     print(c)

# hands on

# fibonacci series till n number
def fibo(max_number):
    # initializing first 2 numbers
    p, q = 0, 1
    while p < max_number:
        yield p
        p, q = q, p + q


fib_gen = fibo(10)
for i in fib_gen:
    print(i)


