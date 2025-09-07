list1 = [x * x for x in range(10)]
print("sum1", sum(list1))

gen1 = (x * x for x in range(10))
print(gen1)
print("sum2", sum(gen1))
print("sum3", sum(gen1))

def squares(n):
    for x in range(n):
        yield x * x

gen2 = squares(10)
print(gen2)
print("sum4", sum(gen2))

sum5 = 0
for x in squares(10):
    sum5 += x
print("sum5", sum5)