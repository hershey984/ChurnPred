from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
import pandas as pd

def encode_features(
        X: pd.DataFrame,
        one_hot_cols: list=None,
        ordinal_cols: list=None
) -> pd.DataFrame:
    
    X_encoded = X.copy()

    if ordinal_cols:
        ord_encoder = OrdinalEncoder()
        X_encoded[ordinal_cols] = ord_encoder.fit_transform(X_encoded[ordinal_cols])
    
    if one_hot_cols:
        pass
    
