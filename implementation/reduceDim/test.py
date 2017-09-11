from reduceDim.PAA import *
from utility.readLines import *
from utility.readFiles import *

allPathes = readFiles.getPathesOfDataFiles("dataFiles")
lines = getLinesFromDataFiles(allPathes)
ts = getDataPointsInATimeSegment(16, lines)
paa = PAA(ts)
for t in paa:
    print(t)