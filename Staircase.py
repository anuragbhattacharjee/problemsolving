#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i = 1 
    while i <= n:
        j = 0
        k = n-i
        while j < k :
            print(' ', end='')
            j += 1
        while k < n:
            print('#', end='')
            k += 1
        i += 1
        print('\r')


if __name__ == '__main__':
    n = int(input())

    staircase(n)
