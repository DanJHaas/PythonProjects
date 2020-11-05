import csv
import fileinput
from pathlib import Path
import time
t0 = time.time()
mappings = {}
lineschanged = 0

for path in Path('MappingConversion//Mappings').rglob('*.csv'):
    with open(path, newline='') as csvfile:
        inputfile = csv.reader(csvfile, delimiter=',', quotechar='|')
        for csvinput in inputfile:
            mappings[str(csvinput[0])] = str(csvinput[1])

for path in Path('MappingConversion//ModFile').rglob('*.java'):
    for line in fileinput.input(path, inplace=True):
        line = line.rstrip()
        if not line:
            continue
        if "func_" or "field_" or "p_" in line:
            for key, val in mappings.items():
                if key in line:
                    line = line.replace(key, val)
                    lineschanged = lineschanged+1
        print(line)

t1 = time.time() - t0
print(t1)
print(len(mappings))
print(lineschanged)
