from config.schema_loader import load_schema
from config.schema_validator import validate_schemas
from src.data_loader import load_excel
from config.paths import RAW_DATA_PATH
from config.schemas import DROP_COLS
from src.preprocessing import preprocess_data
from config.schemas import ONE_HOT_COLS, ORDINAL_COLS, SCALE_COLS, SCALER_TYPE
from src.feature_engineering import encode_features, scaling_features, scaler

schema = load_schema()
validate_schemas(schema)
print("Schema Validated")

df = load_excel(RAW_DATA_PATH, drop_cols=DROP_COLS)
print(df.head())

x, y = preprocess_data(df)

X = encode_features(x, ONE_HOT_COLS, ORDINAL_COLS)
X, scaler  = scaling_features(x, SCALE_COLS, SCALER_TYPE)





