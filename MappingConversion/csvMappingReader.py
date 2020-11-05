import csv
import fileinput
from pathlib import Path
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
            # f.write("{0},{1}\n".format(columns[0],columns[1]))




for path in Path('rscircuits').rglob('*.java'):
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

