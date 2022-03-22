import os
import numpy as np


def getfiles_walk(inputpath, exts=None, keys=None, min_size=None, max_size=None):
    rez = []
    for dirpath, dirnames, filenames in os.walk(inputpath):
        for filename in filenames:
            filterTestsPass = [
                (exts is None) or os.path.splitext(filename)[1] in exts,
                (keys is None) or np.all([key in filename for key in keys]),
                (min_size is None) or (os.path.getsize(os.path.join(dirpath, filename)) > min_size),
                (max_size is None) or (os.path.getsize(os.path.join(dirpath, filename)) < max_size)
            ]

            if np.all(filterTestsPass):
                rez += [(dirpath, filename)]
    return np.array(rez)