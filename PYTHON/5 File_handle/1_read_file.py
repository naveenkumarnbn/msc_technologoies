
fh = open('names.txt', 'r')

## To open a file from another path
#fw = open(r'C:\Users\smellamp\RRR.txt', 'r')

## Using read we can read entire file data and return in string format
print(fh.read())

## Using readline we can read only one line and return in string format
print(' 1 :: ', fh.readline())

#print(' 2 :: ', fh.readline())


## Using readlines we can read total lines in a file and  return in list format
print(' READ LINES 1 ', fh.readlines())

# To close a file
fh.close()
