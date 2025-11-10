import pandas as pd
from typing import Dict, Tuple, Union, List
def data_underscore_query(
        X: pd.DataFrame,
        Y: pd.DataFrame,
        filters: pd.DataFrame,
        merge_key: str,
        conditions: Dict[str, Union[Tuple[str, float], float]],
        multiplier_col: str = None,
        multiplier: float = 1.0
)-> Tuple[pd.DataFrame, pd.DataFrame]:
        #Apply each cross-frame condition
    for name, func in conditions.items():
        mask = func(X, Y, df_filtered)
        if not isinstance(mask, pd.Series) or mask.dtype != bool:
            raise ValueError(f"Condition '{name}' must return a boolean Series mask.")
        if len(mask) != len(df_filtered):
            raise ValueError(f"Mask length mismatch for condition '{name}'.")
        df_filtered = df_filtered[mask]
        # Keep only merge key
    df_filtered = df_filtered[[merge_key]].drop_duplicates()
        #Merge with X and Y
    X_filtered = pd.merge(X, df_filtered, on=merge_key, how='inner')
    Y_filtered = pd.merge(Y, df_filtered, on=merge_key, how='inner')
        # Optional multiplier
    if multiplier_col and multiplier_col in X_filtered.columns:
        X_filtered[multiplier_col] *= multiplier

    return X_filtered, Y_filtered