fr = open('fil1.txt','r')
w = len(fr.read().split())
#print(w)   here output is 9 (it counted num of words)..
chrs = len(open('fil1.txt').read())
# print(chrs)   here output is 34.(it count no.of charecters in file).
num_lines = len(open('fil1.txt').readlines())
# print(num_lines)  here output is 3..(it count no of lines)

dic = {'lines':num_lines,'words':w,'charecters':chrs}

print(dic)

print(dic.keys())

print(dic.values())


fr.close()