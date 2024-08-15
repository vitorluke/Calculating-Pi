from math import sqrt

precisão = 100000000
r = 0
soma1 = 0
soma2 = 0

while r < precisão:
    x1 = 1/precisão * r
    x2 = 1/precisão * (r+1)
    y1 = sqrt(1 -((x1)**2))
    y2 = sqrt(1 -((1/precisão * (r+1))**2))
    r += 1
    soma1 += x1*y2
    soma2+= y1*x2

Pi = (sqrt((soma1 - soma2)**2)/2)*4
print(Pi)