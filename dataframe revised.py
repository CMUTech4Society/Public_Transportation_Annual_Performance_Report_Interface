import pandas as pd

def process_frames(X, Y, X_filters, Y_filters, multipliers):
    #Apply filters to X
    for f in X_filters:
        mask = X.apply(f, axis=1)
        X = X.loc[mask]

    #Apply filters to Y
    for f in Y_filters:
        mask = Y.apply(f, axis=1)
        Y = Y.loc[mask]

    # Apply multipliers to X AFTER filtering
    for m in multipliers:
        X["value"] = X.apply(m, axis=1)

    return X, Y
