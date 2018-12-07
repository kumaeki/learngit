#try:
#    f = open("do_class_type.py","r");
#    print(f.read())
#finally:
#    if f:
#        f.close()


with open("do_class_type.py","rb") as f:
    for l in f.readlines():
        print(l)


with open("do_class_type.py","a") as fl:
    fl.write("hello world")
