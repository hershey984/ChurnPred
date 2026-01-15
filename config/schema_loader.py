from . import schemas

#loading schema and returning dictionary
def load_schema():
    return{
        "drop":schemas.DROP_COLS,
        "target":schemas.TARGET_COL,
        "numeric":schemas.NUM_COLS,
        "categorical":schemas.CAT_COLS,
        "binary":schemas.BIN_COLS
    }