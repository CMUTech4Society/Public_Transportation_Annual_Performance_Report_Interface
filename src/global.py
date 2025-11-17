class PlotStruct:
    def __init__(self, meta, x_axis, y_axis, x_filter, y_filter, multiplier):
        self.meta = meta                # None
        self.x_axis = x_axis            # dataset
        self.y_axis = y_axis            # dataset
        self.x_filter = x_filter        # None/[filter]
        self.y_filter = y_filter        # None/[filter]
        self.multiplier = multiplier    # None/[filter]

class dataset:
    def __init__(self, label, dataframe):
        self.label = label
        self.dataframe = dataframe

class filter:
    def __init__(self, label, func):
        self.label = label
        self.func = func 
