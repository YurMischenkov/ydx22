x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())


def peres(x1, y1, w1, h1, x2, y2):
    if (x2 >= x1 and x2 <= (x1 + w1)) and (y2 >= y1 and y2 <= (y1 + h1)):
        return True
    else:
        return False
    
    
m = []
m.append(peres(x1, y1, w1, h1, x2, y2))
m.append(peres(x1, y1, w1, h1, x2 + w2, y2))
m.append(peres(x1, y1, w1, h1, x2, y2 + h2))
m.append(peres(x1, y1, w1, h1, x2 + w2, y2 + h2))
m.append(peres(x2, y2, w2, h2, x1, y1))
m.append(peres(x2, y2, w2, h2, x1 + w1, y1))
m.append(peres(x2, y2, w2, h2, x1, y1 + h1))
m.append(peres(x2, y2, w2, h2, x1 + w1, y1 + h1))
if True in m:
    print('YES')
else:
    print('NO')
