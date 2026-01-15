import schemas

def validate_schemas(schema):
    # validates the loaded schema
    if not schema.get("target"):
        raise ValueError("Target column not defined")
    
    feature_cols = [
        *schemas.get("numerical", []),
        *schemas.get("categorical", []),
        *schemas.get("binary", [])
    ]

    if not feature_cols:
        raise ValueError("No Feature Colums Defined")
    
    if len(feature_cols) != len(set(feature_cols)):
        raise ValueError("Dupliacte Columns exist")
    
    return True 