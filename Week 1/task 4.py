# Topic 4: Data Handling with Pandas – Extended
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset (Titanic)
df = sns.load_dataset("titanic")

# --- Task 1: groupby analysis ---
avg_survival = df.groupby("sex")["survived"].mean()
print("\nAverage Survival Rate by Gender:")
print(avg_survival)

# --- Task 2: Filtering with multiple conditions ---
filtered_df = df[(df['age'] > 30) & (df['fare'] > 50) & (df['survived'] == 1)]
print("\nFiltered Passengers (age > 30, fare > 50, survived):")
print(filtered_df[['sex', 'age', 'fare', 'survived']].head())

# --- Task 3: Dropping missing and duplicate rows ---
initial_shape = df.shape
df_cleaned = df.dropna().drop_duplicates()
cleaned_shape = df_cleaned.shape
print("\nOriginal shape:", initial_shape)
print("After cleaning:", cleaned_shape)
print("Impact: Rows with missing or duplicate data removed for analysis integrity.")

# --- Challenge: Dataset exploration with insights ---
# Load public dataset again to explore fresh
explore_df = sns.load_dataset("titanic")

# Clean dataset
explore_df.dropna(subset=["age", "fare", "embarked"], inplace=True)

# Insight 1: Survival rate by class
print("\nInsight 1: Survival rate by passenger class")
print(explore_df.groupby("pclass")["survived"].mean())

# Insight 2: Average fare by embarkation point
print("\nInsight 2: Average fare by embarkation port")
print(explore_df.groupby("embarked")["fare"].mean())

# Insight 3: Gender distribution in each class
print("\nInsight 3: Gender count in each class")
print(explore_df.groupby("pclass")["sex"].value_counts())

# Insight 4: Average age of survivors vs. non-survivors
print("\nInsight 4: Avg age of survivors vs. non-survivors")
print(explore_df.groupby("survived")["age"].mean())

# Insight 5: Plot - Survival by age group
plt.figure(figsize=(10, 5))
sns.histplot(data=explore_df, x="age", hue="survived", multiple="stack", bins=30)
plt.title("Survival Distribution by Age")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
