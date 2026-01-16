from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from config.model_config import MODEL_PARAMS

def get_model(model_nae: str):
    model_name = model_name.lower()
    params = MODEL_PARAMS.get(model_name, {})

    if model_name == "logistic":
        return LogisticRegression(**params)
    
    elif model_name == "random_forest":
        return RandomForestClassifier(**params)
    
    else:
        raise ValueError(f"Unsupported Model: {model_name}")
    