import math
import numpy as np
import tracemalloc
import os
import linecache
import csv
import pandas as pd


def binary_search(List, value, lo=0, hi=None):
    if hi is None:
        hi = len(List)
    while lo < hi:
        mid = (lo+hi)//2
        midval = int(List[mid][0])
        if midval < value:
            lo = mid+1
        elif midval > value:
            hi = mid
        else:
            return mid
    return -1

def display_top(snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))

def modulus(a,b):
    return a-math.floor(a/b)*b

# The main function to sort an array of given size

def binary_search(List, value, lo=0, hi=None):
    if hi is None:
        hi = len(List)
    while lo < hi:
        mid = (lo+hi)//2
        midval = int(List[mid][0])
        if midval < value:
            lo = mid+1
        elif midval > value:
            hi = mid
        else:
            return mid
    return -1
def babystep_giantstep(B,a,P):
    t = math.floor(math.sqrt(P))
    print('t: ', t)

    #giant step
    g_step = np.zeros(t)
    g_step[0] = a % P
    g_s_ind = np.arange(1, t+1)
    for g in range(1,t):
        g_step[g] = pow(int(g_step[0] * g_step[g - 1]), 1, P)
    print('giant step complete')

    #baby step
    b_step = np.zeros(t)
    b_s_ind = np.arange(0, t+1)
    #fermat's little theorem, P is prime
    inv = pow(a,P-2, P)
    inv_t_mod = pow(inv, t, P)
    print(f"inv: {inv}, inv^t mod P: {inv_t_mod}")
    for y in range(t):
        if y == 0:
            b_step[y] = B % P
        else:
            b_step[y] = pow(int(b_step[y - 1]) * inv_t_mod, 1, P)
    print('Baby step complete')

    #Create sorted lists that will help us search through all of the possibilities faster using binary search
    #For binary search, we'll create a 2-d list that holds the baby step and giant step values
    #Alongside the powers of a and a inverse so that the final power can be extracted after sorting
    bs = np.zeros((t, 2))
    bs[0, :] = [b_step[0], b_s_ind[0]]

    for cc in range(1, t):
        bs[cc, :] = [b_step[cc], b_s_ind[cc]]

    indices = np.argsort(bs[:, 0])
    bs = bs[indices]
    print('bs sorted')

    #search giant step
    for z in range(t):
        #search baby step

        x = binary_search(bs, int(g_step[z]))
        if x > -1:
            print(z)
            print(int(bs[x][1]))
            ans = (z + 1) + (t * int(bs[x][1]))
            return(ans)