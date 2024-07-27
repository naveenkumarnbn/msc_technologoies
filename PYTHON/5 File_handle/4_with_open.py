# reading names.txt and writing into names_write.txt

with open('names.txt') as fr, open('WRITE.txt', 'w') as fw:
    fw.write(fr.read())








