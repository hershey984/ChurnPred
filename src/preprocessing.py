import pandas as pd
from sklearn.impute import SimpleImputer
from config.schemas import TARGET_COL

def preprocess_data(df: pd.DataFrame):
    try:
        print("----------HEAD----------")
        print(df.head())
        dup = df.duplicated().sum()
        if dup > 0:
            print(f"Dropping {dup} duplicate rows")
            df = df.drop_duplicates()
        
        print("Separating Features and Target")
        X = df.drop(columns=[TARGET_COL])
        y = df[TARGET_COL]
        
        numerical_cols = X.select_dtypes(include=['int64','float64']).columns
        cat_cols = X.select_dtypes(include=['object','bool','category']).columns
        
        num_imputer = SimpleImputer(strategy="median")
        cat_imputer = SimpleImputer(strategy="most_frequent")
        X[numerical_cols] = num_imputer.fit_transform(X[numerical_cols])
        X[cat_cols] = cat_imputer.fit_transform(X[cat_cols])
        
        return X,y
    
    except Exception as e:
        print(f"Failed to preprocess data {e}")
        raise
        


