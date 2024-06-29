import pandas as pd
import sys

#some stuff
print("job finished successfully")

# parameters passed after python script.py arg1 arg2
print("iterating through sys.argv")
for n, val in enumerate(sys.argv):
    print(n, val)

print("\n sys.argv as a list:",sys.argv)

