from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

def scaling_features(
        X: pd.DataFrame,
        scaling_cols: list,
        scaler_type: str = "standard" 
):
    
    X_scaled = X.copy()
    
    if not scaling_cols:
        raise ValueError("No columns provided")
    
    if scaler_type == "standard":
        scaler = StandardScaler()
    elif scaler_type == "minmax":
        scaler = MinMaxScaler()
    else:
        raise ValueError("must be of type standard or minmax")
    
    X_scaled[scaling_cols] = scaler.fit_transform(X_scaled[scaling_cols])

    return X_scaled, scaler

