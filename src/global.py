class PlotStruct:
    def __init__(self, meta, x_axis, y_axis, x_filter, y_filter, multiplier):
        self.meta = meta                # None
        self.x_axis = x_axis            # Dataset
        self.y_axis = y_axis            # Dataset
        self.x_filter = x_filter        # None/[Filter]
        self.y_filter = y_filter        # None/[Filter]
        self.multiplier = multiplier    # None/[Filter]

class Dataset:
    def __init__(self, label, dataframe):
        self.label = label
        self.dataframe = dataframe

class Filter:
    def __init__(self, label, func):
        self.label = label
        self.func = func
