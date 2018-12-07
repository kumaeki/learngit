import pickle

d = dict(name="kuma",age="32",score="80")

f = open('D:\\GIT_other\\learngit\\test\\test.txt','wb')

pickle.dump(d,f)

f.close()
