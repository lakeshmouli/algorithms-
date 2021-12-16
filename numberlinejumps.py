

import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"
        
    
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1v1x2v2 = input().rstrip().split()

    x1 = int(x1v1x2v2[0])

    v1 = int(x1v1x2v2[1])

    x2 = int(x1v1x2v2[2])

    v2 = int(x1v1x2v2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
