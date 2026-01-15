import pandas as pd
from config.paths import RAW_DATA_PATH
from config.schema_loader import load_schema
from config.schema_validator import validate_schemas
from config.schemas import BIN_COLS, CAT_COLS, DROP_COLS, NUM_COLS, TARGET_COL
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from src.data_loader import load_excel

# Load and validate schema
schema = load_schema()
validate_schemas(schema)

# Load dataset
df = load_excel(RAW_DATA_PATH, drop_cols=DROP_COLS)

print(f"[INFO] Dataset shape: {df.shape}")
print(f"[INFO] Target column: {TARGET_COL}")
print(f"[INFO] Numeric columns: {len(NUM_COLS)}")
print(f"[INFO] Categorical columns: {len(CAT_COLS)}")

# Separate target and features
X = df.drop(TARGET_COL, axis=1)
y = df[TARGET_COL]

# Encode categorical columns
le_dict = {}
for col in CAT_COLS:
    if col in X.columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        le_dict[col] = le

# Encode target variable
le_target = LabelEncoder()
y = le_target.fit_transform(y)

print(f"[INFO] Encoded {len(CAT_COLS)} categorical columns")
print(f"[INFO] X shape: {X.shape}, y shape: {y.shape}")

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"[INFO] Train set size: {X_train.shape[0]}, Test set size: {X_test.shape[0]}")

# Initialize the model
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)

# Train the model
print("[INFO] Training Random Forest model...")
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
print("\n[RESULTS] Confusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("\n[RESULTS] Classification Report:")
print(classification_report(y_test, predictions, target_names=[str(x) for x in le_target.classes_]))
print(f"\n[RESULTS] Accuracy: {accuracy_score(y_test, predictions):.4f}")

# Feature importance
print("\n[INFO] Top 10 Important Features:")
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print(feature_importance.head(10))
