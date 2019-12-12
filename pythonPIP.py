# Python PIP: pythonPIP.py

import camelcase

cC = camelcase.CamelCase()

text = "HELLO UNIVERSE";

print("Before: "+text)
print("Now: "+cC.hump(text))

