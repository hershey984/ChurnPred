from config.schema_loader import load_schema
from config.schema_validator import validate_schemas
from src.data_loader import load_excel
from config.paths import RAW_DATA_PATH
from config.schemas import DROP_COLS

schema = load_schema()
validate_schemas(schema)

df = load_excel(RAW_DATA_PATH, drop_cols=DROP_COLS)
print(df.head())

print("Schema Validated")