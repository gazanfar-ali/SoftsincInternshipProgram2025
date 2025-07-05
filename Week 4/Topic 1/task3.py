import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load dataset
titanic = sns.load_dataset("titanic").dropna(subset=['age', 'fare', 'embarked', 'sex', 'survived'])

# Feature Selection
X = titanic[['age', 'fare', 'embarked', 'sex']]
y = titanic['survived']

# Encode categorical features
X['sex'] = LabelEncoder().fit_transform(X['sex'])
X['embarked'] = LabelEncoder().fit_transform(X['embarked'])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train and Evaluate
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
preds = model.predict(X_test_scaled)

print("\n🔹 Logistic Regression on Titanic")
print("Accuracy:", accuracy_score(y_test, preds))
print("Confusion Matrix:\n", confusion_matrix(y_test, preds))
