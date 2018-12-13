import struct,base64

#print(struct.pack('>I', 10240099))
#print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

with open("C:\\Users\\xiong_yi\\Desktop\\test\\pythontest.bmp","br") as f:
    fb64 =base64.b64encode(f.read())
    print(fb64)
    fb = base64.b64decode(fb64)
    r = struct.unpack("<ccIIIIIIHH",fb[:30])

rd = {"width":r[6],"height":r[7],"color":r[9]}
print(rd)