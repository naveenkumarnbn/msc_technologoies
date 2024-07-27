''' HI
1. finally block will execute both times when try block executed successfully or fail.
2. It is used to do cleanup activities(Closing File, Killing process, close remote connections, Remove log files like that...).
''' 
try:
    fh = open('3_finally.py')
    print(fh.readline())
    import re
except:
    print(' Except Block ')
else:
    print(' Else block ')
finally:
    fh.close()
    print(' FINALLY BLOCK ')


