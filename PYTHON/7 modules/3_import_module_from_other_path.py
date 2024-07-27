'''
1. To import module from another path we should add module path to sys.path list
2. sys is a python pre define module
'''
import sys

sys.path.append(r'C:\INSTITUTE_COURSES\INST\2_ONLINE_CLASS\1_PYTHON\7 modules\ONE')

import RRR

print(RRR.NAME)

RRR.mul()


