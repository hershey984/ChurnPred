from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
import pandas as pd

def encode_features(
        X: pd.DataFrame,
        one_hot_cols: list=None,
        ordinal_cols: list=None
) -> pd.DataFrame:
    
    X_encoded = X.copy()

    if not one_hot_cols and not ordinal_cols:
        raise ValueError("no columns provided")

    if ordinal_cols:
        ord_encoder = OrdinalEncoder()
        X_encoded[ordinal_cols] = ord_encoder.fit_transform(X_encoded[ordinal_cols])
    
    if one_hot_cols:
        ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
        
        ohe_array = ohe.fit_transform(X_encoded[one_hot_cols])
        ohe_col = ohe.get_feature_names_out(X_encoded[one_hot_cols])

        ohe_df = pd.DataFrame(
            ohe_array,
            columns=ohe_col,
            index=X_encoded.index
        )

        X_encoded = X_encoded.drop(columns=one_hot_cols)
        X_encoded = pd.concat([X_encoded, ohe_df], axis=1)

    return X_encoded


