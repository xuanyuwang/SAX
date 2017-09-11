from utility.readFiles import *
from utility.readLines import *
from discretization.symbolize import *
from reduceDim.PAA import *
import sys

if __name__ == "__main__":
    # parameters = sys.argv[1:]
    # dataFolder = parameters[0]
    # widthOfTimeSegment = parameters[1]
    # alphabetSize = parameters[2]
    parameters = ["dataFiles", 16, 9]
    dataFolder = parameters[0]
    widthOfTimeSegment = parameters[1]
    alphabetSize = parameters[2]

    allDataFilePath = getPathesOfDataFiles(dataFolder)
    inputLines = getLinesFromDataFiles(allDataFilePath)
    timeSegments = getDataPointsInATimeSegment(widthOfTimeSegment, inputLines)

    reducedTS = PAA(timeSegments)
    numberOfRecords = getNumberOfRecords(getPathesOfDataFiles(dataFolder))
    symbols = symbolize(reducedTS, alphabetSize, widthOfTimeSegment, numberOfRecords)
    for sym in symbols:
        print(sym)
    # with open("symbols.txt", 'w') as file:
    #     for symbol in symbols:
    #         file.write(symbol)


