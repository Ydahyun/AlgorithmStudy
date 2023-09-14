# 최초의 알고리즘이라고 알려진 유클리드의 최대공약수를 찾는 알고리즘이다.


def Euclid(a, b):
    if b == 0:
        return a
    else:
        return Euclid(b, a % b)

a = 24
b = 14

p = Euclid(a, b)
print(p)
