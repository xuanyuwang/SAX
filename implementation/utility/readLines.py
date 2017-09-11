from utility import readFiles


def getLinesFromDataFiles(allDataFilePath):
    """

    :param allDataFilePath: A list or a generator contains all data files' pathes
    :return: Lines of all data files.
    """
    for filePath in allDataFilePath:
        with open(filePath, 'r') as dataFile:
            for line in dataFile:
                yield line.strip()