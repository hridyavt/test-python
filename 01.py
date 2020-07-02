import math
import os
import sys
import matplotlib as mat

import numpy as num
import requests

print(sys.version)
print(sys.executable)
print("numpyversion", num.version.version)


def greet(who_to_greet):
    greeting = "Hello {}".format(who_to_greet)
    return greeting


print(greet("Hridya"))
print(greet("Arjuna"))

r = requests.get('http://www.google.com')
print(r.status_code)
