import math
import timeit
import tracemalloc
from Bstep_algorithm import babystep_giantstep
from Bstep_algorithm import display_top
import numpy as np

test = [15, 2, 37]
part_a = [1228035139812, 3, 2199023255867]
part_b = [259893785866906004, 3, 2305843009213699919]

#tracemalloc.start()

for i in [part_a, part_b]:
    start = timeit.default_timer()
    answer = babystep_giantstep(i[0],i[1],i[2])
    stop = timeit.default_timer()
    print(f": {i[1]}^{answer} = {i[0]} modulus {i[2]}")
    print(f"Time: {math.floor((stop - start) / 60)} minutes, {(stop-start) % 60} seconds")

#snapshot = tracemalloc.take_snapshot()
#display_top(snapshot)