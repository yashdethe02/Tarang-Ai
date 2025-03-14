import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.calibration import CalibratedClassifierCV
import warnings
import pickle
warnings.filterwarnings("ignore")

df = pd.read_csv("used_sorted_water_data.csv", encoding="latin1")

state_mapping = {state: code for code, state in enumerate(df["STATE"].astype("category").cat.categories)}
reverse_state_mapping = {v: k for k, v in state_mapping.items()}
df["STATE"] = df["STATE"].astype("category").cat.codes

df.replace("NAN", np.nan, inplace=True)
df = df.apply(pd.to_numeric, errors='coerce')

safe_conditions = (
    (df["Temp"] >= 0) & (df["Temp"] <= 35) &
    (df["D.O. (mg/l)"] >= 4) &
    (df["PH"] >= 6) & (df["PH"] <= 9) &
    (df["CONDUCTIVITY (µmhos/cm)"] <= 1500) &
    (df["B.O.D. (mg/l)"] <= 3) &
    (df["NITRATENAN N+ NITRITENANN (mg/l)"] <= 45) &
    (df["FECAL COLIFORM (MPN/100ml)"] <= 100)
)

df["Water Safety"] = np.where(safe_conditions, 1, 0) 

train, test = train_test_split(df, test_size=0.2, random_state=42, stratify=df["Water Safety"])

x_train = train[train.columns[:-1]]
y_train = train[train.columns[-1]].values

x_test = test[test.columns[:-1]]
y_test = test[test.columns[-1]].values

numerical_cols = x_train.columns

preprocessor = ColumnTransformer(
    transformers=[
        ("num", Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="mean")), 
            ("scaler", StandardScaler())  
        ]), numerical_cols),  
    ]
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(random_state=42, class_weight="balanced")), 
    ]
)

calibrated_model = CalibratedClassifierCV(model, method='sigmoid', cv=5)

calibrated_model.fit(x_train, y_train)

y_pred = calibrated_model.predict(x_test)
y_proba = calibrated_model.predict_proba(x_test)

inputt = [float(x) for x in "5 24.5 6 7 332 6 1.2 8.2".split(' ')]
final = pd.DataFrame([inputt], columns=x_train.columns)  

b = calibrated_model.predict_proba(final)

pickle.dump(calibrated_model, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl', 'rb'))

b_loaded = model.predict_proba(final)
print(b_loaded)



# FOLLOWING COMMENTED CODE IS TO MAKE PREDICTION HERE ON BACKEND:

# print("\nModel Evaluation:\n", classification_report(y_test, y_pred))

# print("\nEnter values for prediction:")
# user_input = []
# for col in x_train.columns:
#     value = float(input(f"{col}: "))
#     user_input.append(value)

# user_input_df = pd.DataFrame([user_input], columns=x_train.columns)

# probabilities = calibrated_model.predict_proba(user_input_df)

# prob_safe = probabilities[0][1] * 100
# prob_unsafe = probabilities[0][0] * 100

# print("\nPrediction Probabilities (in %):")
# print(f"SAFE: {prob_safe:.2f}%")
# print(f"UNSAFE: {prob_unsafe:.2f}%")

# final_prediction = "SAFE" if prob_safe > prob_unsafe else "UNSAFE"
# print(f"\nFinal Prediction: {final_prediction}")



# # TO PLOT HISTOGRAM
# for label in df.columns[1:-1]: 
#     plt.hist(df[df["Water Safety"] == 1][label], color='blue', label='Safe', alpha=0.7, density=True)
#     plt.hist(df[df["Water Safety"] == 0][label], color='red', label='Unsafe', alpha=0.7, density=True)
#     plt.title(label)
#     plt.ylabel("Probability")
#     plt.xlabel(label)
#     plt.legend()
#     plt.show()


# # HEATMAP KA PLOT
# import seaborn as sns
# plt.figure(figsize=(10, 8))
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
# plt.title("Feature Correlation Heatmap")
# plt.show()