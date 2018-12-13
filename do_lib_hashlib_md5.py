import hashlib

md5 = hashlib.md5()
md5.update("how to use md5 in python hashlib?".encode("utf-8"))
r1 = md5.hexdigest()
print(r1)

md5_2 = hashlib.md5()
md5_2.update("how to use md5 in ".encode("utf-8"))
md5_2.update("python hashlib?".encode("utf-8"))
r2=md5_2.hexdigest()
print(r2)