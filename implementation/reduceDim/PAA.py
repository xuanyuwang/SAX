from utility import readLines
from utility import readFiles
from utility.record import record

def getDataPointsInATimeSegment(widthOfTimeSegment, lines):
    """

    :param widthOfTimeSegment: the number of data points a time segment has
    :return: A generator which will yield many data points within a time segment.
    :note: For the last time segment, there might be less data points if:
            (total number of data points) mod (width of time segment) != 0
    """
    dataPoints = list()
    # Bundle each w data points together and return
    for line in lines:
        index, value = line.split()
        dataPoints.append(float(value))
        if len(dataPoints) == widthOfTimeSegment:
            yield dataPoints
            dataPoints.clear()
    # For the last a few lines, return them directly
    if len(dataPoints) != 0:
        yield dataPoints

def PAA(timeSegments):
    """

    :param timeSegments: A generator of _getDataPointsInATimeSegment. Each element is a collection of
            data points within a time segment.
    :return:
    """
    index = 0
    for segment in timeSegments:
        index += len(segment)
        yield (index, sum(segment) / len(segment))
