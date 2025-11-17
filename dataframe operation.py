import pandas as pd
from typing import Callable, List, Union
def data_underscore_query(
        X: pd.DataFrame,
        Y: pd.DataFrame,
        X_filter: pd.DataFrame,
        Y_filter: pd.DataFrame,
        multiplier: pd.DataFrame,
)-> tuple[pd.DataFrame, pd.DataFrame]:
        #Apply condition for X
        X_result = X.copy()
        if X_filter:
            combined_mask = pd.Series(True, index=X.index)
            for func in X_filter:
                mask = func(X_result)
                if not isinstance(mask, (pd.Series, np.ndarray)):
                    raise ValueError(
                        "One of the X filters did NOT return a Boolean mask."
                    )
                combined_mask &= mask
            X_result = X_result[combined_mask]
        #Apply condition for Y
        Y_result = Y.copy()
        if Y_filter:
            combined_mask = pd.Series(True, index=Y.index)
            for func in Y_filter:
                mask = func(Y_result)
                if not isinstance(mask, (pd.Series, np.ndarray)):
                    raise ValueError(
                        "One of the Y filters did NOT return a Boolean mask."
                    )
                combined_mask &= mask
            Y_result = Y_result[combined_mask]
        #Apply Multiplier to Filtered X
        if multiplier:
            for func in multiplier:
                X_result = func(X_result)

        return X_result, Y_result

        