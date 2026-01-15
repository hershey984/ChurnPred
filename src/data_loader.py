import pandas as pd

def load_excel(file_path:str, drop_cols: list = None) -> pd.DataFrame:
    #loads the excel file and drops unwanted columns

    try:
        df = pd.read_excel(file_path)

        #remove whitespace from column name
        df.columns = df.columns.str.strip()

        #remove unwanted cols
        if drop_cols:
            to_drop = []
            missing_cols = []

            for col in drop_cols:
                if col in df.columns:
                    to_drop.append(col)
                else:
                    missing_cols.append(col)

            if to_drop:
                df = df.drop(columns=to_drop)

        #warnings for missing cols
            if missing_cols:
                print(f"[WARNING] These cols were not found in the dataset: {missing_cols}")
          
            if to_drop:
                print(f"[INFO] Dropped columns:{to_drop}")
        
        print(f"[INFO] Loaded '{file_path}' with {df.shape[0]} rows and {df.shape[1]} columns")

        return df
    
    except FileNotFoundError:
        print(f"[ERROR] File not found at: {file_path} ")
        raise

    except Exception as e:
        print(f"[ERROR] Failed to load file: {e}")
        raise
