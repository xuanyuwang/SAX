from utility import readFiles
from utility import readLines

if __name__ == "__main__":
    pathes= readFiles.getPathesOfDataFiles("dataFiles")
    lines = readLines.getLinesFromDataFiles(pathes)
    for line in lines:
        print(line)
