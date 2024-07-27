d = {'A':1, 'B':2}

try:
    import OK
    d.upper()
    print(d['B'])
    open('RRR.xml')
except FileNotFoundError:
    print(' RRR.txt file should exist ')
except ModuleNotFoundError:
    print(' OK MODULE IS NOT INSTALLED ')
except KeyError:
    print(d.get('C', '333'))
except Exception as e:
    print(' TRY BLOCK GOT FAILED DUE TO ', e)