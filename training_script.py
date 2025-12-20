import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# ==========================================
# 1. LOAD THE CLEAN DATA
# ==========================================
print("Loading data...")
try:
    df = pd.read_csv('data/leads_cleaned.csv')
except FileNotFoundError:
    print("Error: File not found. Make sure 'leads_cleaned.csv' is inside the 'data' folder.")
    exit()

# ==========================================
# 2. PREPROCESSING (ENCODING)
# ==========================================
# Convert categorical variables to numerical values using One-Hot Encoding
# This creates columns like "Occupation_Student", "Lead Source_Google", etc.
print("Encoding categorical features...")
df_encoded = pd.get_dummies(df, drop_first=True)

# Separate features (X) and target (y)
X = df_encoded.drop('Converted', axis=1)
y = df_encoded['Converted']

# ==========================================
# 3. SAVE COLUMN NAMES (CRITICAL STEP)
# ==========================================
# Save feature column names so the app can match inputs correctly
print("Saving model columns...")
joblib.dump(X.columns, 'model_columns.pkl')

# ==========================================
# 4. SPLIT & SCALE
# ==========================================
print("Splitting and scaling data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features (important for Logistic Regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save the scaler for later use in the app
joblib.dump(scaler, 'scaler.pkl')

# ==========================================
# 5. TRAIN THE MODEL
# ==========================================
print("Training Logistic Regression model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# ==========================================
# 6. EVALUATE & SAVE
# ==========================================
y_pred = model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {acc:.2%}")

# Save the trained model
joblib.dump(model, 'lead_scoring_model.pkl')
print("Training completed. Model saved as 'lead_scoring_model.pkl'")
