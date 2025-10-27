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
    