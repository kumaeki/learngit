from io import StringIO

f=StringIO()

print(f.write("hello"))
print(f.write(" "))
print(f.write("world!"))

print(f.getvalue())


f2 = StringIO("Hello!\nHi!\nGoodbay!")
for s in f2.readlines():
    print(s.strip())
