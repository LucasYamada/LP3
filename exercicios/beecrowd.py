n = int(input())

_in = []
_out = []

for _ in range(n):
    x = int(input())
    if x in range(10,20):
        _in.append(x)
    else:
        _out.append(x)

print(len(_in),"in")
print(len(_out),"out")