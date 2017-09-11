import os.path
import pathlib

def getFileTree(pathOfDataFolder):
    """

    :param rootDir: The root directory of data files
    :return: A generator, which will generate the file tree in a top-down way.
    """
    return os.walk(pathOfDataFolder, topdown=True)

def getPathOfDataFolder(dataFolderName):
    """

    :param dataFilesDirName: The name of the directory of data files
    :return: The path of the root of data file directory
    """
    pathOfCurrentDir = pathlib.Path(__file__).resolve().parent # It should be the directory of utility
    pathOfImplementationDir = pathOfCurrentDir.parent
    pathOfDataFilesRootDir = pathOfImplementationDir.parent.joinpath(dataFolderName)
    return pathOfDataFilesRootDir

def getPathesOfDataFiles(dataFolerName):
    """

    :param dataFileTree: A generator produce all data files' pathes
    :return: A generator will be iterated, which contains all files' path under the root data directory
    """
    pathOfDataFolder = getPathOfDataFolder(dataFolerName)
    fileTree = getFileTree(pathOfDataFolder)
    for branch in fileTree:
        dirPath, fileNames = branch[0], branch[2]
        for file in fileNames:
            yield os.path.join(dirPath, file)