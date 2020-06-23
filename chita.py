# we can easily speed up the execution time by playing around with our code; here i have used numexpr library instead of numpy to execute arithmetic expressions



import timeit
import numexpr as ne
import pandas as pd
code_to_test = """
import numpy as np
from timeit import Timer
import numexpr as ne


def haversine(lat1, lon1, lat2, lon2):
    radius = 100
    lat1, lon1, lat2, lon2 = map(np.deg2rad, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    # typical expression writings: f = np.sin(dlat/2)**2 + ne.evaluate("cos(lat1)") * np.cos(lat2) * np.sin(dlon/2)**2
    f = ne.evaluate("sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2")
    g = 2 * np.arcsin(np.sqrt(f))

    distance = radius * g
    print(distance)
    return distance

lat2 = np.array(range(100000))
lon2 = np.array(range(100000))


haversine(65, 70, lat2, lon2)
"""

print(timeit.timeit(code_to_test, number=100)/100)
