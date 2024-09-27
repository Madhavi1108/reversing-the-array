#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    list_arr = []
    for i in range(0, n):
        list_arr.append(arr[n - i - 1])

    string = " ".join(str(i) for i in list_arr)
    print(string)

    
