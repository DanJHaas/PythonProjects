import csv
import fileinput
from pathlib import Path
import time
t0 = time.time()
fields = {}
methods = {}
params = {}

for path in Path('MappingConversion//Mappings').rglob('*.csv'):
    with open(path, newline='') as csvfile:
        inputfile = csv.reader(csvfile, delimiter=',', quotechar='|')
        for csvinput in inputfile:
            if "fields" in path.name:
                fields[str(csvinput[0])] = str(csvinput[1])
            if "methods" in path.name:
                methods[str(csvinput[0])] = str(csvinput[1])
            if "params" in path.name:
                params[str(csvinput[0])] = str(csvinput[1])




for path in Path('witchery').rglob('*.java'):
    for line in fileinput.input(path, inplace=True):
        line = line.rstrip()
        if not line:
            continue
        for key, val in fields.items():
            if key in line:
                line = line.replace(key, val)
        for key, val in methods.items():
            if key in line:
                line = line.replace(key, val)
        for key, val in params.items():
            if key in line:
                line = line.replace(key, val)
        print(line)


t1 = time.time() - t0
print(t1)