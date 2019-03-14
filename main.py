import os
import pathlib
import time

scanFolder = pathlib.Path('D:/Scans')
daysToKeep = 5

secondsToKeep = daysToKeep * 60 * 60 * 24
deleteOlderThan = time.time() - secondsToKeep

for item in os.listdir(scanFolder):
    currentFilePath = scanFolder / item
    if os.path.isfile(currentFilePath):
        if os.path.getmtime(currentFilePath) < deleteOlderThan:
                os.remove(currentFilePath)