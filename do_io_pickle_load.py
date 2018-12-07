import pickle

f = open('D:\\GIT_other\\learngit\\test\\test.txt','rb')

print(pickle.load(f))

f.close()
