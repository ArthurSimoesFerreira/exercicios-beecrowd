x01, y01, x11, y11 = map(int, input().split())
x02, y02, x12, y12 = map(int, input().split())
if x01 <= x02 <= x11 or x01 <= x12 <= x11 or  x02 <= x11 <= x12 or x02 <= x01 <= x12:
    if y01 <= y02 <= y11 or y01 <= y12 <= y11 or  y02 <= y11 <= y12 or y02 <= y01 <= y12:
        print("1")
    else:
        print("0")
else:
    print("0")